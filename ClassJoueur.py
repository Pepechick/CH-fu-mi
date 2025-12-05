from File import Files
from microbit import *
import radio
import music

radio.on()
radio.config(channel=7)

class Joueur:
    def __init__(self):
        self.name = None  
        # Le choix du nom se fait en début de partie
        self.choix = None  
        # Le choix correspond à la valeur choisi à chaque manche
        self.connecte = "non"  
        # Oui quand le joueur à appuyé sur A pendant 5sec

    def transition(self):
        """méthode qui crée une transition"""
        for y in range(5):
            for x in range(5):
                display.set_pixel(x, y, 9) 
                sleep(80)
        sleep(500)
    
    def Choix_du_nom(self):
        """méthode qui permet de choisir son nom"""

        alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXY" 
        f = Files()  # On crée une file f
        liste_nom = []
        seuil_validation = 2000
        terminer = False
        for index in alpha:
            f.enfiler(index) # on enfile les lettres de alpha

        # permet d'afficher les lettres
        lettre = f.defiler()
        f.enfiler(lettre)
        display.show(str(lettre))

        # permet de faire défiler les lettres
        # lorsqu'on appuie sur a les éléments défilent
        # lorsqu'on appuie sur b rapidemment les lettres sont validés
        # lorsqu'on appuie sur b pendant 3sec le nom est validé
        while not terminer:
            if button_a.was_pressed():
                lettre = f.defiler()
                f.enfiler(lettre)
                display.show(str(lettre))
                sleep(200)
            if button_b.is_pressed():
                t0 = running_time()
                while button_b.is_pressed():
                    if running_time() - t0 > seuil_validation:
                        terminer = True
                        break
                else:
                    liste_nom.append(lettre)  # ajout simple si press courte
                    display.show(Image.YES)
                    sleep(300)

        self.name = "".join(liste_nom)
        display.scroll(self.name)
        sleep(100)
        return

    def Choix_symbole(self):
        """méthode qui permet de choisir son symbole"""

        dictio_symboles = {
            "pierre": Image("09990:" "90009:" "90009:" "90009:" "09990:"),
            "feuille": Image("99999:" "90009:" "90009:" "90009:" "99999:"),
            "ciseaux": Image("90009:" "09090:" "00900:" "09090:" "09090:"),
            "gorn": Image("99999:" "00009:" "99999:" "90000:" "99999:"),
            "spock": Image("09090:" "09090:" "09990:" "99990:" "09990:"),
        }
        f = Files() # On crée une file f
        seuil_validation = 2000
        terminer = False
        for cle, valeur in dictio_symboles.items():
            f.enfiler((cle, valeur))  # on enfile cle valeur de dictio_symboles
        
        # permet d'afficher l'image du symbole
        symbole_courant = f.defiler()
        if symbole_courant is not None:
            cle, image = symbole_courant
            f.enfiler(symbole_courant)
            display.show(image)

        # permet de faire défiler les images
        # lorsqu'on appuie sur a les symboles défilent
        # lorsqu'on appuie sur b pendant 2sec le symbole est validé
        while not terminer:
            if button_a.was_pressed():
                symbole_courant = f.defiler()
                if symbole_courant is not None:
                    cle, image = symbole_courant
                    f.enfiler(symbole_courant)
                    display.show(image)
                    sleep(200)
            if button_b.is_pressed():
                start = running_time()
                while button_b.is_pressed():
                    if running_time() - start > seuil_validation:
                        if symbole_courant is not None:
                            self.choix = symbole_courant[0]  # clé du symbole
                            display.show(Image.YES)
                            sleep(300)
                            terminer = True

        display.show(str(self.choix))
        radio.send(str(self.name) + ":" + str(self.choix))
        # envoyer le choix à la carte arbitre ainsi que le nom du joueur
        sleep(1000)
        
        # On met une transition
        self.transition()
        sleep(1000)
        return

    def connexion(self):
        """méthode qui permet de se connecter"""

        display.scroll("APPUI 3s")

        # appuyer 3 secondes pour ce connecter
        while self.connecte == "non":
            if button_a.is_pressed() or button_b.is_pressed():
                start = running_time()
                while button_a.is_pressed() or button_b.is_pressed():
                    if running_time() - start > 3000:
                        # on lance la méthode :
                        self.Choix_du_nom()
                        while True:
                            radio.send(
                                str(self.name)
                            )  # envoyer le nom à la carte arbitre
                            msg = radio.receive()
                            sleep(100)
                            # si on reçoit "ok" un C apparait
                            if msg == "ok":
                                display.show("C")  # Connected
                                self.connecte = "oui"
                                sleep(500)
                                break
        sleep(1000)

        # On met une transition
        self.transition()
        sleep(1000)
        return

    def principal(self):
        """méthodes principale"""

        # tant que le nom n'est pas valide recommencer
        while self.connecte == "non":
            self.connexion()
            display.clear()

        cparti = False
        fin = False

        while True:
            msg = radio.receive()
            sleep(50)
            if not msg:
                continue  # on a rien reçu, on attend
            elif msg == "go":
                cparti = True
            elif msg == "à vos choix" and cparti:
                self.Choix_symbole()
            elif msg == "partie finie":
                # On met une transition
                self.transition()
                sleep(1000)
                fin = True

            # si on reçoit notre nom :
            elif msg == self.name:
                if fin:
                    # La mélodie pour le générique de fin
                    melodie_generique = [
                        "C5:4",
                        "E5:4",
                        "G5:4",
                        "C6:8",
                        "G5:4",
                        "E5:4",
                        "C5:8",
                        "D5:4",
                        "F5:4",
                        "A5:4",
                        "D6:8",
                        "A5:4",
                        "F5:4",
                        "D5:8",
                    ]
                    music.play(melodie_generique)
                    sleep(3000)
                    display.clear()
                    break
                else:
                    display.show(Image.YES)
                    melody = ["C5:4", "E5:4", "G5:4", "C6:8"]
                    music.play(melody)
        return

a = Joueur()
print(a.principal())