import os
import sys


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
        # TODO
        return 0
    
    # tirage d'une ordonnée au hasard dans l'intervalle [y_min; y_max]
    def randomY(self):
        # TODO
        return 0

    # permet de savoir si un point est dans la surface ou non :
    # à réimplémenter pour chaque type de surface (mais pas ici !)
    def isInArea(self,x,y):
        return true
    
    # tirage de nbRepet points dans le rectangle de sommets :
    # (x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)
    # renvoie le nombre de ces points qui étaient dans la surface
    def countMonteCarlo(self,nbRepet):
        # TODO
        return 0

    # calcule une estimation de l'aire si count points étaient dans la surface
    # lors de nbRepet tirages de points
    def areaMonteCarlo(self,count,nbRepet):
        # TODO
        return 0

    # calcule une estimation de l'aire si count points étaient dans la surface
    # lors de nbRepet tirages de points
    def printMonteCarlo(self,count,area):
        # TODO
        return None

    # construit la chaîne de caractères avec en premier le nombre de points
    # dans la surface, puis une espace, puis l'estimation de l'aire de la 
    # surface avec 3 chiffres obligatoires derrière la virgule
    # affiche cette chaîne de caractères
    def simulateMonteCarlo(self,nbRepet):
        # TODO
        return None

# 1e experience : la surface est un rectangle
# Attention, il y a deux rectangles du coup ici :
# - celui dans lequel les points sont tirés (attributs d'une surface)
# - celui que l'on cherche à mesurer (méthode isInArea)
class Rectangle(Surface):
    
    # définition du rectangle dans lequel les points seront tirés
    def __init__(self):
        # TODO
        return None
        
    # quand est-ce qu'un point tiré au hasard est dans le rectangle à mesurer ?
    def isInArea(self,x,y):
        # TODO
        return true

# 2e experience : la surface est un cercle
class Circle(Surface):

    # définition du rectangle dans lequel les points seront tirés
    def __init__(self):
        # TODO
        return None

    # quand est-ce qu'un point tiré au hasard est dans le cercle ?
    def isInArea(self,x,y):
        # TODO
        return true

# 3e experience : la surface est celle indiquée dans le graphique de l'énoncé
class Graph(Surface):
    
    def __init__(self):
        # TODO
        return None
    
    def isInArea(self,x,y):
        # TODO
        return true

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

