'''Extract entity data from the dictionary'''
import re
import pandas as pd

# Determined based on the type of entity you want to match
tool=[]

with open('./initial_entitydata/ent-text-79-22.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    ent_lists=[]
    for idx, line in enumerate(lines):
        if idx%1000==0:
            print(idx)
        ents = re.findall(r"<entity_(Tool)>(.*?)</entity_(Tool)>", line)
        # ents = re.findall(r"<entity_(Metric|Method|Dataset|Tool)>(.*?)</entity_(Metric|Method|Dataset|Tool)>", line)
        ent_list = []
        for e in ents:

            ent_list.append([e[0].lower(), e[1].lower()])
        str(ent_list)
        ent_lists.append(str(ent_list))
with open('./initial_entitydata/tool.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(ent_lists))

# Extract basic information
f = open(r"./initial_entitydata/ent-text-79-22.txt" ,encoding='utf-8')
file_content =f.read()


l_id = re.findall(r'"id":(.+?),' ,file_content)
l_year = re.findall(r'"year":(.+?),' ,file_content)
l_title = re.findall(r'"title":(.+?),' ,file_content)

all_info =[]
for i in range(len(l_id)):
    each_info ={}
    each_info['id' ] =l_id[i]
    each_info['year' ] =l_year[i]
    each_info['title' ] =l_title[i]
    all_info.append(each_info)

df1 =pd.DataFrame(all_info)
df1.to_excel(r'quchong.xlsx', index=False)

# Generate a table of entity frequencies
import  json
from collections import Counter, defaultdict
all_ent=[]
d = defaultdict(int)
with open('./initial_entitydata/tool.txt') as f:
    lines = f.readlines()
    for line in lines:
        entity=eval(line)
        for ent in entity:
            d[ent[1]] += 1
ent2id = {}

result_sorted = sorted(d.items(),key = lambda x:x[1], reverse = True)
m=0
for i in result_sorted:
   ent2id[i[0]]=m
   m+=1
with open('./ent2id/ent2id_tool.txt', 'w', encoding='utf8') as f:
    json.dump(ent2id, f, indent=4)

res = []
for i in result_sorted:
    res.append(f'{i[0]}\t{i[1]}')

with open('./ee/ee_tool.txt', 'w', encoding='utf8') as f:
    f.write('\n'.join(res))
    
# Get word vectors
from gensim.models import Word2Vec, KeyedVectors
#The load_model function in the import fasttext module is used to import the pre-trained ftt.model
from fasttext import load_model
from gensim.models import Word2Vec
import json


def get_vec(path, model_path):
    ftt_model = load_model(model_path)
    ents = []
    vecs=[]
    with open(path, encoding='utf8') as f:
        content = f.read()
        dictionary = eval(content)
        for key in dictionary:
           id=dictionary[key]
           v=ftt_model.get_word_vector(key)
           v = list(v)
           v.insert(0, id)
           v = map(str, v)
           vecs.append(' '.join(v))

           if len(vecs)==10000:
               with open('./vecs/vecs_tool.txt', 'a', encoding='utf8') as f:
                   f.write('\n'.join(vecs)+'\n')
                   vecs = []
                   print(id + 1)

        if vecs:
            with open('./vecs/vecs_tool.txt', 'a', encoding='utf8') as f:
                f.write('\n'.join(vecs) + '\n')
            print(id + 1)

if __name__ == '__main__' :
    get_vec("./ent2id/ent2id_tool.txt","ftt.model")
    model = KeyedVectors.load_word2vec_format("./vecs/vecs_tool.txt", binary=False, no_header=True)
    model.save_word2vec_format("./vecs/vecs_tool.bin", binary=True)
  
  
#Codify the initial paper entity
restr = r"[\@()/.\w\s\-]+"
entityset = set(['method', 'dataset', 'tool', 'metric', ' '])
ent2id = json.loads(open('./ent2id/ent2id_tool.txt', 'r', encoding='gbk').read())
entity=[]
lengths=[]
def entid_match(entity):
    id = []
    for ety in entity:
        if ety[1] in ent2id:
            id.append(ent2id[ety[1]])
    id=list(set(id))
    id.sort(reverse=False)
    return id
entid = {}
df = pd.DataFrame(columns=["Lists"])
entid={}
with open('./initial_entitydata/ent_lists(tool).txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        entity=eval(line)
        lst = entid_match(entity)
        df.loc[len(df)] = [lst]

df.to_excel('./id2id/initialenttoid_tool.xlsx')


# Novelty Score Measure
from gensim.models import KeyedVectors
from itertools import combinations
import pandas as pd

df= pd.read_excel('./id2id/initialenttoid_tool.xlsx')
ids=df[df.columns[1]].tolist()
model = KeyedVectors.load_word2vec_format('./vecs/vecs_tool.bin', binary=True, unicode_errors='ignore')

res, i = [], 0

for k in ids:
    i += 1
    ids=eval(k)
    ids = sorted(ids)
    if len(ids)<1: continue
    combs = combinations(ids, 2)
    for c in combs:
        sim = model.similarity(str(c[0]), str(c[1]))
        res.append(f'{c[0]}-{c[1]}\t{sim}')
    if i%500==0:
        with open('./sims/sims_tool.txt', 'a', encoding='utf8') as f:
            f.write('\n'.join(res)+'\n')
        res = []
        print(i)
if res:
    with open('./sims/sims_tool.txt', 'a', encoding='utf8') as f:
        f.write('\n'.join(res))
        print(i)

import json
from itertools import combinations
import pandas as pd
df=pd.read_excel('./id2id/initialenttoid(2).xlsx')
ids=df[df.columns[1]].tolist()
ent2=[]
with open('./sims/sims(2).txt',encoding='utf8') as f:
    for line in f:
        a=line.split('\t')

        ent2.append(a[0])
    # print(ent2)
index =int( len(ent2) )

# ent3=set(ent2[:index])
# print(len(ent3))
ent2.sort(key=lambda x: x[1])
ent3=ent2[:int(index*0.1)]
print(ent3)
i=0
score={}
for id in ids:
    i += 1
    id = eval(id)
    if len(id)<2:
        novelty=0
        score[i] = novelty
    else:
        combs = combinations(id, 2)
        n, l =0, 0
        for c in combs:
            l += 1
            if f'{c[0]}-{c[1]}' in ent3:
                n+=1
        novelty=n/l
        score[i]=novelty
        if i % 500 == 0:
            print(i)

with open('score.txt', 'w', encoding='utf-8') as file:
    json.dump(score, file, indent=4)


