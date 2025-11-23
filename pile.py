class Pile:
    """ Classe Pile implémentée en python
    à partir de liste python
    """
    def __init__(self):
        self.pile = []

    def est_vide(self):
        if self.pile == []:
            return True
        else:
            return False

    def depiler(self):
        if not self.est_vide():
            val = self.pile[-1] 
            del self.pile[-1]
            return val
        else:
            print("Attention la pile est vide")
            return None
    
    def empiler(self, element):
        self.pile = self.pile + [element]
        return None
    
    def afficher(self):
        for i in range(self.taille()-1, -1, -1):   # balaie la pile en sens inverse
            val = self.pile[i]
            print(f"|{val}|")
        return None
    
    def taille(self):
        taille_pile = 0
        for val in self.pile:
            taille_pile = taille_pile + 1
        return taille_pile
