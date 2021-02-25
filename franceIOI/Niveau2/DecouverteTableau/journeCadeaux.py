'''
Il devra lire un premier entier, le nombre d'habitants (au plus 1000) puis, pour chaque habitant il devra lire sa fortune, un entier. Il devra calculer puis afficher une valeur permettant de dire facilement si une personne est riche ou pas, simplement en regardant si la fortune de cette personne est plus grande ou plus petite que cette valeur.

Deux cas peuvent se présenter :

Si le nombre d'habitants est impair, par exemple si leurs fortunes sont 10, 5, 12, 8, 3 alors la valeur recherchée est 8. En effet, il y aura alors 2 personnes "riches" (10 et 12), 2 "moins riches" (3 et 5) et 1 juste au milieu (8) qui ne donnera ni recevra de cadeau.
Si le nombre d'habitants est pair, par exemple si leurs fortunes sont 10, 5, 12, 8, 3, 9 alors la valeur recherchée est entre 8 et 9. Il y a en effet 3 personnes "riches" (9, 10 et 12) et 3 "moins riches" (3, 5 et 8). Par convention on prendra la valeur 8.5, c'est-à-dire la moyenne de 8 et 9.
'''

nbPerson = int(input())
fortune = [0] * nbPerson 

for idPerso in range(nbPerson):
    fortune[idPerso] = int(input())

fortune.sort()
print("liste of nbPers Fortunes ",fortune)

# calculate a median impair or pair 

if (nbPerson % 2 == 1):
    middle = (nbPerson - 1) // 2
    print(fortune[middle])
else:
    middle = nbPerson//2
    print((fortune[middle - 1] + fortune[middle]) / 2)
    