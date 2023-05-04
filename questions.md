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
Dans le cas d'une clique de N sommets avec un poids unitaire pour les arêtes, le temps optimal d'acheminement d'un message d'une source quelconque à une destination arbitraire est égal au nombre d'arête minimal séparant les deux sommets et permettant aux drones de se transmettre le message.

Dans le cas où les poids sont hétérogènes, un algorithme simple pour calculer K tournées est le suivant: 
Ach_Mess(G: graphe, s: arête, d: arête, K: tournée): entier
    entier t = 0;
    acc = s
    Som_vis = construcTab(0, 2);
    Arc_vis = construcTab(0, 2);
    pro = sommet_suiv_poids_min(G, s);
    pour i allant de 1 à K:
        si (est_rempli(Som_vis)):
            Som_vis = augmenter(Som_vis);
        si (est_rempli(Arc_vis)):
            Arc_vis = augmenter(Arc_vis); 
        t += poids_arc(G, acc, pro);
        acc = pro
        pro = sommet_suiv_poids_min(G, acc);
    retourner t;
Cet algorithme prend en paramètre un graphe G, le sommet source s, le sommet de destination d, et le nombre de tournée K. Le principe est le suivant: on parcourt le graphe en passant à chaque fois par l'arc possèdant le poids le plus faible en retenant dans un tableau le nom de l'arc emprunté et du sommet visité afin de visité chaque arc et chaque sommet une seule fois lors d'une tournée afin de récupérer et transmettre les messages de la tournée en cours, puis on somme les poids des arcs visités afin d'obtenir le temps d'acheminement. Cet algorithme ne prend pas en compte les changements de drones, pour inclure les changements de drones, on peut penser que chaque drones dépose ses messages à transmettre à chaque points où il doit le faire et sait quand il doit reprendre un message à un point donné. Ainsi, lorsqu'un drone doit récupérer quelque chose à un point il le fait lors de son passage.
Le temps T de notre algorithme est O(T) = K*n*m avec n : le nombre de sommets et m: le nombre d'arêtes

# Partie 2

Dans le code (fichier `graph_encoding.py`).

# Partie 3

To do

# Partie 4

To do

# Rapport

Lien rapport : [rapport.tex](https://www.overleaf.com/2785759683mbxscjmzxbbp "Overleaf").