class KeywordKnn(object):

    def __init__(self, word, serie, category, frequency, weight):
        self.word = word
        self.serie = serie
        self.category = category
        self.frequency = frequency
        self.weight = weight

    def __str__(self):
        res = self.word + ", " + self.serie + " (" + self.category + ")" + ", Frecuencia: " + str(self.frequency) + ", Peso: " + str(self.weight)
        return res