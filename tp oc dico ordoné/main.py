class DictionnaireOrdonne(object):
    def __init__(self, **args):
        self.args = args


    def affiche(self):
        print (self.args)


test = DictionnaireOrdonne(carrote = 26, poire = 45)
test.affiche()
