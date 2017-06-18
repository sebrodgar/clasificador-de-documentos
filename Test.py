#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from Document import Document
from Bayes import Bayes
from ClassificationBayes import ClassificationBayes
from Bayes import Bayes
import AuxiliaryMethods as AuxiliaryMethod


categories = {"Comedia": ["cómico", "cómica", "cómicos", "cómicas", "risa", "risas", "comedia", "comedias", "humor", "peculiar"
                          , "surrealista", "surrealistas", "extravagante", "extravagantes", "chiste", "chistes", "gracioso", "graciosa",
                          "graciosos", "graciosas", "divertido", "divertida"],
              "Misterio": ["intriga", "intrigas", "misterio", "misterioso", "misteriosa", "misteriosos", "misteriosas", "asesinato",
                           "asesinatos", "cadáver", "muerte", "muerto", "muerta", "muere", "muerte", "malvado", "malvada", "malvados", "malvadas",
                           "desaparición", "crimen", "crímenes", "caso", "casos", "detective", "sospechoso", "investigación", "investigaciones","suspense"],
              "Infantil": ["niño", "niña", "niños", "niñas", "infantil", "infantiles", "divertido", "divertida", "aventura", "aventuras",
                           "dibujo", "dibujos", "animado", "animada", "animados", "animadas", "animación", "infancia", "gracioso", "graciosa",
                           "graciosos", "graciosas", "héroe"]}
documents = []
documents_by_category = {} # Se usa para no tener que ir calculando cada vez todas los documentos de una categoria

#Creamos y descargamos los partidos de la jornada
print("Comienza el programa de obtención de datos.\n"
      "Elija opción para la ruta donde guardar los documentos: R (raiz del proyecto) o escriba ruta")
option = input()

print("Comienza el programa de obtención de documentos")

AuxiliaryMethod.get_documents_words(documents, documents_by_category)

if option == "R" or option == "r":
    bayes = Bayes(documents, categories, documents_by_category, "")
else:
    bayes = Bayes(documents, categories, documents_by_category, option)


bayes.start_algorithm()

AuxiliaryMethod.save_information_csv()
print("Programa Terminado")
