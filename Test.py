#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from Document import Document
categories = {"Comedia": ["humor", "risa", "risas", "cómico", "cómicos", "cómica", "cómicas"], "Misterio": []}
documents = []

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

            doc = Document(file_name.split(".")[0], text)

            doc.words = get_words_text(doc.text)

            documents.append(doc)
            infile.close()

print("Comienza el programa de obtención de documentos")
get_documents_words()

for i in documents:
    print(i)

print("Programa Terminado")
#print(documents)