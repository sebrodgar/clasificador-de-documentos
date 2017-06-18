import math
from KeywordKnn import KeywordKnn
import os

class Knn(object):

    def __init__(self, documents_array, categories, documents_by_category):
        self.documents_array = documents_array
        self.categories = categories
        self.documents_by_category = documents_by_category
        self.keywords = []  # Array con todas las palabras claves del sistema
        self.keywordsKnn = [] # Lista de keywordsKnn
        self.wordsByDocument = {} # Diccionario para el número de documentos en los que aparece una palabra
        self.frequenciesInv = {} # Diccionario para las frecuencias inversas
        self.weightsByDocument = {}

    # Se obtienen las palabras claves de todas las categorias para almacenarlas en un listado
    def get_keywords_category(self):
        for c in self.categories:
            self.keywords += self.categories[c]

    # Esta función calcula el número de apariciones que tiene una palabra por cada documento. Cada palabra tiene
    # que tener una columna por cada documento que tengamos.
    # Se usará un diccionario {palabra_clave : [listado con los diferentes valores de las columnas correspondientes]}
    def calculate_frequencies(self):
         for doc in self.documents_array: # Se recorren todos los documentos
            for w in self.keywords: # Se recorren todas las palabras clave
                keywordKnn = KeywordKnn(w, doc.name, doc.words.count(w), 0) # Creamos un keywordKnn y le añadimos su frecuencia
                self.keywordsKnn.append(keywordKnn) # Lo añadimos a una lista de keywordsKnn

    # Esta función  calcula el número de documentos en el que aparece una palabra
    # Tendremos un diccionario (palabra --> número de documentos en los que aparece)
    def calculate_documental_frequencie(self):
        for doc in self.documents_array: # Se recorren todos los documentos
            for w in self.keywords: # Se recorren todas las palabras clave
                if w not in self.wordsByDocument: # Si esa palabra no está en el diccionario...
                    self.wordsByDocument[w] = 0 # ...se añade y se le asigna como valor el cero
                self.wordsByDocument[w] = self.wordsByDocument[w] + doc.words.count(w) # Se le suma el número de veces que aparece en el documento


    # Esta función calcula el logaritmo del número total de documentos entre la frecuencia documental para
    # cada palabra clave
    def calculate_inverse_documental_frequencie(self):
        N = len(self.documents_array) # Número de documentos que hay
        for key in self.wordsByDocument.keys(): # Para cada número de documentos en los que aparece una palabra
            if self.wordsByDocument[key] == 0:
                self.frequenciesInv[key] = 0 # Si es cero, añadimos un cero al diccionario de frecuencias inverssas
            else: # Si no, hacemos el cálculo de la misma
                self.frequenciesInv[key] = math.log10(N/self.wordsByDocument[key])

    # Esta función calcula el peso de una palabra clave con respecto a cada documento
    def calculate_weight(self):
        for kw in self.keywordsKnn: # Recorremos las keywordsKnn
            for inv in self.frequenciesInv.keys(): # Recorremos las claves del diccionario de frecuencias inversas, que son las palabras
                if kw.word == inv: # Si ambas claves son iguales, hacemos el siguiente cálculo
                    kw.weight = kw.frequency * self.frequenciesInv[inv] # Multiplicamos cada frecuencia por la frecuencia inversa

    # Esta función calcula los pesos de cada documento
    def calculateWeightByDocument(self):
        serieAux = ""
        keysAux = self.keywordsKnn
        for kw in self.keywordsKnn:
            serieAux = kw.serie
            if kw.serie not in self.weightsByDocument:
                self.weightsByDocument[kw.serie] = []
            if kw.serie is serieAux:
                aux = self.weightsByDocument[kw.serie].append(kw.weight)
            keysAux.remove(kw)

    # Esta función calcula la proximidad entre dos vectores
    def proximidad(self, w1, w2):
        numerador, result = 0
        for i in range(len(w1)):
            numerador += w1[i]*w2[i]
        for i in range(len(w1)):
            denominador1 = math.sqrt(w1[i]*w1[i])
        for i in range(len(w2)):
            denominador2 = math.sqrt(w2[i]*w2[i])
        result = (numerador) / (denominador1 * denominador2)
        return result

    # Genera el archivo CSV de las series con sus pesos
    def save_information_csv(self):
        filename = self.source_csv + './datos/datos_knn.csv'
        if not os.path.exists(os.path.dirname(filename)):  # Comprobamos que el directorio existe, sino pues lo creamos
            os.makedirs(os.path.dirname(filename))
        archivo = open(filename, 'w')

        # Empezamos escribiendo en el fichero la primera linea que será la de los titulos y luego se va recorriendo
        # y guardando los objetos KeyWordsKnn tal y como indica su metodo "str".
        archivo.write('Peso' + '\n')
        for w in self.weightsByDocument:
            archivo.write(str(w))


    def start_algorithm(self):
        self.get_keywords_category()
        self.calculate_frequencies()
        self.calculate_documental_frequencie()
        self.calculate_inverse_documental_frequencie()
        self.calculate_weight()
        self.calculateWeightByDocument()
        print(self.weightsByDocument)
