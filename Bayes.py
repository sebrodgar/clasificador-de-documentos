import csv, operator
from KeyWord import KeyWord
import os


class Bayes(object):

    def __init__(self, documents_array, categories, documents_by_category, option):
        self.documents_array = documents_array
        self.categories = categories
        self.documents_by_category = documents_by_category
        self.source_csv = option
        self.pcs = {}
        self.total_appearances = 0
        self.categories_keys = []
        self.number_of_keywords = 0
        self.keywords_csv = []

    # Calculamos proporción de los documentos de todas las categorias con respecto al total de documentos de los que
    # disponemos
    def calculate_pc(self):
        for c in self.documents_by_category:
            self.pcs[c] = len(self.documents_by_category[c])/len(self.documents_array)


    # Se calcula las apariciones de las palabras entre todos los documentos de cada categoria
    def calculate_appearances(self):
        for c in self.categories: # Se recorren el diccionario de categorias
            category = Category(c)
            for word in self.categories[c]: # Se accede al listado de palabras claves de cada catogoría para calcular el numero de apariciones de las palabras.
                appearances = 0
                for doc in self.documents_by_category[c]: # Se recorren todos los documentos de la categoria en busca de las palabras claves.
                    appearances += doc.words.count(word)

                w = KeyWord(c, word, self.pcs[c], appearances)   # Se añade la palabra clave al listado de palabras claves para luego realizar los calculos de probabilidades.
                category.keywords.append(w)

                self.number_of_keywords += 1
                self.total_appearances += appearances
                self.keywords_csv.append(w)

            category.pc = self.pcs[c]
            self.categories_keys.append(category)


    def calculate_ptc(self):
        for keyword in self.keywords_csv:
            keyword.ptc = ((keyword.appearances + 1) / ((self.total_appearances - keyword.appearances)
                                                        + self.number_of_keywords))
        for cat in self.categories_keys:
            for keyword in cat.keywords:
                keyword.ptc = ((keyword.appearances + 1) / ((self.total_appearances - keyword.appearances)
                                                            + self.number_of_keywords))

    def start_algorithm(self):
        self.calculate_pc()
        self.calculate_appearances()
        self.calculate_ptc()

        self.save_information_csv()
        #for c in self.categories_keys:
        #    print(c)

    def save_information_csv(self):
        filename = self.source_csv + './datos/datos_bayes.csv'
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        archivo = open(filename, 'w')
        # archivo.write('Partido;CPPG(Local);CPPG(Visitante);CPP vs(Local);CPP vs(Visitante);CPPHome(Local);CPPAway(Local);CPPHome(Visitante);CPPAway(Visitante);Estimacion' + '\n')
        archivo.write('Categoria;Palabra;Pc;Ptc;Apariciones' + '\n')
        for w in self.keywords_csv:
            archivo.write(str(w))


class Category(object):

    def __init__(self, name):
        self.name = name
        self.pc = -1
        self.keywords = [] # Listado de objetos Keyword


    def __str__(self):
        word = ""
        for k in self.keywords:
            word += str(k)
        #res = self.name + ";" + str(self.pc) + ";" + str(self.keywords) + "\n"
        res = self.name + ";" + str(self.pc) + ";" + word + "\n"

        return res

    def __eq__(self, other):
        res = False
        if self.name == other.name:
            res = True

        return res
