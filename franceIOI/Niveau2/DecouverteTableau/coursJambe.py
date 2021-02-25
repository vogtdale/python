'''
Le premier entier à lire est le nombre de participants (au plus 3 000) qui sera toujours pair. 
Ensuite il faut lire, pour chaque participant, un entier qu'il a choisi librement.
Les équipes sont constituées ainsi : la personne ayant choisi le plus petit entier est avec celle ayant choisi le plus grand, 
celle ayant choisi le deuxième plus petit est avec celle ayant choisi le deuxième plus grand, et ainsi de suite.
Vous devrez afficher la composition de chacune des équipes, dans l'ordre : d'abord celle dont le plus petit numéro fait partie, puis celle dont le second plus petit numéro fait partie, et ainsi de suite. Au sein de chaque équipe on affichera d'abord le plus petit numéro puis le plus grand.
'''

nbParticipant = int(input())
choix = [0] * nbParticipant

for idPers in range(nbParticipant):
    choix[idPers] = int(input())

choix.sort()

for idPrem in range(nbParticipant//2):
    idSec = nbParticipant - 1 - idPrem
    print(f"{choix[idPrem]} {choix[idSec]}")
