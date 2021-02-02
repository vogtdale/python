nbProd = int(input())
nbPers = int(input())
wishlist = [0] * nbProd

for idPers in range(nbPers):
   numProd = int(input())
   wishlist[numProd] = wishlist[numProd] + 1
   print("thid is the whislist",wishlist[numProd])
   
