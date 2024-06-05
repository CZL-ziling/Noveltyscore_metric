# Different types of classification of entity combinations
import pandas as pd
import json
id2ent={}
ent2id = json.loads(open('./ent2id/ent2id_all.txt', 'r', encoding='utf-8').read())
ent2id_method = json.loads(open('./ent2id/ent2id_method.txt', 'r', encoding='utf-8').read())
ent2id_dataset = json.loads(open('./ent2id/ent2id_dataset.txt', 'r', encoding='utf-8').read())
ent2id_tool = json.loads(open('./ent2id/ent2id_tool.txt', 'r', encoding='utf-8').read())
ent2id_metric = json.loads(open('./ent2id/ent2id_metric.txt', 'r', encoding='utf-8').read())
for i ,j in enumerate(ent2id):
    id2ent[i]=j

ent_ent_method=[]
ent_ent_dataset=[]
ent_ent_tool=[]
ent_ent_metric=[]

with open('./sims/sims.txt',encoding='utf8') as f:
    for line in f:
        a=line.split('\t')
        qian = a[0].split('-')[0]
        hou = a[0].split('-')[1]
        qian_entity_name =  id2ent[int(qian)]
        hou_entity_name =  id2ent[int(hou)]


        if qian_entity_name in ent2id_method.keys() and hou_entity_name in ent2id_method.keys():
            ent_ent_method.append(a[0])
        elif qian_entity_name in ent2id_dataset.keys() and hou_entity_name in ent2id_dataset.keys():
            ent_ent_dataset.append(a[0])
        elif qian_entity_name in ent2id_tool.keys() and hou_entity_name in ent2id_tool.keys():
            ent_ent_tool.append(a[0])
        elif qian_entity_name in ent2id_metric.keys() and hou_entity_name in ent2id_metric.keys():
            ent_ent_metric.append(a[0])


with open('./sims/ent_ent_metric.txt', 'w') as file:
    for item in ent_ent_metric:
        file.write(f"{item}")

with open('./sims/ent_ent_method.txt', 'w') as file:
    for item in ent_ent_method:
        file.write(f"{item}")

with open('./sims/ent_ent_tool.txt', 'w') as file:
    for item in ent_ent_tool:
        file.write(f"{item}")

with open('./sims/ent_ent_dataset.txt', 'w') as file:
    for item in ent_ent_dataset:
        file.write(f"{item}")


#Calculate fine-grained novelty scores based on combinations of different types of entities
from itertools import combinations
import pandas as pd


df=pd.read_excel('./id2id/initialenttoid.xlsx')
ids=df[df.columns[1]].tolist()
ent2=[]
print(len(ids))
with open('./sims/sims.txt',encoding='utf8') as f:
    for line in f:
        a=line.split('\t')
        ent2.append(a[0])
index =int( len(ent2) )

i=0
score={}
method_ration = {}
dataset_ration = {}
tool_ration = {}
metric_ration = {}
for id in ids:
    i += 1
    id=eval(id)
    ids = sorted(id)
    if len(ids)<2:
        novelty=0
        score[i] = novelty
        method_ration[i] = novelty
        dataset_ration[i] = novelty
        tool_ration[i] = novelty
        metric_ration[i] = novelty
    else:
        combs = combinations(ids, 2)
        n, l,method,dataset,tool,metric =0,0,0,0,0,0
        for c in combs:
            l += 1
            if f'{c[0]}-{c[1]}' in ent2:
                n+=1
            if f'{c[0]}-{c[1]}' in ent_ent_method:
                method+=1
            if f'{c[0]}-{c[1]}' in ent_ent_dataset:
                dataset+=1
            if f'{c[0]}-{c[1]}' in ent_ent_tool:
                tool+=1
            if f'{c[0]}-{c[1]}' in ent_ent_metric:
                metric+=1
        if n ==0:
            method_ration[i] = 0
            dataset_ration[i] = 0
            metric_ration[i] = 0
            tool_ration[i] = 0
            score[i] = 0
        else:
            method_novelty =  method/n
            method_ration[i] = method_novelty
            dataset_novelty = dataset/n
            dataset_ration[i] = dataset_novelty
            tool_novelty = tool/n
            tool_ration[i] = tool_novelty
            metric_novelty = metric/n
            metric_ration[i] = metric_novelty
            score[i]=n/l
        if i % 500 == 0:
            print(i)

df=pd.DataFrame(dataset_ration.items(),columns=['id','score'])
df.to_excel('./score/score_dataset.xlsx')
df=pd.DataFrame(method_ration.items(),columns=['id','score'])
df.to_excel('./score/score_method.xlsx')
df=pd.DataFrame(tool_ration.items(),columns=['id','score'])
df.to_excel('./score/score_tool.xlsx')
df=pd.DataFrame(metric_ration.items(),columns=['id','score'])
df.to_excel('./score/score_metric.xlsx')
