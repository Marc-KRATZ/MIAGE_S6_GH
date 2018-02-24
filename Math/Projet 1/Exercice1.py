import random
import time


nbAlea = []
i = 0

while i < 100:
	nbAlea.append(round(random.uniform(0,10),2))
	i += 1


i = 0
afficheNbs = ""


while i < 100:
	afficheNbs += str(nbAlea[i]) + " "
	i += 1

print(afficheNbs)

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


print (effectifInter(0,1,nbAlea), effectifInter(1,3,nbAlea), effectifInter(3,7,nbAlea), effectifInter(7,9,nbAlea), effectifInter(9,10,nbAlea))

print (effectifFreq(0,1,nbAlea), effectifFreq(1,3,nbAlea), effectifFreq(3,7,nbAlea), effectifFreq(7,9,nbAlea), effectifFreq(9,10,nbAlea))

print (effectifDens(0,1,nbAlea), effectifDens(1,3,nbAlea), effectifDens(3,7,nbAlea), effectifDens(7,9,nbAlea), effectifDens(9,10,nbAlea))
