class KeyWord(object):
    '''def __init__(self, word, category, appearances, pc):
        self.word = word
        self.category = category
        self.appearances = appearances
        self.ptc = -1.0
        self.pc = pc
'''
    def __init__(self, category, word, pc, appearances, ptc=-1):
        self.category = category
        self.word = word
        self.pc = pc
        self.ptc = ptc
        self.appearances = appearances

    def __str__(self):
        res = self.category + ";" + self.word + ";" + str(self.pc) + ";" + str(self.ptc) + ";" + str(self.appearances) \
              + "\n"

        return res