import os
import sys
import math
import random

# Classe générique pour toutes les surfaces
class Surface:

    # la classe aura quatre attributs à instancier à la création des objets...
    # mais uniquement dans les classes qui en hérite
    # attributs : x_min, x_max, y_min, y_max
    # à initialiser avec des self.x_min = 0 par exemple
    # et à chaque appel, il faudra bien penser au self.x_min au lieu de x_min
    # ces nombres définissent le rectangle dans lequel les points seront tirés :
    # sommets : (x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)

    def __init__(self):
        raise NotImplementedError("Vous ne pouvez pas instancier cette classe !")

    # tirage d'une abscisse au hasard dans l'intervalle [x_min; x_max]
    def randomX(self):
        return (random.uniform(self.x_min,self.x_max))

    # tirage d'une ordonnée au hasard dans l'intervalle [y_min; y_max]
    def randomY(self):
        return (random.uniform(self.y_min,self.y_max))

    # permet de savoir si un point est dans la surface ou non :
    # à réimplémenter pour chaque type de surface (mais pas ici !)
    def isInArea(self,x,y):
        return true

    # tirage de nbRepet points dans le rectangle de sommets :
    # (x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)
    # renvoie le nombre de ces points qui étaient dans la surface
    def countMonteCarlo(self,nbRepet):
        count = 0
        i = 0
        while i < nbRepet:
            if (self.isInArea(self.randomX(),self.randomY())):
                count = count + 1
            i = i + 1
            pass
        return count

    # calcule une estimation de l'aire si count points étaient dans la surface
    # lors de nbRepet tirages de points
    def areaMonteCarlo(self,count,nbRepet):
        surf = (self.x_max-self.x_min) * (self.y_max-self.y_min)
        return ((count * surf) / nbRepet)

    # calcule une estimation de l'aire si count points étaient dans la surface
    # lors de nbRepet tirages de points
    def printMonteCarlo(self,count,area):
        print(count,'{:.3f}'.format(area))
        return None

    # construit la chaîne de caractères avec en premier le nombre de points
    # dans la surface, puis une espace, puis l'estimation de l'aire de la
    # surface avec 3 chiffres obligatoires derrière la virgule
    # affiche cette chaîne de caractères
    def simulateMonteCarlo(self,nbRepet):
        count = self.countMonteCarlo(nbRepet)
        area = self.areaMonteCarlo(count,nbRepet)
        self.printMonteCarlo(count,area)
        return None

# 1e experience : la surface est un rectangle
# Attention, il y a deux rectangles du coup ici :
# - celui dans lequel les points sont tirés (attributs d'une surface)
# - celui que l'on cherche à mesurer (méthode isInArea)
class Rectangle(Surface):

    # définition du rectangle dans lequel les points seront tirés
    def __init__(self):
        self.x_min = 1
        self.x_max = 4
        self.y_min = 0.5
        self.y_max = 2.5
        return None

    # quand est-ce qu'un point tiré au hasard est dans le rectangle à mesurer ?
    def isInArea(self,x,y):
        test = False
        if(2<=x<=3):
            if(1<=y<=2):
                test = True
        return test

# 2e experience : la surface est un cercle
class Circle(Surface):

    # définition du rectangle dans lequel les points seront tirés
    def __init__(self):
        self.x_min = -1
        self.x_max = 1
        self.y_min = -1
        self.y_max = 1
        return None

    # quand est-ce qu'un point tiré au hasard est dans le cercle ?
    def isInArea(self,x,y):
        test = False
        if (math.sqrt((x*x)+(y*y))<=1):
            test = True
        return test

# 3e experience : la surface est celle indiquée dans le graphique de l'énoncé
class Graph(Surface):

    def __init__(self):
        self.x_min = -1
        self.x_max = 1
        self.y_min = -2
        self.y_max = 3
        return None

    def isInArea(self,x,y):
        test = False
        if (math.exp(x)>=y):
            if ((x-(x*x*x)-1)<=y):
                test = True
        return test

# Execution du programme
if len(sys.argv) > 1:
    _nbRepet = int(sys.argv[1])

    # 1e experience : rectangle
    exp1 = Rectangle()
    exp1.simulateMonteCarlo(_nbRepet)

    # 2e experience : cercle
    exp2 = Circle()
    exp2.simulateMonteCarlo(_nbRepet)

    # 3e experience : surface du graphique
    exp3 = Graph()
    exp3.simulateMonteCarlo(_nbRepet)

else:
    print ("No arguments")
