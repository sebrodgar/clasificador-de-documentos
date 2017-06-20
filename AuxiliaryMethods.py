#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Document import Document
import os as os
import csv
from KeyWord import KeyWord
import math

categories = {"Comedia": ["cómico", "cómica", "cómicos", "cómicas", "risa", "risas", "comedia", "comedias", "humor", "peculiar", "peculiares",
                          "surrealista", "surrealistas", "extravagante", "extravagantes", "chiste", "chistes", "gracioso", "graciosa",
                          "graciosos", "graciosas", "divertido", "divertida"],
              "Misterio": ["intriga", "intrigas", "misterio", "misterioso", "misteriosa", "misteriosos", "misteriosas", "asesinato",
                           "asesinatos", "asesino", "cadáver", "muerte", "muertes", "muerto", "muerta", "muere", "matar", "malvado", "malvada", "malvados",
                           "malvadas", "desaparición", "crimen", "crímenes", "caso", "casos", "detective", "sospechoso", "investigación", "investigaciones","suspense"],
              "Infantil": ["niño", "niña", "niños", "niñas", "infantil", "infantiles", "divertido", "divertida", "aventura", "aventuras",
                           "dibujo", "dibujos", "animado", "animada", "animados", "animadas", "animación", "infancia", "gracioso", "graciosa",
                           "graciosos", "graciosas","héroe"],
              "Romantica": ["amor", "amoroso", "amorosa", "amorosos", "amorosas", "desamor", "beso", "besos", "besar", "boda", "enamorado",
                            "enamorada", "enamorados", "enamoradas", "romántico", "romántica", "romance", "relación", "pareja", "novio",
                            "novia", "gay", "apasionante", "pasión"],
              "CienciaFiccion": ["ciencia", "ficción", "ficciones", "fantasía", "fantástico", "fantástica", "fantásticos", "fantásticos",
                                  "increíble", "increíbles", "fenómeno", "fenómenos", "poder", "poderes", "sobrenatural", "sobrenaturales",
                                  "extraño", "extraña", "extraños", "extrañas", "irreal", "irreales", "extraterrestre", "extraterrestres",
                                  "sorprendente", "sorprendentes", "ciencia", "científico", "científica", "científicos", "científicas"]}
#documents = []
#documents_by_category = {} # Se usa para no tener que ir calculando cada vez todas los documentos de una categoria

# Se realiza una comprobación de las palabras para luego poder excluir las palabras que no nos aportan nada para la
# clasificación
def check_words_util(word):
    words = ["como", "los", "que", "qué", "esta", "está", "del", "este", "esté", "hace", "quién", "pero", "alguien", "para"]
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
def get_documents_words(documents, documents_by_category):
    for category_dir in os.listdir("Series"):
        for file_name in os.listdir("Series/" + category_dir):

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

def get_documents_words_to_clasificated():
    documents = []
    for file_name in os.listdir("SeriesClasificacion"):

        infile = open("SeriesClasificacion/" + file_name, 'r')

        text = ""
        # Realizamos el for porque el metodo readLines nos da una lista por cada párrafo y necesitamos juntarlo
        for line in infile.readlines():
            text += " " + line

        doc = Document(file_name.split(".")[0], text, file_name)

        doc.words = get_words_text(doc.text)

        documents.append(doc)

        infile.close()

    return documents


# Genera el archivo CSV a partir del listado de keywords con sus calculos realizados
def save_information_csv():
    filename = './datos/keywords.csv'
    if not os.path.exists(os.path.dirname(filename)): # Comprobamos que el directorio existe, sino pues lo creamos
        os.makedirs(os.path.dirname(filename))
    archivo = open(filename, 'w')

    # Empezamos escribiendo en el fichero la primera linea que será la de los titulos y luego se va recorriendo
    # y guardando los objetos KeyWords tal y como indica su metodo "str".
    archivo.write('Categoria;Palabra' + '\n')
    for c in categories:
        for w in categories[c]:
            word = c + ";" + w + "\n"

            archivo.write(word)


# Genera el archivo CSV a partir del listado de keywords con sus calculos realizados
def save_information_csv2(keywords):
    filename = './datos/keywords.csv'
    if not os.path.exists(os.path.dirname(filename)): # Comprobamos que el directorio existe, sino pues lo creamos
        os.makedirs(os.path.dirname(filename))
    archivo = open(filename, 'w')

    # Empezamos escribiendo en el fichero la primera linea que será la de los titulos y luego se va recorriendo
    # y guardando los objetos KeyWords tal y como indica su metodo "str".
    archivo.write('Categoria;Palabra' + '\n')
    for k in keywords:
        archivo.write(k.string_export_csv_category_keyword())

# Se obtienen las las palabras claves y categorias del archivo csv donde están almacenadas.
def get_data_csv():
    keywords = []
    with open('./datos/keywords.csv') as csvdata:
        input = csv.reader(csvdata)
        indice = 0
        for reg in input:
            datas = reg[0].split(';')
            if indice > 0:
                keywords.append(KeyWord(datas[0], datas[1]))
            else:
                indice += 1

    return keywords

# Método para clasificar las palabras claves por categorias y tener un acceso más fácil
def get_category_dictionary():
    keywords = get_data_csv()
    dictionary_category = {}
    for k in keywords:

        if k.category in dictionary_category:
            dictionary_category[k.category].append(k.word)
        else:
            dictionary_category[k.category] = [k.word]

    return dictionary_category

# Esta función calcula la proximidad entre dos vectores
def proximidad(w1, w2):
    numerador = 0
    denominador1 = 0
    denominador2 = 0
    result = 0
    for i in range(len(w1)):
        numerador += float(w1[i]*w2[i])
    for i in range(len(w1)):
        denominador1 += float(math.sqrt(w1[i]*w1[i]))
    for i in range(len(w2)):
        denominador2 += float(math.sqrt(w1[i]*w1[i]))
    if denominador1 == 0.0 or denominador2 == 0.0:
        result = 0.0
    else:
        result = float((numerador) / (denominador1 * denominador2))
    return result

# Obtener todas las categorias de los nombres de las carpetas para mostrarle al usuario las categorias disponibles para
# añadir palabras claves
def get_all_categories():
    categories_cod = {}
    for category_dir in os.listdir("Series"):
        categories_cod[category_dir[:2].lower()] = category_dir
        print("(" + category_dir + ") - " + category_dir[:2].lower())

    return categories_cod

# Se encarga de insertar las palabras claves. Primero te muestra todas las categorias de las que se dispone y luego
# solicita que selecciones una categoría, una vez seleccionada te pide que insertes la palabra clave que se desee. El
# método pararía de ejecutarse cuando se encuentre la cadena "/exit" en el insertar categoría o palabra clave.
def insert_keywords(categories):
    print("Se muestran las categorias encontradas:")
    categories_cod = get_all_categories()
    keywords = get_data_csv()
    keyword = None
    while keyword != "/exit":
        category = input("Seleccione las dos letras de la categoria que quiera incluir palabras claves: ")
        if category in categories_cod or category == "/exit":
            if category != "/exit":
                print("Palabras registradas para la categoría" + categories_cod[category] + ":")
                if categories_cod[category] in categories:
                    print(categories[categories_cod[category]])
                    print("\n")
                else:
                    categories[categories_cod[category]] = []
                    print("No se disponen de palabras claves para esa categoría.\n")
                keyword = input("Introduzca la palabra clave: ")
                if keyword != "/exit":
                    keywords.append(KeyWord(categories_cod[category], keyword))
                    categories[categories_cod[category]].append(keyword)
                    print("La categoría y la palabra clave introducidas son :" + category + " - " + keyword + "\n")
            else:
                print("Se ha terminado de añadir palabras claves.")
                break
        else:
            print("Introducido CÓDIGO CATEGORÍA INCORRECTO!\n")
    save_information_csv2(keywords)
    print("Fin del programa")



