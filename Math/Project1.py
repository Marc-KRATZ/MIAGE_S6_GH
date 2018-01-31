import random

nbAlea = []
i = 0

while i < 100:
	nbAlea.append(round(random.uniform(0,10),2))
	i += 1

print (i)

result=''
for nb in nbAlea:
	result += str(nb) + " "

print(result)