import csv
import math
from KeyWord import KeyWord

class ClasificationBayes(object):

    def __init__(self, document, source_csv):
        self.document = document
        self.source_csv = source_csv
        self.keywords = []
        self.keywords_found = []


    def get_data_csv(self):
        #print(self.source_csv)
        with open(self.source_csv) as csvdata:
            input = csv.reader(csvdata)
            indice = 0
            for reg in input:
                datas = reg[0].split(';')
                if indice > 0:
                    self.keywords.append(KeyWord(datas[0], datas[1], float(datas[2]), int(datas[4]), float(datas[3])))
                indice += 1

    def select_words_in_docuement(self):
        for w in self.keywords:
            if self.document.words.count(w.word) > 0:
                w.appearances = self.document.words.count(w.word)
                self.keywords_found.append(w)


    def divide_keywords_in_category(self):
        categories_keywords = {} # Sigue el patron {Categoria:[keywords]}
        for w in self.keywords_found:
            if w.category not in categories_keywords:
                categories_keywords[w.category] = [w]
            else:
                categories_keywords[w.category].append(w)
        self.calculate_probabilities(categories_keywords)

    def calculate_probabilities(self, categories_keywords):
        category = ""
        category_value = -1

        for c in categories_keywords.keys():
            c_value = 1
            pc = -1
            for w in categories_keywords[c]:
                #print(w.ptc)
                c_value *= math.pow(w.ptc, w.appearances)
                #print(math.pow(w.ptc, w.appearances))
                #print(w.ptc)
                #print(w.appearances)
                pc = w.pc

            c_value *= pc
            #print(c_value)
            if c_value > category_value:
                category = c
                category_value = c_value

        print("La categoria del documento " + self.document.name.upper() + " es: " + category.upper() + " con una probabilidad de: "
              + str(category_value))


    def start(self):
        self.get_data_csv()
        self.select_words_in_docuement()
        self.divide_keywords_in_category()
