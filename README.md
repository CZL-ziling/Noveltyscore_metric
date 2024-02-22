# Research on the Relationship between Team Composition and Novelty of Academic Papers: Based on the Perspective of Fine-grained Knowledge Entities

## Overview

**Dataset and source code for paper "Research on the Relationship between Team Composition and Novelty of Academic Papers: Based on the Perspective of Fine-grained Knowledge Entities".**.
In this study, the novelty of three major conference papers in the field of NLP was measured.Our work includes the followig aspects:

* The purpose of this paper is to analyze the relationship between the type of team institution and the novelty of the paper. First, the author's institution is extracted, the name of the institution is collected through GRID, and the institution data is supplemented with Wikipedia and GeoNames data. The types of team institutions are divided into three categories: academia, mixed academia and industry, and industry.
* We use Zhang's model to extract the method entities in the paper. The novelty of the paper is measured based on the fine-grained entities extracted. The novelty is further explained from the proportion of atypical entity combinations. The novelty of the measurement was correlated with the type of institution.

## Main findings

* The novelty of papers in industrial institutions is significantly lower than that in academic institutions and institutions with mixed academia and industry.
* In terms of the proportion of contributions from different types of fine-grained knowledge entity combinations, mixed institutions from academia and industry pay more attention to the novelty of the combination of methodological indicators, and industrial institutions pay more attention to the novelty of the combination of methods and tools.
## Directory structure
    novelty_metric                             Root directory
    ├── Code                                           Source code folder
    │   ├── get_result                            Code for novelty metrics
    ├── Dataset                                        Dataset folder
    │   ├── paper-ents.txt                       Extracted entities of papers
    └── README.md
## Dependency packages
System environment is set up according to the following configuration:

pytorch 2.0.1
transformers 4.28.1
pandas 2.0.0
pytorch-crf 0.7.2
fasttext 0.9.2
flashtext 2.7
nltk 3.8.1
numpy 1.24.1
