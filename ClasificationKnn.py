import csv
import math
from DocumentoKnn import DocumentoKnn

class ClasificationKnn(object):

    '''def __init__(self, document, source_csv):
        self.document = document
        self.source_csv = source_csv
        self.documentsKnn = []'''

    def __init__(self, source_csv):
        self.source_csv = source_csv
        self.documentsKnn = []

    def stringToArray(self, string):
        res = []
        aux = string.split('-')
        for i in range(len(aux)):
            res.append(float(aux[i]))
        return res


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


    def start(self):
        self.get_data_csv()
        for d in self.documentsKnn:
            print(d)