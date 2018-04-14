# Squelette du projet 3

### Contenu

Dans ce dossier, il n'y a qu'un seul fichier en plus du README. Il contient les
différentes définitions de classes utiles :
- Surface : classe abstraite contenant les informations générales pour parler
    d'une surface
- Rectangle : classe pour calculer l'aire d'un rectangle 
- Circle : classe pour calculer l'aire d'un cercle 
- Graph : classe pour calculer l'aire de la surface indiquée sur le graphique.
Enfin, en fin de fichier se trouve la partie principale du programme.  

### Travail à faire

- Surface : compléter toutes les méthodes non abstraites :
  + randomX
  + randomY
  + countMonteCarlo
  + areaMonteCarlo
  + printMonteCarlo
- Rectangle : compléter le constructeur et la méthode isInArea :
  + Rectangle
  + isInArea
- Circle : compléter le constructeur et la méthode isInArea :
  + Circle
  + isInArea
- Graph : compléter le constructeur et la méthode isInArea :
  + Graph
  + isInArea

Vous n'avez pas besoin de modifier la fin du code (partie d'exécution), sauf si
vous avez envie de rendre certaines classes plus génériques (en créant de
meilleurs constructeurs dans les différentes classes, pour qu'ils acceptent des
paramètres).

Afin que le projet soit déjà compilable, toutes les fonctions à modifier
retournent une valeur par défaut (0 si elles devaient renvoyer quelque chose,
None sinon).

Vous n'êtes pas obligés de suivre ce squelette : il ne fait que vous fournir une
aide pour potentiellement aller plus vite. En revanche, je suis sûre qu'il
fonctionne, puisque j'ai un programme qui tourne et fait ce qui est demandé,
après avoir complété ce squelette.

### Installation

Avec un environnement Python3 bien configuré :

Lancement (avec, par exemple, 300 répétitions) :
python3 projet3.py 300

Si vous ne donnez pas de nombre de répétitions, le programme se contentera de
répondre "No Arguments".

### Problèmes

Pour tout problème avec ce squelette, ou question sur comment l'utiliser,
n'hésitez pas à me demander, soit directement, soit par mail
(sophie.bernard@unice.fr).