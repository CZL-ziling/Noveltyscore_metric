# Exploring the Relationship Between Team Institutional Composition and Novelty in Academic Papers Based on Fine-Grained Knowledge Entities
## Overview

**Dataset and source code for paper "Exploring the Relationship Between Team Institutional Composition and Novelty in Academic Papers Based on Fine-Grained Knowledge Entities".**.
In this study, the novelty of three major conference papers in the field of NLP was measured.Our work includes the followig aspects:

* The purpose of this paper is to analyze the relationship between the type of team institution and the novelty of the paper. First, the author's institution is extracted, the name of the institution is collected through [GRID](https://grid.ac/), and the institution data is supplemented with Wikipedia and [GeoNames data](https://www.geonames.org/). The types of team institutions are divided into three categories: academia, mixed academia and industry, and industry.
* We use [Zhang's model](https://github.com/ZH-heng/technology_development) to extract the method entities in the paper. The novelty of the paper is measured based on the fine-grained entities extracted. The novelty is further explained from the proportion of atypical entity combinations. The novelty of the measurement was correlated with the type of institution.

## Main findings

* significant differences in the novelty of academic papers are observed among different types of team institutional compositions. It is found that academic institutions and mixed academic and industrial institutions produce papers with higher novelty compared to papers from industrial institutions.
  
 ![WPS图片(2)](https://github.com/CZL-ziling/Noveltyscore_metric/assets/156270701/4861f471-3345-4c0f-a367-b82e1b8d7e74)

* In terms of the proportion of contributions from different types of fine-grained knowledge entity combinations, mixed institutions from academia and industry pay more attention to the novelty of the combination of methodological indicators, and industrial institutions pay more attention to the novelty of the combination of methods and tools.
  
![WPS图片(1)](https://github.com/CZL-ziling/Noveltyscore_metric/assets/156270701/8c90f3ee-9e08-4ed2-8d2c-f77592babce0)

## Dataset Discription

This study encompasses one datasets: ent-text-79-22.txt

`./Dataset/ent-text-79-22.txt`   Due to the need for further research, we have provided partial data, including a sample of 500 from the three major conferences in the NLP field from 79 to 22 years. Each paper in the dataset is presented by a dictionary with three main keys, namely "id", "year", and "sentence". 
The field "id" is used to represent the unique value of th  e paper.   
"year" is the year in which the paper was published. 
The "sentence" contains the full-text content of each paper, which contains our annotation entities, which are of four types: methods, datasets, measures, and tools.  
```
'id': ['P79-1000', 'P79-1001', 'P79-1002', 'P79-1003', 'P79-1004', 'P79-1005', 'P79-1006', 'P79-1007', 'P79-1008', 'P79-1009', 'P79-1010', 'P79-1011', 'P79-1012', 'P79-1013', 'P79-1014', 'P79-1015', 'P79-1016', 'P79-1017', 'P79-1018']

'year': ['1979', '1979', '1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979'，'1979']

'sentence': 'A SNAPSHOT OF <entity_Method>KDS</entity_Method> A KNOWLEDGE DELIVERY SYSTEM SUMMARY <entity_Method>KM</entity_Method> is a computer program which creates multi-paragraph ...'
```
*  Translation of Explanations and Examples for Four Entity Types
  
|    Type  |        Description       | Example|
| -------- | -------------------------|-------------------------|
|  Method  | Algorithms, Models, etc. | SVM, LSTM, BERT, Adam, RNN          |
|  Dataset | Corpora, Lexicons, etc.  | Brown Corpus, Penn Treebank, WordNet|
|  Metric  | Evaluation metrics       | Accuracy, Precision, Recall, BLEU   |
|  Tool    | Programming languages, Software, Open-so urce tools, etc.| Python, GIZA++, TensorFlow, PyTorch|


## Novelty score distribution

The novelty score is between 0 and 1, the closer to 1 is the more novel the paper, and vice versa, the novelty score of most papers is concentrated between 0.1 and 0.2, and only a small number of papers have a novelty score greater than 0.5. This suggests that most of the papers are still of low novelty, reflecting conservative research methods.

![WPS图片(3)](https://github.com/CZL-ziling/Noveltyscore_metric/assets/156270701/e129c306-e6d9-4da8-84a0-cb35ac63abfb)


we analyzed the trend in novelty over time. There was a notable and consistent increase in novelty scores between 1995 and 2000.

![WPS图片(4)](https://github.com/CZL-ziling/Noveltyscore_metric/assets/156270701/6f2c8a91-90b0-43eb-827c-c1f7ee1ada09)

## Directory structure
    novelty_metric                             Root directory
    ├── Code                                             Source code folder
    │    ├── Novelty score calculation.py              Novelty measurement code
    |    ├── Fine-grained novelty score calculation.py  Fine-grained novelty measurement code
    Code for novelty metrics
    ├── Dataset                                        Dataset folder
    │   ├── ent-text-79-22.txt                     Extracted entities of papers
    └── README.md
## Dependency packages
System environment is set up according to the following configuration:
- pytorch 2.0.1  
- transformers 4.28.1  
- pandas 2.0.0  
- pytorch-crf 0.7.2  
- fasttext 0.9.2  
- flashtext 2.7  
- nltk 3.8.1  
- numpy 1.24.1  


## Citation
Please cite the following paper if you use this code and dataset in your work.
    
>Ziling Chen, Chengzhi Zhang\*, Heng Zhang, Yi Zhao, Chen Yang, and Yang Yang. Exploring the Relationship Between Team Institutional Composition and Novelty in Academic Papers Based on Fine-Grained Knowledge Entities. ***The Electronic Library***, 2024.（under review)  [[doi]]()  [[Dataset & Source Code]](https://github.com/CZL-ziling/Noveltyscore_metric) 
