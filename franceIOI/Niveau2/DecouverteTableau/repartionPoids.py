'''
Ce que doit faire votre programme :
On vous décrit les charrettes qui composent une caravane, en vous donnant pour chacune, le poids des marchandises qu'elle transporte.
Votre programme doit déterminer quel poids ajouter ou retirer à chaque charrette, pour qu'elles transportent toutes ensuite le même poids, et ce sans modifier le poids total transporté par l'ensemble des charrettes de la caravane.

INPUT
L'entrée commence par un entier nbCharrettes (nbCharrettes <= 3000) : le nombre de charrettes de la caravane.
Les nbCharrettes lignes suivantes décrivent chacune une charrette par un nombre décimal : le poids qu'elle transporte initialement.

OUTPUT
Vous devez afficher nbCharrettes nombres décimaux sur la sortie : le poids à ajouter à chaque charrette (ce qui revient à en retirer si ce nombre est négatif), dans le même ordre que celui de l'entrée. Il n'y a pas d'arrondis à faire.
'''

nbChars = int(input("Entrez nombre de Charrette: "))
poids = [0.0] * nbChars

poidsTot = 0.0

for numChars in range(nbChars):
    poids[numChars] = float(input("Entrez le nobre de kilo que chaq char transport: "))
    poidsTot = poidsTot + poids[numChars]

moyen = poidsTot / nbChars

for numero in range(nbChars):
    print(moyen - poids[numero])
