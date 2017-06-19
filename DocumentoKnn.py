class DocumentoKnn(object):

    def __init__(self, serie, category, weights):
        self.serie = serie
        self.category = category
        self.weights = weights

    def arrayToString(self, array):
        res = ""
        for i in range(len(array)):
            if i is len(array)-1:
                res += str(array[i])
            else:
                res = res + str(array[i]) + "-"
        return res

    def __str__(self):
        weightsString = self.arrayToString(self.weights)
        res = self.serie + ";" + self.category + ";" + weightsString + "\n"
        return res