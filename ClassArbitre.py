from pile import Pile
from microbit import *
import radio

radio.on()
radio.config(channel=7)

class Arbitre:
    def __init__(self):
        self.arbitre = []
        self.joueur_c = 0
    
    def connexion(self):
        incoming = []
        while not button_b.is_pressed() or not button_a.is_pressed():
            incoming.append(radio.receive())
            for i in incoming :
                self.joueur_c += 1
        if button_a.is_pressed() or button_b.is_pressed():
            sleep(1000) 
            self.lancer_partie()
            # l'arbitre choisi de lancer la partie
        return
            
    def lancer_partie(self):
        while self.score() == False:    # <-- TERMINER
            self.lance_manche()
        self.fin()      # <-- TERMINER
    
    def lancer_manche(self):
        radio.send("Go")
        