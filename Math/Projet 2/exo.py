import sys
import os
import random

try:
    if len(sys.argv) != 4:
        raise Exception()
except Exception:
    print ("Il faut 3 argument pour que le programme fonctionne")

b = int(sys.argv[1])
s = int(sys.argv[2])
n = int(sys.argv[3])

# retourne un nombre divisible par 5
def div_cinq(a):
    res = int(round(a*100,2))
    res = res % 5
    if res >= 3:
        res1 = 5 - res
        return round((a+(res1/100)),2)
    else:
        return round((a-(res/100)),2)


def init_prix_stock(b,s):
    tab = []
    n = 0
    while n < b:
        tab.append([div_cinq(round(random.uniform((s*b/20),(s*b/5)),2)),s])
        n += 1
    return tab

def calcul_prob(b,tab):
    pt=0
    p=0
    i=0
    while i<b:
        p = p + 1/tab[i][0]
        i+=1

    i=0
    pt = 1/p
    while i<b:
        tab[i].append(round(pt/tab[i][0],3))
        i+=1

    i=0
    while i<b:
        tab[i].append((pt/tab[i][0])*n)
        i+=1

tab = init_prix_stock(b,s)
print(tab)
calcul_prob(b,tab)
print(tab)

ligne1 = ''
ligne2 = ''
ligne3 = ''
ligne4 = ''

for value in tab:
    ligne1 += '{:.2f}'.format(value[0]) + " "

for value in tab:
    ligne2 += '{:.3f}'.format(value[2]) + " "

for value in tab:
    ligne3 += '{:.0f}'.format(value[3]) + " "

print(ligne1)
print(ligne2)
print(ligne3)
print(ligne4)
