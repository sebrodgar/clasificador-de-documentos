
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from Document import Document
from Bayes import Bayes
from ClassificationBayes import ClassificationBayes
from ClasificationKnn import  ClasificationKnn
from Bayes import Bayes
from Knn import Knn
import AuxiliaryMethods as AuxiliaryMethod


categories = {}

documents = []
documents_by_category = {} # Se usa para no tener que ir calculando cada vez todas los documentos de una categoria
documents_to_clasificated = []

#Creamos y descargamos los partidos de la jornada


print("Comienza el programa de obtención de documentos")

AuxiliaryMethod.get_documents_words(documents, documents_by_category)
#AuxiliaryMethod.save_information_csv()
categories = AuxiliaryMethod.get_category_dictionary()
action_option = ""
while action_option != "/exit":
    print("¿Qué acción desea realizar?")
    action_option = input("1 - Insertar nuevas palabras claves, 2 - Clasificar los documentos utilizando Naives Bayes, 3 - Clasificar "
          "los documentos usando Knn \n")

    if action_option == "1":
        AuxiliaryMethod.insert_keywords(categories)
        categories = AuxiliaryMethod.get_category_dictionary()

    elif action_option == "2":
        print("Comienza el programa de clasifiación de datos.\n"
              "Elija opción para la ruta donde obtener los documentos: R (raiz del proyecto) o escriba ruta")
        option = input()
        if option == "R" or option == "r":
            bayes = Bayes(documents, categories, documents_by_category, "")
            bayes.start_algorithm()
        else:
            bayes = Bayes(documents, categories, documents_by_category, option)
            bayes.start_algorithm()
        documents_to_clasificated = AuxiliaryMethod.get_documents_words_to_clasificated()
        if option == "R" or option == "r":
            for r in range(0, len(documents_to_clasificated) - 1):
                bayesC = ClassificationBayes(documents_to_clasificated[r], "datos/datos_bayes.csv")
                bayesC.start()
        else:
            for r in range(0, len(documents_to_clasificated) - 1):
                bayesC = ClassificationBayes(documents_to_clasificated[r], option)
                bayesC.start()

    elif action_option == "3":
        print("Comienza el programa de clasifiación de datos.\n"
              "Elija opción para la ruta donde obtener los documentos: R (raiz del proyecto) o escriba ruta")
        option = input()
        if option == "R" or option == "r":

            knn = Knn(documents, categories, documents_by_category, "")
            knn.start_algorithm()
        else:
            kann = Knn(documents, categories, documents_by_category, option)
            knn.start_algorithm()

        documents_to_clasificated = AuxiliaryMethod.get_documents_words_to_clasificated()

        k = input("Establezca un k mayor que cero: ")
        if k.isdigit() and int(k) > 0:
            for r in range(0, len(documents_to_clasificated) - 1):
                KnnC = ClasificationKnn(documents_to_clasificated[r], documents, categories, "datos/datos_knn.csv", k)
                KnnC.start()





'''if option == "R" or option == "r":
    bayes = Bayes(documents, categories, documents_by_category, "")
else:
    bayes = Bayes(documents, categories, documents_by_category, option)
'''


print("Programa Terminado")
