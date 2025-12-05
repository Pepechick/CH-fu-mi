mclass Files:
    """ Classe File implémentée en python
    à partir de liste python
    """
    def __init__(self):
        self.file = []

    def est_vide(self):
        if self.file == []:
            return True
        else:
            return False

    def defiler(self):
        if not self.est_vide():
            val = self.file[0]
            del self.file[0]
            return val
        else:
            print("Attention la file est vide")
            return None

    def enfiler(self, element):
        self.file = self.file + [element]
        return None

