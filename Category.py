class Category(object):

    def __init__(self, name):
        self.name = name
        self.pc = -1
        self.keywords = {}# Este diccionario seguiría este patrón {'palabra':ptc,'palabra':ptc}


    def __str__(self):
        res = self.name + ";" + self.pc + ";" + str(self.keywords) + "\n"

        return res