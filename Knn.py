
class Knn(object):

    # Para el cálculo de las frecuencias podemos guardarlo en un diccionario y podremos seguir el siguiente estilo:
    # frecuencias = {palabra_clave : [listado con los diferentes valores de las columnas correspondientes]}

    def __init__(self, documents_array, categories):
        self.documents_array = documents_array
        self.categories = categories
        self.frequencies = {}

    # Este método debe calcular el número de apariciones que tiene una palabra por cada documento. Cada palabra tiene
    # que tener una columna por cada documento que tengamos.
    def calculate_frequencie(self):
         print("hola")

    # Este método debe calcular el número total de apariciones de cada palabra clave entre todo el conjunto
    # de documentos
    def calculate_documental_frequencie(self):
        print("hola")

    # Este método debe calcular el logaritmo del numero total de documentos entre la frecuencia documental, eso para
    # cada palabra clave
    def calculate_inverse_documental_frequencie(self):
        print("hola")

    # Este método debe calcular el peso de una palabra clave con respecto a cada documento(el peso tiene la representación
    # en la tabla de W), por lo tanto deberá haber con respecto a cada palabra clave una columna de peso por cada documento
    def calculate_weight(self):
        print("hola")





