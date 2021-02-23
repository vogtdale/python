'''
On vous donne le numéro du produit préféré par différentes personnes. Écrivez un programme qui indique pour chaque numéro de produit, le nombre de personnes dont c'est le produit préféré.
'''
nbProduits = int(input("Entrez le nombre de produits: "))
nbPerson = int(input("Entrez le nombre de pers: "))
wishList = [0] * nbProduits

for idPers in range(nbPerson):
    numProduct = int(input("Entrez le numero du produit prefere: "))
    wishList[numProduct] = wishList[numProduct] + 1

for numProduct in range(nbProduits):
    print(wishList[numProduct])
