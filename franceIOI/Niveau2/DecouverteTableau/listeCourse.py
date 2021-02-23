'''
Ce que doit faire votre programme :
Il y a 10 ingrédients et ils ont tous un prix au kilo différent : 9, 5, 12, 15, 7, 42, 13, 10, 1 et 20.

Votre programme devra lire 10 entiers, le poids (en kilogrammes) qu'il faut acheter pour chaque ingrédient. Il devra calculer le coût total de ces achats.
'''

prix_kilo = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
cout_total = 0

for item in range(5):
    qty = int(input("Entrez le qty: "))

    cout_total = cout_total + prix_kilo[item] * qty
print(cout_total)
