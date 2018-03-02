import sys
import os
import random


try:
    if len(sys.argv) != 4:
        raise Exception()
except Exception:
    print ("/!------------------------------------------------------!\\")
    print ("/! Il faut 3 arguments pour que le programme fonctionne !\\")
    print ("/!------------------------------------------------------!\\")
    exit()

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

#initialise les prix de chaque biere ainsi que le stock
def init_prix_stock(b,s):
    tab = []
    n = 0
    while n < b:
        tab.append([div_cinq(round(random.uniform((s*b/20),(s*b/5)),2)),s])
        n += 1
    return tab

#calcul de chaque prob des bieres
def calcul_prob_init(b,tab):
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


def calcul_prob(b,tab):
    pt=0
    p=0
    i=0
    while i<b:
        if tab[i][0] > 0:
            p = p + 1/tab[i][0]
        i+=1

    i=0
    pt = 1/p
    while i<b:
        if  tab[i][0] > 0:
            tab[i][2]=round(pt/tab[i][0],3)
        else:
            tab[i][2]=0
        i+=1

#prendre une biere d'apres la probabilite et en utilisant une fonction random entre 0 et 1
def defini_une_biere(tab,b):
    i = 0
    x = random.random()
    somme = 0

    while somme < x and i < b:
        somme += tab[i][2];
        i+=1
    return i

#repetition du premier achat suivant n
def rep_premier_achat(tab,n,b):
    i=0
    while i<b:
        tab[i].append(0)
        i+=1
    i=0
    while i<n:
        tab[defini_une_biere(tab,b)-1][3]+=1
        i+=1

#simule la vente de toutes les bieres
def simule_vente(tab,b,s):
    i=0
    sominit=0
    somfinal=0
    while i<b:
        sominit+=tab[i][0]*s
        i+=1
    i=0
    while i<(b*s):
        sortie = ''
        calcul_prob(b,tab)
        biere = defini_une_biere(tab,b)
        while tab[biere-1][1]==0:
            biere = defini_une_biere(tab,b)
        j=0
        while j<b:
            if j==biere-1:
                somfinal+= tab[biere-1][0]
                tab[biere-1][1]-=1
                tab[biere-1][0]+=(5*(b-1))/100
                if tab[biere-1][1] == 0:
                    tab[biere-1][0] = 0.00
            else:
                if tab[j][1]!=0:
                    tab[j][0]-=0.05
            sortie += '{:.2f}'.format(tab[j][0]) + " "
            j+=1
        print(sortie)
        i+=1
    print('{:.2f}'.format(somfinal-sominit))

#defini la range 0 et 1
tab = init_prix_stock(b,s)
#defini la range 2
calcul_prob_init(b,tab)
#defini la range 3
rep_premier_achat(tab,n,b)


ligne1 = ''
ligne2 = ''
ligne3 = ''


for value in tab:
    ligne1 += '{:.2f}'.format(value[0]) + " "

for value in tab:
    ligne2 += '{:.3f}'.format(value[2]) + " "

for value in tab:
    ligne3 += '{:d}'.format(value[3]) + " "


print(ligne1)
print(ligne2)
print(ligne3)
simule_vente(tab,b,s)
