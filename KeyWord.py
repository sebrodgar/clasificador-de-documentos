class KeyWord(object):

    # Permitimos que el constructor se pueda crear con solo los parametros category y word, para ello dejamos los demás
    # parametros por defecto a -1 para saber que es un valor que no pueden tener calculados.
    def __init__(self, category, word, pc=-1, appearances=-1, ptc=-1):
        self.category = category
        self.word = word
        self.pc = pc
        self.ptc = ptc
        self.appearances = appearances

    def string_export_csv_category_keyword(self):
        res = self.category + ";" + self.word + "\n"

        return res

    def __str__(self):
        res = self.category + ";" + self.word + ";" + str(self.pc) + ";" + str(self.ptc) + ";" + str(self.appearances) \
              + "\n"

        return res