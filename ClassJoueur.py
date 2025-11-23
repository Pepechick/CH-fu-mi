from File import Files
from microbit import *

class Joueur:
    def __init__(self):
        self.statut = None      # Il pourra être soit éméteur, soit recepteur
        self.name = None        # Le choix du nom se fait en début de partie
        self.choix = None       # Le choix correspond à la valeur choisi à chaque manche
        self.score = 0          # A 3, la partie s'arrête
        self.connexion = "non"  # Oui quand le joueur à appuyé sur A pendant 5sec

    def Choix_du_nom(self):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        f = Files()
        liste_nom = []
        seuil_validation = 2000
        terminer = False
        for index in alpha :
            f.enfiler(index)
        lettre = f.defiler()
        f.enfiler(lettre)
        display.show(str(lettre))

        while not terminer:
            if button_a.was_pressed():
                lettre = f.defiler()
                f.enfiler(lettre)
                display.show(str(lettre))
                sleep(200)
            if button_b.was_pressed():
                liste_nom.append(lettre)
                display.show(Image.YES)
                sleep(300)
                display.show(str(lettre))
            if button_b.is_pressed():
                t0 = running_time()
                while button_b.is_pressed():
                    if running_time() - t0 > seuil_validation:
                        terminer = True
                        break

        self.name = "".join(liste_nom)
        display.scroll(self.name)
        sleep(1000)
        return self.name