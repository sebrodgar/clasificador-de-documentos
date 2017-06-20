import csv
import math
from contextlib import redirect_stderr
import operator

from DocumentoKnn import DocumentoKnn
from KeywordKnn import KeywordKnn
from Knn import Knn
import AuxiliaryMethods

class ClasificationKnn(object):

    def __init__(self, document, documents_array, categories, source_csv, k):
        self.document = document
        self.documents_array = documents_array
        self.categories = categories
        self.source_csv = source_csv
        self.k = k
        self.keywords = []
        self.frequencyWords = {}
        self.documentsKnn = []
        self.neighbours = {}
        self.KNeighbours = {}

    def stringToArray(self, string):
        res = []
        aux = string.split('-')
        for i in range(len(aux)):
            res.append(float(aux[i]))
        return res

    def get_keywords_category(self):
        for c in self.categories:
            for s in self.categories[c]:
                keywordKnn = KeywordKnn(s, "", c, 0, 0)
                self.keywords.append(keywordKnn)

    def get_data_csv(self):
        with open(self.source_csv) as csvdata:
            input = csv.reader(csvdata)
            indice = 0
            for reg in input:
                datas = reg[0].split(';')
                if indice > 0:
                    s = self.stringToArray(datas[2])
                    self.documentsKnn.append(DocumentoKnn(datas[0], datas[1], s))
                indice += 1

    def calculate_frequencies(self):
        for w in self.keywords: # Se recorren todas las palabras clave
            if w not in self.frequencyWords:
                self.frequencyWords[w] = 0.0
            self.frequencyWords[w] += self.document.words.count(w.word)

    def getNeighbours(self, documentsKnn, k):
        ks = []
        aux = []
        values = []
        for key in self.frequencyWords.keys():
            aux.append(float(self.frequencyWords[key]))
        for d in documentsKnn:
            prox = float(AuxiliaryMethods.proximidad(d.weights, aux))
            saux = d.serie + ", " + d.category
            self.neighbours[saux] = prox
        for neig in self.neighbours:
            values.append(self.neighbours[neig])
            values = sorted(values, reverse = True)
        for i in range(1,k+1):
            ks.append(values[i-1])
        for n in self.neighbours:
            for r in range(len(ks)):
                if self.neighbours[n] == ks[r]:
                    self.KNeighbours[ks[r]] = n
        self.KNeighbours = sorted(self.KNeighbours.items(), key=operator.itemgetter(0), reverse=True)

    def start(self):
        self.get_data_csv()
        self.get_keywords_category()
        self.calculate_frequencies()
        self.getNeighbours(self.documentsKnn, 4)
        print(self.KNeighbours)