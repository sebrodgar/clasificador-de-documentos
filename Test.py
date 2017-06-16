#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from Document import Document
from Bayes import Bayes
from ClassificationBayes import ClassificationBayes
from Bayes import Bayes


categories = {"Comedia": ["cómico", "cómica", "cómicos", "cómicas", "risa", "risas", "comedia", "comedias", "humor", "peculiar"
                          , "surrealista", "surrealistas", "extravagante", "extravagantes", "chiste", "chistes", "gracioso", "graciosa",
                          "graciosos", "graciosas", "divertido", "divertida"],
              "Misterio": ["intriga", "intrigas", "misterio", "misterioso", "misteriosa", "misteriosos", "misteriosas", "asesinato",
                           "asesinatos", "cadáver", "muerte", "muerto", "muerta", "muere", "muerte", "malvado", "malvada", "malvados", "malvadas",
                           "desaparición", "crimen", "crímenes", "caso", "casos", "detective", "sospechoso", "investigación", "investigaciones","suspense"],
              "Infantil": ["niño", "niña", "niños", "niñas", "infantil", "infantiles", "divertido", "divertida", "aventura", "aventuras",
                           "dibujo", "dibujos", "animado", "animada", "animados", "animadas", "animación", "infancia", "gracioso", "graciosa",
                           "graciosos", "graciosas","héroe"]}
documents = []
documents_by_category = {} # Se usa para no tener que ir calculando cada vez todas los documentos de una categoria

# Se realiza una comprobación de las palabras para luego poder excluir las palabras que no nos aportan nada para la
# clasificación
def check_words_util(word):
    words = ["como", "los", "que","qué", "esta", "está", "del", "este", "esté", "hace", "quién", "pero", "alguien", "para"]
    res = True
    if words.count(word) > 0:
        res = False
    return res

# Se obtiene los array de palabras de los textos de los documentos para facilitar luego los cálculos para la clasificación
def get_words_text(text):
    filter_words = []
    #for line in text_array:
    text_line_formatted = text.replace(",", "").replace("'", "").replace(".", " ")\
        .replace("(", "").replace(")", "").lower() # Lo pasamos también a minúsculas para no tener que realizar una mayor comprobación
    words = text_line_formatted.split(" ")
    for w in words:
        w_strip = w.strip() # Con esto lo que hacemos es eliminar los espacios en blanco que tenga tanto por delante como por detrás
        if len(w_strip) > 3:
            if check_words_util(w_strip):
                filter_words.append(w_strip)
    return filter_words
    #print(filter_words)

# Se obtiene el listado de documentos con los textos obtenidos y los arrays de palabras sacados del texto para su
# comprobación mediante los algoritmos de Knn y Bayes
def get_documents_words():
    for category_dir in listdir("Series"):
        for file_name in listdir("Series/" + category_dir):

            # En primer lugar debemos de abrir el fichero que vamos a leer.
            # Usa 'rb' en vez de 'r' si se trata de un fichero binario.
            infile = open("Series/" + category_dir + "/" + file_name, 'r')

            text = ""
            # Realizamos el for porque el metodo readLines nos da una lista por cada párrafo y necesitamos juntarlo
            for line in infile.readlines():
                text += " " + line

            doc = Document(file_name.split(".")[0], text, category_dir)

            doc.words = get_words_text(doc.text)

            documents.append(doc)

            # Con esta parte lo que estamos haciendo es añadir en un diccionario los documentos por categorias,
            # con esto nos ahorramos el tener que realizar ese filtrado en los algoritmos.
            try:
                lis = documents_by_category[doc.category]
                lis.append(doc)
                documents_by_category[doc.category] = lis
            except:
                documents_by_category[doc.category] = [doc]

            infile.close()

#Creamos y descargamos los partidos de la jornada
print("Comienza el programa de obtención de datos.\n"
      "Elija opción para la ruta donde guardar los documentos: R (raiz del proyecto) o escriba ruta")
option = input()

print("Comienza el programa de obtención de documentos")
get_documents_words()
#get_documents_by_category()

'''for i in documents:
    print(i)
'''
#print(documents_by_category)

#bayes = Bayes(documents, categories, documents_by_category,option)
if option == "R" or option == "r":
    bayes = Bayes(documents, categories, documents_by_category, "")
else:
    bayes = Bayes(documents, categories, documents_by_category, option)


bayes.start_algorithm()
print("Programa Terminado")
'''print("Comienza el programa de clasifiación de datos.\n"
      "Elija opción para la ruta donde obtener los documentos: R (raiz del proyecto) o escriba ruta")
option = input()
if option == "R":
    bayesC = ClassificationBayes(documents[0], "/datos/datos_bayes.csv")
else:
    bayesC = ClassificationBayes(documents[0], option)



#bayes.start_algorithm()

print("Programa Terminado")
#print(documents)'''