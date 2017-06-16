import csv, operator
from KeyWord import KeyWord
import os


class Bayes(object):

    def __init__(self, documents_array, categories, documents_by_category, option):
        self.documents_array = documents_array  # Array con todos los documentos que se tengan almacenados
        self.categories = categories            # Diccionario con las categorias y sus palabras claves
        self.documents_by_category = documents_by_category  # Diccionario con los documentos repartidos por categorias
        self.source_csv = option    # Variable que indica la ruta de guardado del archivo csv
        self.pcs = {}               # Diccionario con todos las probabilidades de las categorias
        self.keywords = []          # Array con todas las palabras claves del sistema
        # Array del objeto KeyWord con las palabras claves guardadas y sus parámetros asociados
        self.keywords_calculated_appearances = []
        self.keywords_category = {} # Diccionario con los objetos KeyWord clasificados por categorias



    # Calculamos proporción de los documentos de todas las categorias con respecto al total de documentos de los que
    # disponemos
    def calculate_pc(self):
        for c in self.documents_by_category:
            self.pcs[c] = len(self.documents_by_category[c])/len(self.documents_array)

    # Se calcula las apariciones de una palabra y categoria dada entre todos los documentos de esa categoria
    def calculate_appearances_doc_in_category(self, category, word):
        appearances = 0
        for doc in self.documents_array:
            if doc.category == category:
                appearances += doc.words.count(word)
        return appearances


    # Se obtienen las palabras claves de todas las categorias para almacenarlas en un listado
    def get_keywords_category(self):
        for c in self.categories:
            self.keywords += self.categories[c]

    # Calcula las veces que aparece una palabra clave en los documentos de las diferentes categorias y lo guarda en la
    # variable keywords_category(se guarda para tener dividido las palabras que pertenece a cada categoria, esto nos
    # ayuda en el calculo del ptc) y en la variable keywords_calculated_appearances (se guarda para luego recorrerla y
    # añadirle los ptc, además que ayuda a seguir el formato para guardarlo en el csv)
    def calculate_appearances(self):
        for k in self.keywords:
            for c in self.categories:
                appearance = self.calculate_appearances_doc_in_category(c, k)
                keyword = KeyWord(c, k, self.pcs[c], appearance)
                self.keywords_calculated_appearances.append(keyword)
                if c in self.keywords_category:
                    self.keywords_category[c].append(keyword)
                else:
                    self.keywords_category[c] = [keyword]

    # Se encarga de calcular la probabilidad de una palabra condicionada a una categoria incluyendole el suavizado de
    # Laplace para que no nos de probabilidades que sean 0
    def calculate_ptc(self):
        numero_total_palabras = len(self.keywords)
        for key in self.keywords_calculated_appearances:
            appearances_cat = 0
            for key_category in self.keywords_category[key.category]:# Recorremos las palabras claves de una categoria
                # Añadimos en la variable appearances_cat todas las apariciones de las palabras de una categoria
                appearances_cat += key_category.appearances
            # Se aplica la formula de la probabilidad condicionada
            key.ptc = (key.appearances + 1) / (appearances_cat + numero_total_palabras)


    # Con este método iniciamos el algoritmo para que realice todos los cálculos y genere el documento csv donde se
    # se le haya indicado
    def start_algorithm(self):
        self.get_keywords_category()
        self.calculate_pc()
        self.calculate_appearances()
        self.calculate_ptc()

        self.save_information_csv()

    # Genera el archivo CSV a partir del listado de keywords con sus calculos realizados
    def save_information_csv(self):
        filename = self.source_csv + './datos/datos_bayes.csv'
        if not os.path.exists(os.path.dirname(filename)): # Comprobamos que el directorio existe, sino pues lo creamos
            os.makedirs(os.path.dirname(filename))
        archivo = open(filename, 'w')

        # Empezamos escribiendo en el fichero la primera linea que será la de los titulos y luego se va recorriendo
        # y guardando los objetos KeyWords tal y como indica su metodo "str".
        archivo.write('Categoria;Palabra;Pc;Ptc;Apariciones' + '\n')
        for w in self.keywords_calculated_appearances:
            archivo.write(str(w))
