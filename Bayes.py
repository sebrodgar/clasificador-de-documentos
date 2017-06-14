class Bayes(object):

    def __init__(self, documents_array, categories, documents_by_category):
        self.documents_array = documents_array
        self.categories = categories
        self.documents_by_category = documents_by_category
        self.pcs = {}
        self.keywords = []

    # Calculamos proporción de los documentos de todas las categorias con respecto al total de documentos de los que
    # disponemos
    def calculate_pc(self):
        for c in self.documents_by_category:
            self.pcs[c] = len(self.documents_by_category[c])/len(self.documents_array)


    # Se calcula las apariciones de las palabras entre todos los documentos de cada categoria
    def calculate_appearances(self):
        for c in self.categories: # Se recorren el diccionario de categorias
            for word in self.categories[c]: # Se accede al listado de palabras claves de cada catogoría para calcular el numero de apariciones de las palabras.
                appearances = 0
                for doc in self.documents_by_category[c]: # Se recorren todos los documentos de la categoria en busca de las palabras claves.
                    appearances += doc.words.count(word)

                w = KeyWord(word, c, appearances)   # Se añade la palabra clave al listado de palabras claves para luego realizar los calculos de probabilidades.

                self.keywords.append(w)


    def calculate_ptc(self):
        sum_all = 0
        keys = []
        for key in self.keywords:   # Se realiza la suma de todas las apariciones de las palabras claves en los documentos
            sum_all += key.appearances

        for keyword in self.keywords:   # Se realizra el calculo de la probabilidad P(t|c)
            keyword.ptc = ((keyword.appearances + 1) / ((sum_all-keyword.appearances) + len(self.keywords)))
            keys.append(keyword)

        self.keywords = keys

    def start_algorithm(self):
        self.calculate_pc()
        self.calculate_appearances()
        self.calculate_ptc()

        for k in self.keywords:
            print(k)
        print(self.pcs)

    def save_information_csv(self):
        print("p")


class KeyWord(object):
    def __init__(self, word, category, appearances):
        self.word = word
        self.category = category
        self.appearances = appearances
        self.ptc = -1.0

    def __str__(self):
        res = self.word + ";" + self.category + ";" + str(self.appearances) + ";" + str(self.ptc) + "\n"

        return res
