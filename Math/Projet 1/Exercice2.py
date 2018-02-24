import random

lettre = ["A","B","C","D"]
mot = ""
i = 0

while i<7:
	mot+=random.choice(lettre)
	i += 1

print(mot)


def verifMot(mot, Amot):
	nblettre1 = [0,0,0,0]
	nblettre2 = [0,0,0,0]
	i = 0
	for value in mot:
		if value == "A":
			nblettre1[0] += 1
		if value == "B":
			nblettre1[1] += 1
		if value == "C":
			nblettre1[2] += 1
		if value == "D":
			nblettre1[3] += 1

	for value in Amot:
		if value == "A":
			nblettre2[0] += 1
		if value == "B":
			nblettre2[1] += 1
		if value == "C":
			nblettre2[2] += 1
		if value == "D":
			nblettre2[3] += 1

	while i<4:
		if(nblettre1[i]<nblettre2[i]):
			return False
		i += 1
	return True


def trouve(mot, lettre):
	result = []
	test = False
	for v1 in lettre:
		for v2 in lettre:
			for v3 in lettre:
				for v4 in lettre:
					for v5 in lettre:
						for v6 in lettre:
							for v7 in lettre:
								if verifMot(mot,v1+v2+v3+v4+v5+v6+v7):
									for t in result:
										if t == v1+v2+v3+v4+v5+v6+v7:
											test = True
									if test == False:
										result.append(v1+v2+v3+v4+v5+v6+v7)
									test = False
	return result

anagram = trouve(mot,lettre)

for value in anagram:
	print(value)
