# Fine-grained novelty score calculation
import pandas as pd
import json
id2ent={}
ent2id = json.loads(open('./ent2id/ent2id_all(2).txt', 'r', encoding='utf-8').read())
ent2id_method = json.loads(open('./ent2id/ent2id_method(2).txt', 'r', encoding='utf-8').read())
ent2id_dataset = json.loads(open('./ent2id/ent2id_dataset(2).txt', 'r', encoding='utf-8').read())
ent2id_tool = json.loads(open('./ent2id/ent2id_tool(2).txt', 'r', encoding='utf-8').read())
ent2id_metric = json.loads(open('./ent2id/ent2id_metric(2).txt', 'r', encoding='utf-8').read())
for i ,j in enumerate(ent2id):
    id2ent[i]=j


ent_ent_method=[]
ent_ent_dataset=[]
ent_ent_tool=[]
ent_ent_metric=[]

if 'fscore' in ent2id_metric.keys():
    print('jj ')
with open('./sims/sims(qian10).txt',encoding='utf8') as f:
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

b={}
for i in ent_ent_method:
    b[i.strip()]='method'
for j in ent_ent_dataset:
    b[j.strip()]='dataset'
for k in ent_ent_tool:
    b[k.strip()]='tool'
for l in ent_ent_metric:
    b[l.strip()]='metric'

with open('./sims/ent_ent.txt', 'w') as file:
    json.dump(b, file)