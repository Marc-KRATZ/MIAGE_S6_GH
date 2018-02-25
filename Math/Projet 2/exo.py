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
nb = int(sys.argv[3])

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


tab = init_prix_stock(b,s)
print(tab)

ligne1 = ''
ligne2 = ''
ligne3 = ''
ligne4 = ''

for value in tab:
    ligne1 += '{:.2f}'.format(value[0]) + " "

print(ligne1)
print(ligne2)
print(ligne3)
print(ligne4)
