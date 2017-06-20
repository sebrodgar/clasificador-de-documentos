import csv
import math
from contextlib import redirect_stderr

from DocumentKnn import DocumentKnn
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
        self.frequencyWords = {} # Diccionario de las palabras del documento a clasificar con sus frecuencias
        self.documentsKnn = []
        self.neighbours = {} # Diccionario de todos los vecinos
        self.KNeighbours = {} # Diccionario de los k vecinos más próximos

    # Esta función convierte el string de pesos en un array con dichos pesos
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
                    self.documentsKnn.append(DocumentKnn(datas[0], datas[1], s))
                indice += 1

    def calculate_frequencies(self):
        for w in self.keywords: # Se recorren todas las palabras clave
            if w not in self.frequencyWords:
                self.frequencyWords[w] = 0.0
            #print(float(self.document.words.count(w.word)))
            self.frequencyWords[w] += float(self.document.words.count(w.word))

    def getNeighbours(self, documentsKnn, k):
        aux = [] # Array para la frecuencia de las palabras del documento a clasificar
        values = [] # Array de proximidades
        ks = []  # Array de proximidades de los k vecinos más próximos
        for key in self.frequencyWords.keys(): # Recorremos las palabras que aparecen en el documento a clasificar
            aux.append(float(self.frequencyWords[key])) # y añadimos sus frecuencias al array

        for d in documentsKnn: # Recorremos los documentos
            prox = float(AuxiliaryMethods.proximidad(d.weights, aux)) # Calculamos la proximidad del documento a clasificar con cada documento
            saux = d.serie + ", " + d.category # Esta será la clave del diccionario de vecinos (Nombre de la seria, categoría)
            self.neighbours[saux] = prox # Añadimos la proximidad
        for neig in self.neighbours: # Para cada vecino
            values.append(self.neighbours[neig]) # Cogemos sus proximidades...
            values = sorted(values, reverse=True) # ...y las ordenamos de mayor a menor
        for i in range(1, k+1): # for desde 1 hasta k
            ks.append(values[i-1]) # Metemos la proximidad
        for n in self.neighbours: # Este for es para obtener las series de...
            for r in range(len(ks)): # ...las proximidades
                if self.neighbours[n] == ks[r]:
                    if n not in self.KNeighbours:
                        self.KNeighbours[n] = 0.0
                    self.KNeighbours[n] = ks[r] # Añadimos las k series más próximas

    def calculate_category(self):
        # En este diccionario es para establecer el numero de veces que aparece cada categoría
        # entre los vecinos para quedarse con la categoria mayoritaria entre los vecinos
        categories_dicc = {}
        category_selected = ""
        category_selected_kneighbour_number = -1
        for kn in self.KNeighbours:
            category = kn.split(",")[1]
            if category in categories_dicc:
                categories_dicc[category] += 1
            else:
                categories_dicc[category] = 1

        for cat in categories_dicc:
            if category_selected == "":
                category_selected = cat
                category_selected_kneighbour_number = categories_dicc[cat]
            elif categories_dicc[cat] > category_selected_kneighbour_number:
                category_selected_kneighbour_number = categories_dicc[cat]
                category_selected = cat

        print("La serie " + self.document.name.upper() +" pertenece a la categoría " + category_selected.upper())

    def start(self):
        self.get_data_csv()
        self.get_keywords_category()
        self.calculate_frequencies()
        self.getNeighbours(self.documentsKnn, 4)
        self.calculate_category()

class CategoryKnn(object):

    def __init__(self, serie, category, weight):
        self.serie = serie
        self.category = category
        self.weight = weight