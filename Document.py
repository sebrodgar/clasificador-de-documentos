class Document(object):

    def __init__(self, name, text, category):
        self.name = name
        self.text = text
        self.words = []
        # Aquí registramos las frecuencias que calculamos con el algoritmo Knn
        self.frequencies = {}
        # Categoría que se le asigna despues de realizar el analisis pertinente
        self.category = category

    def __str__(self):
        res = "Documento: " + self.name + " Palabras: " + str(self.words)
        return res
