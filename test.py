#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:10:59 2024

@author: hyw
"""


import pandas as pd



data_articles = pd.read_csv("articles.CDKN2A.csv")

data_authors = pd.read_csv("authors.CDKN2A.csv")

data_counts_q = pd.read_csv("paper_counts.csv")

#print(data_articles)

data_counts_q.plot()