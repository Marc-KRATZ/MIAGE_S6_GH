import random
import time

print("Exercice 1")

print("\n")

nbAlea = []
i = 0

while i < 100:
	nbAlea.append(round(random.uniform(0,10),2))
	i += 1

print ("Liste des nombres :\n")
i = 0

while i < 100:
	print('{0:8} {1:8} {2:10} {3:10} {4:10}'.format(nbAlea[i],nbAlea[i+1],nbAlea[i+2],nbAlea[i+3],nbAlea[i+4]))
	i += 5

def effectifInter(a,b,tab):
	compteur = 0
	for value in tab:
		if value >= a and value < b:
			compteur += 1
	return compteur

def effectifFreq(a,b,tab):
	compteur = 0
	for value in tab:
		if value >= a and value < b:
			compteur += 1
	return compteur/len(tab)

def effectifDens(a,b,tab):
	compteur = 0
	for value in tab:
		if value >= a and value < b:
			compteur += 1
	return compteur/(b-a)

print("\n")

print ("Effectif sur l'intervalle [0;1[ :", effectifInter(0,1,nbAlea))
print ("Effectif sur l'intervalle [1;3[ :", effectifInter(1,3,nbAlea))
print ("Effectif sur l'intervalle [3;7[ :", effectifInter(3,7,nbAlea))
print ("Effectif sur l'intervalle [7;9[ :", effectifInter(7,9,nbAlea))
print ("Effectif sur l'intervalle [9;10[ :", effectifInter(9,10,nbAlea))

print("\n")

print ("Fréquence sur l'intervalle [0;1[ :", effectifFreq(0,1,nbAlea))
print ("Fréquence sur l'intervalle [1;3[ :", effectifFreq(1,3,nbAlea))
print ("Fréquence sur l'intervalle [3;7[ :", effectifFreq(3,7,nbAlea))
print ("Fréquence sur l'intervalle [7;9[ :", effectifFreq(7,9,nbAlea))
print ("Fréquence sur l'intervalle [9;10[ :", effectifFreq(9,10,nbAlea))

print("\n")

print ("Densité sur l'intervalle [0;1[ :", effectifDens(0,1,nbAlea))
print ("Densité sur l'intervalle [1;3[ :", effectifDens(1,3,nbAlea))
print ("Densité sur l'intervalle [3;7[ :", effectifDens(3,7,nbAlea))
print ("Densité sur l'intervalle [7;9[ :", effectifDens(7,9,nbAlea))
print ("Densité sur l'intervalle [9;10[ :", effectifDens(9,10,nbAlea))

print("\n")

print("Exercice 2")


lettre = ["A","B","C","D"]
mot = ""
i = 0

while i<7:
	mot += random.choice(lettre)
	i += 1




quit = ""
while quit != "q":
	quit = input("Pour quitter entrez q : ")
