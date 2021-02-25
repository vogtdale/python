'''
Votre programme devra lire le nombre d'emplacements nbEmplacements (au maximum 1 000), 
puis pour chaque emplacement à partir de 0, le numéro du marchand à qui est attribué l'emplacement (entre 0 et nbEmplacements − 1).

Ensuite, pour chaque marchand de 0 à nbEmplacements − 1, votre programme devra afficher le numéro de l'emplacement qui lui est attribué.
'''

nbEmplacements = int(input())
emplMarchands = [0] * nbEmplacements

for iEmp in range(nbEmplacements):
   emplMarchands[iEmp] =  int(input())

for iMarchand in range(nbEmplacements):
   print(emplMarchands[iMarchand])
