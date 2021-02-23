'''
Un livre de comptes décrit les achats et ventes successives de 10 produits numérotés de 1 à 10. 
Le livre décrit les opérations depuis une situation où le stock de chacun des produits était de zéro.
Chaque ligne du livre de comptes décrit l'achat (augmentation du stock)
ou la vente (réduction du stock) d'une certaine quantité de l'un des produits.
Votre objectif est de déterminer pour chaque produit, 
la quantité restant dans le stock à l'issue de l'ensemble de ces achats et ventes.
'''
Qty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nbOperations = int(input())

for i in range(nbOperations):
   idProd = int(input())
   buyorsell = int(input())
   Qty[idProd] = Qty[idProd] + buyorsell

for id in range(1,11):
   print(Qty[id])
