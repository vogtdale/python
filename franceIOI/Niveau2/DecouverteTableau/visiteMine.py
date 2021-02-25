'''
Il existe 5 types de déplacements, représentés par 5 entiers différents : aller à gauche (1), aller à droite (2), aller tout droit (3), monter (4) et descendre (5).
Le premier entier à lire est le nombre total de déplacements (1000 au maximum). Ensuite, chaque déplacement (représenté par un entier) est indiqué sur sa propre ligne.
Vous devez afficher la suite des déplacements à faire pour aller de votre position actuelle à la sortie.
'''

deplacementInverse = [0, 2, 1, 3, 5, 4]
nbDeplacements = int(input())
chemin = [0] * nbDeplacements
for numero in range(nbDeplacements):
   chemin[numero] = int(input())
for numero in range(nbDeplacements-1, -1, -1):
   deplacement = chemin[numero]
   print(deplacementInverse[deplacement])
