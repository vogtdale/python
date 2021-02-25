nbPerson = int(input())
nbProduits = int(input())
wishlist = [0] * nbProduits

for idpers in range(nbPerson):
    numProduit = int(input())
    wishlist[numProduit] = wishlist[numProduit] + 1

for num in range(nbProduits):
    print(wishlist[num])




