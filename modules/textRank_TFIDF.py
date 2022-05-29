import pandas as pd
import numpy as np
import sys
import os
import re
import datetime 
import networkx
import json
from konlpy.tag import Komoran, Kkma, Okt
from kss import split_sentences
import math
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def tokenize(content):
    #split sentence
    if(type(content) == str):
        content = content.split('\n')

    sent_list = [sent for sent in split_sentences(''.join(content)) if sent != None]
    return sent_list


class TextRank:
    def __init__(self):
        self.posTagger = Okt()
        self.graph2 = []
        self.nouns = []
        self.sentences = []
 
    def loadSentence(self, sentenceToken):    
        self.sentences = sentenceToken   
        for sentence in self.sentences:
            if sentence != '':
                self.nouns.append(' '.join([noun for noun in self.posTagger.nouns(str(sentence)) 
                                       if len(noun) > 1]))
    
    def get_rank(self, d=0.85):
        matrix_size = self.graph2.shape[0]
        for id in range(matrix_size):
            self.graph2[id, id] = 0
            link_sum = np.sum(self.graph2[:,id])
            if link_sum != 0:
                self.graph2[:, id] /= link_sum
            self.graph2[:, id] *= -d
            self.graph2[id, id] = 1
        graph_mat = (1-d) * np.ones((matrix_size, 1))
        ranks = np.linalg.solve(self.graph2, graph_mat)
        return {idx: r[0] for idx, r in enumerate(ranks)}
    
    def build(self, sentence):
        tfidf = TfidfVectorizer()
        count = CountVectorizer()
        tfidf_mat = tfidf.fit_transform(sentence).toarray()
        self.graph2 = np.dot(tfidf_mat, tfidf_mat.T)
 

    def summarize(self, ratio):
        summary = []
        index=[]

        idx_rank = self.get_rank()
        sorted_rank_idx = sorted(idx_rank, key=lambda k: idx_rank[k], reverse=True)
        sorted_rank_idx = sorted_rank_idx[:int(len(sorted_rank_idx)*ratio)]
        print(len(sorted_rank_idx))
        for idx in sorted_rank_idx:
            index.append(idx)
        index.sort()
        for idx in index:
            summary.append(self.sentences[idx])
        return ' '.join(summary)


