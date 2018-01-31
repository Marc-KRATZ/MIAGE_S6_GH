import random

nbAlea = []
i = 0

while i < 100:
	nbAlea.append(round(random.uniform(0,10),2))
	i += 1

print (i)
i = 0

while i < 100:
	print('{0:8} {1:8} {2:10} {3:10}'.format(nbAlea[i],nbAlea[i+1],nbAlea[i+2],nbAlea[i+3]))
	i += 4


