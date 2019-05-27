class DictionnaireOrdonne():
    def __init__(self, **args):
        self.args = args
        self.key = []
        self.value = []

    def data(self):
        for key in self.args:
            self.key.append(key)
            self.value.append(self.args[key])
        print(self.key, self.value)

        return self.key, self.value
    def __len__(self):
        return len(self.key)
    def __repr__(self):
        exit = ""

        for ex in range(len(self.key)):  #formate pour affichage les clées des tuple en ajoutant des guillemet si la cle est une chaine
            if isinstance(self.key[ex], str):
                exit = exit + "'{}': ".format(self.key[ex])
            else:
                exit = exit + "{}: ".format(self.key[ex])

            if isinstance(self.value[ex], str):#formate pour affichage les valeurs des tuple en ajoutant des guillemet si la valeur est une chaine
                exit += "'{}'".format(self.value[ex])
            else:
                exit += "{}".format(self.value[ex])

            if ex != len(self.key) - 1:
                exit += ", "

        return "{%s}" %exit

    def __setitem__(self, saisi, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur"""
        print(saisi)
        if self.key.count(saisi) == 0:
            self.key.append(saisi)

        index = self.key.index(saisi)
        self.value[index] = valeur


fruits = DictionnaireOrdonne(dsfds = 34, fade = 34)
fruits.data()
print(fruits)
fruits["fade"] = 36
print(fruits)