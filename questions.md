# Partie 1

## Modélisation
- Dans le monde sans contrainte, on peut utiliser un graphe où chaque sommet est connecté à tous les autres sommets, car le drone peut se déplacer en ligne droite sans contrainte.

- Dans le monde avec contraintes, on peut utiliser un graphe dont les arêtes représentent les déplacements possibles du drone, soit en utilisant une variante graphe où les arêtes correspondent à des chemins entre les villages, soit en utilisant une variante obstacle où les arêtes ne peuvent traverser les zones interdites par les obstacles.

Il faut aussi dans les deux cas stocker d'autres informations comme l'emplacement des villages et des drones par exemple.

## Algorithme de parcours
L'algorithme de parcours que l'on peut utiliser pour résoudre ce problème est l'algorithme de Dijkstra, qui permet de trouver le chemin le plus court entre deux sommets dans un graphe pondéré. Dans notre cas, les poids des arêtes pourraient représenter les temps de déplacement entre les villages.

## Problème similaire
Le problème de graphe qui ressemble le plus à notre problème est le problème du voyageur de commerce, où l'objectif est de trouver le chemin le plus court passant par toutes les villes visitées une seule fois. Dans notre cas, nous avons plusieurs drones et chaque drone doit effectuer une tournée, mais l'idée est similaire en ce sens qu'il faut trouver un chemin qui minimise la distance parcourue par chaque drone.

## Temps d'acheminement

To do

# Partie 2

Dans le code (fichier `graph_encoding.py`).

# Partie 3

To do

# Partie 4

To do

# Rapport

Lien rapport : [rapport.tex](https://www.overleaf.com/2785759683mbxscjmzxbbp "Overleaf").