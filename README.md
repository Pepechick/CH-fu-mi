# Partie de Chi Fu Mi Gorn Spock

# Préparation des joueurs :
Carte joueur :

Un petit message apparait sur la carte : "appuyez 3s" 
Appuyez 3 secondes sur le bouton A
Normalement la première lettre de l'alphabet devrait apparaitre

C'EST L'ETAPE DE SELECTION DU NOM : 
Appuyer sur le bouton A pour défiler les lettres
Appuyer sur le bouton B pour selectionner la lettre
(Normalament le symbole de validation devrait apparaitre. Appuyer su A pour revenir aux lettres)
Quand vous avez fini, (ATTENTION ! Il y a un bug au niveau de la validation, c'est pour ça que vous devez revenir aux lettres avant de valider, vous ne devez surtout pas rester sur le symbole de validation), appuyer sur le bouton B 3 seconde et relacher quand vous voyer défiler votre nom. 

Dans la seconde qui suit un C devrait apparaitre sur la carte. C'est que vous êtes connecté.


Carte arbitre :

Au départ le chiffre zéro apparait sur la carte, c'est le nombre de joueurs connectés.
Quand un joueur envoie son nom, la carte prend en compte ce nouveau joueur et augmente le compteur.

Pour lancer la partie il suffit d'appuyer sur le bouton A de la carte.

Maintenant il devrait y avoir le chiffre 1, c'est le nombre de manche 
appuyez sur le bouton A pour défiler les élements,
et appuyer 2 secondes sur B pour accepter le nombre de manches.


# Déroulement de la partie :
Carte joueur :
(ça marche pour un nombre de partie entre 1 et 9, et seulement les chiffres impaires)

Maintenant que la partie s'est lancée, les symboles apparaissent à l'écran.
(carré = feuille, rond = pierre, l'espece de serpent = gorn, la main qui ressemble au symbole des métaleux = spock, et, le dernier les ciseaux)

Appuyez sur A pour défiler puis sur B 2 secondes pour selectionner.
Là le nom du symbole devrait défiler sur la carte.

Si le joueur est gagnant de la manche sa carte devrait sonner.
(il peut arrivé que plusieurs joueurs gagnent et que donc plusieurs cartes sonnent. 
C'est parce que le code prend en compte un score_max, et si plusieurs joueurs ont le score_max, alors leurs cartes sonnent)


Carte arbitre :

Sur la carte s'affiche le numéro de la manche (première, deuxième, ...)
Tout est automatique dans le code de la carte arbitre, il ne se passe pas grand chose de visuel sur la carte.
(plus besoin d'appuyer sur aucun bouton jusqu'a la fin de la partie)


# Fin de partie 
Carte joueur :

Si le joueur a gagné la partie sa carte devrait joueur une musique plus longue à la fin.
(il peut arrivé que plusieurs joueurs gagnent et que donc plusieurs cartes sonnent. 
C'est parce que le code prend en compte un score_max, et si plusieurs joueurs ont le score_max, alors leurs cartes sonnent)