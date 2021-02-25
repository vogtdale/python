'''
Votre programme devra lire deux entiers : le nombre total de positions sur la table (au maximum 1000) et le nombre de changements de positions. Il devra ensuite lire, pour chaque position, un entier : le numéro de la personne qui doit, actuellement, 
s'installer à cette position.
Il faut lire ensuite les changements exprimés sous la forme de deux entiers chacun : position1 et position2. Un changement (position1, position2) signifie que les deux personnes qui étaient à ses positions doivent échanger leurs places (les positions sont indexées à partir de 0).
Vous devrez afficher, pour chaque position, le numéro de la personne qui s'y trouve une fois tous les changements faits.
'''

nbPers = int(input())
nbChange = int(input())
identity = [0] * nbPers

for numPers in range(nbPers):
   identity[numPers] = int(input())
   
for idChange in range(nbChange):
   firstPers = int(input())
   secondPers = int(input())
   tempor = identity[firstPers]
   identity[firstPers] = identity[secondPers]
   identity[secondPers] = tempor
   
for numPers in range(nbPers):
   print(identity[numPers])


for numPers in range(nbPers):
    print(f"{identity[numPers]}")

