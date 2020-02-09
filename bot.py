from konlpy.tag import Kkma
import numpy as np
import matplotlib.pyplot as plt
from time import time


def summarize(contents, radius, k):
    kkma = Kkma()
    keywords = []
    nouns = np.array([hash(elem) for elem in kkma.nouns(contents)], np.int64)
    size = nouns.size
    points = np.zeros([1000, size], np.int)
    i = 0
    sentences = contents.replace('\n', '').split('.')
    for sentence in sentences:
        hash_words = np.array([hash(elem) for elem in kkma.nouns(sentence)])
        arr = []
        for j in range(size):
            points[i][j] = np.count_nonzero(hash_words == nouns[j])
        # print(points[i])
            
        i += 1
    group = np.random.randn(i)
    for i in range(i):
        arr = []
        count = 0
        for j in range(i):
            if i != j:
                distance = np.sum((points[i] - points[j])**2)**0.5
                if distance <= radius:
                    arr.append(j)
        if len(arr) >= k:
            for elem in arr:
                group[elem] = group[i]
    result = []
    for elem in np.unique(group):
        try:
            # result.append(sentences[tolist.index(elem)])
            result.append(sentences[np.where(group == elem)[0][0]])
        except IndexError:
            pass
    return result
