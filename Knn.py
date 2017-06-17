import math

class Knn(object):

    def __init__(self, documents_array, categories, documents_by_category):
        self.documents_array = documents_array
        self.categories = categories
        self.documents_by_category = documents_by_category
        self.frequencies = {}
        self.wordsByDocument = {}
        self.frequenciesInv = {}
        self.weights = {}
        self.weightsByDocument = {}

    # Esta función calcula el número de apariciones que tiene una palabra por cada documento. Cada palabra tiene
    # que tener una columna por cada documento que tengamos.
    # Se usará un diccionario {palabra_clave : [listado con los diferentes valores de las columnas correspondientes]}
    def calculate_frequencies(self):
         for doc in self.documents_array: # Se recorren todos los documentos
            for w in doc.words: # Se recorren todas las palabras de un documento
                if not self.frequencies.has_key(w): # Si esa palabra no está en el diccionario...
                    self.frequencies[w] = [] # ...se añade y se le asigna como valor una lista vacia
                aux = self.frequencies[w]
                aux.append(doc.words.count(w)) # Se añade un nuevo elemento a la lista de frecuencias de esa palabra


    # Esta función  calcula el número de documentos en el que aparece una palabra
    # Tendremos un diccionario (palabra --> número de documentos en los que aparece)
    def calculate_documental_frequencie(self):
        auxWords = [] # Esto es una lista auxiliar para comprobar que en un documento no se cuenten palabras repetidas
        for doc in self.documents_array: # Se recorren todos los documentos
            auxWords.clear()
            for w in doc.words: #Se recorren todas las palabras de un documento
                auxWords.append(w)
                if not self.wordsByDocument.has_key(w): #S i esa palabra no está en el diccionario...
                    self.wordsByDocument[w] = 0 # ...se añade y se le asigna como valor el cero
                if w not in auxWords: # Si la palabra no ha sido ya contada en este documento...
                    self.wordsByDocument[w] = self.wordsByDocument[w] + 1 # ...se cuenta

    # Esta función calcula el logaritmo del numero total de documentos entre la frecuencia documental para
    # cada palabra clave
    def calculate_inverse_documental_frequencie(self):
        N = self.documents_array.count()
        for key in self.wordsByDocument.keys():
            self.frequenciesInv[key] = math.log10(N/self.wordsByDocument[key])

    # Esta función calcula el peso de una palabra clave con respecto a cada documento(el peso tiene la representación
    # en la tabla de W), por lo tanto deberá haber con respecto a cada palabra clave una columna de peso por cada documento
    def calculate_weight(self):
        for freq in self.frequencies.keys():
            for inv in self.frequenciesInv.keys():
                if freq == inv:
                    self.weights[freq] = self.frequencies[freq] * self.frequenciesInv[inv]

    # Esta función calcula los pesos de cada documento
    def calculateWeightByDocument(self):
        for i in range(len(self.weights.keys())): # Creamos un diccionario para contener por cada documento sus pesos
            self.weightsByDocument[i] = []
            for key in self.weights.keys(): # Para cada peso de cada palabra...
                aux = self.weights[key] #...cogemos el peso de esa palabra para dicho documento...
                self.weightsByDocument[i].append(aux[i]) # ...y lo añadimos a los pesos de ese documento

    # Esta función calcula la proximidad entre dos vectores
    def proximidad(self, w1, w2):
        result = 0
        for i in range(len(w1)):
            result = (w1[i]*w2[i]) / (math.sqrt(w1[i]*w1[i]) * math.sqrt(w2[i]*w2[i]))

    def kNN(self, doc, k):
        prox = {}
        for i in range(len(self.weightsByDocument.keys())):
            w1 = self.weightsByDocument[i]
            prox[w1] = []
            for j in range(len(self.weightsByDocument.keys())):
                if i is not j:
                    w2 = self.weightsByDocument[j]
                    pesoAux = self.proximidad(w1, w2)
                    aux = prox[w1]
                    aux.append(pesoAux)
                    pesoAux = 0



    def start_algorithm(self):
        self.calculate_frequencie()
        self.calculate_documental_frequencie()
        self.calculate_inverse_documental_frequencie()
        self.calculate_weight()
        self.calculateWeightByDocument()