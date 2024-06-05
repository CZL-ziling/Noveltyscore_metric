# Exploring the Relationship Between Team Institutional Composition and Novelty in Academic Papers Based on Fine-Grained Knowledge Entities
## Overview

**Dataset and source code for paper "Exploring the Relationship Between Team Institutional Composition and Novelty in Academic Papers Based on Fine-Grained Knowledge Entities"**.

In this study, the novelty of three major conference papers in the field of NLP was measured.Our work includes the followig aspects:

* The purpose of this paper is to analyze the relationship between the type of team institution and the novelty of the paper. First, the author's institution is extracted, the name of the institution is collected through [GRID](https://grid.ac/), and the institution data is supplemented with Wikipedia and [GeoNames data](https://www.geonames.org/). The types of team institutions are divided into three categories: academia, mixed academia and industry, and industry.
* We use [Zhang's model](https://github.com/ZH-heng/technology_development) to extract the method entities in the paper. The novelty of the paper is measured based on the fine-grained entities extracted. The novelty is further explained from the proportion of atypical entity combinations. The novelty of the measurement was correlated with the type of institution.

## Main findings

* significant differences in the novelty of academic papers are observed among different types of team institutional compositions. It is found that academic institutions and mixed academic and industrial institutions produce papers with higher novelty compared to papers from industrial institutions.
  

<div align=center>
  <img width=50% height=50%  src="https://github.com/CZL-ziling/Noveltyscore_metric/blob/master/img/Novelty%20of%20papers%20of%20different%20institution%20types.png"/>
</div>
<div align=center>
 Fig. 1.Novelty of papers of different institution types
</div>

* In terms of the proportion of contributions from different types of fine-grained knowledge entity combinations, mixed institutions from academia and industry pay more attention to the novelty of the combination of methodological indicators, and industrial institutions pay more attention to the novelty of the combination of methods and tools.
  

<div align=center>
  <img  width=80% height=80%  src="https://github.com/CZL-ziling/Noveltyscore_metric/blob/master/img/The%20contribution%20of%20fine-grained%20entity%20combinations%20of%20different%20institutional%20types%20to%20novelty.png"/>
</div>
<div align=center>
 Fig. 2. The contribution of fine-grained entity combinations of different institutional types to novelty
</div>

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

## Method

Firstly, author teams are categorized into three types: academic institutions, industrial institutions, and mixed academic and industrial institutions. Next, the authors extract four types of entities from the full paper: methods, data sets, tools and metric. The novelty of papers is evaluated using entity combination measurement methods. Additionally, pairwise combinations of different types of fine-grained entities are analyzed to assess their contributions to novel papers.
<div align=center>
  <img  width=80% height=80%  src="https://github.com/CZL-ziling/Noveltyscore_metric/blob/master/img/Fine-Grained%20Novelty%20Bias%20Result%20Analysis%20Example%20Diagram.png"/>
</div>
<div align=center>
 Fig. 3. The contribution of fine-grained entity combinations of different institutional types to novelty
</div>

## Quick start
* `./Code/Novelty score calculation.py`In this step, the combination of novel entities is determined by the distance of the cosine distance between the entities, and the proportion of the combination of novel entities in the full text of the paper is taken as the novelty score.Follow the notes step by step to get a novelty score for each paper.
* `./Code/Fine-grained novelty score calculation.py`Through this step, the degree of contribution of different types of entity combinations to the novelty of the novel paper can be further obtained on the basis of the novelty score obtained in the previous step.Enter the relevant files generated in the previous step, and run against the annotations to get fine-grained novelty scores for different entity types.

## Novelty score distribution

* The novelty score is between 0 and 1, the closer to 1 is the more novel the paper, and vice versa, the novelty score of most papers is concentrated between 0.1 and 0.2, and only a small number of papers have a novelty score greater than 0.5. This suggests that most of the papers are still of low novelty, reflecting conservative research methods.

<div align=center>
  <img width=80% height=80%  src="https://github.com/CZL-ziling/Noveltyscore_metric/blob/master/img/The%20distribution%20of%20ACL%20paper%E2%80%99s%20novelty%20scores.png"/>
</div>
<div align=center>
 Fig. 4.The distribution of ACL paper’s novelty scores
</div>


* we analyzed the trend in novelty over time. There was a notable and consistent increase in novelty scores between 1995 and 2000.
<div align=center>
  <img width="800" height="400" src="https://github.com/CZL-ziling/Noveltyscore_metric/blob/master/img/Trends%20in%20novelty%20scores%20of%20academic%20papers%20over%20time.png"/>
</div>
<div align=center>
 Fig. 5. Trends in novelty scores of academic papers over time
</div>

* Consistent with the distribution of the number of entities, the combination of entities participating in method entities is relatively high. Among them, the combination of method and indicator entities contributed the highest, followed by the combination of methods and method entities, and the combination of methods and data entities. In addition to methodological combinations, combinations related to indicator entities contribute less to novelty in novel papers.
<div align=center>
  <img width="900" height="500" src="https://github.com/CZL-ziling/Noveltyscore_metric/blob/master/img/Fine-grained%20novelty%20biases%20the%20score%20distribution.png"/>
</div>
<div align=center>
 Fig. 6.  Fine-grained novelty biases the score distribution
</div>

## Directory structure
    novelty_metric                                        Root directory
    ├── Code                                              Source code folder
    │    ├── Novelty score calculation.py                 Novelty measurement code
    |    ├── Fine-grained novelty score calculation.py    Fine-grained novelty measurement code
    Code for novelty metrics
    ├── Dataset                                           Dataset folder
    │   ├── ent-text-79-22.txt                            Extracted entities of papers
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
