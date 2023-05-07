from graph_encoding import decode_graph_string
from graph_drone import Graph_drone
from dijkstra import Dijkstra
from math import sqrt
import subprocess
import random

###--------PARAMETERS--------
#TODO: SET PARAMETERS IN COMMAND LINE

N = 25 #NODE NUMBER
V = 3 #VILLAGE NUMBER
K = 2 #DRONE NUMBER

n = int(sqrt(N)) #WORLD SIZE

#RANDOM INSTANCE SEED
random.seed(3)


#GENERATE RANDOM VILLAGE 

world_string = ''

for v in range(V):
    (x, y) = (random.randint(0,n-1), random.randint(0,n-1))
    world_string += str(v+1)+': (' +str(x)+','+str(y)+')\n'
    if v < K-1:
        world_string += 'D: '+'(' +str(x)+','+str(y)+')\n'


    
graph = decode_graph_string(n, world_string)

graph.print_world()
graph.print_data()



# DIJKSTRA ALGORITHM

algo = Dijkstra(graph)

print("Distance map pour chaque villlage (DEBUG)")
for i in range (1,V+1):
    distance = algo.caculate(graph.get_village(i))
    for j in range(len(distance)):
        if j % n == 0:
            print()
        print(distance[j], end=' ')
    print()
    print(graph.get_village(i))

#VILLAGE GRAPH

village_graph = [[0 for _ in range(V)] for _ in range(V)]

for i in range(V):
    distance = algo.caculate(graph.get_village(i + 1))
    for j in range(V):
        if i != j:
            village_coord = graph.get_village(j + 1)
            idx = village_coord[1] * n + village_coord[0]
            village_graph[i][j] = distance[idx]

print("Village Adj Graph :")
for i in range(len(village_graph)):
    for j in range(len(village_graph[0])):
        print(village_graph[i][j], end=' ')
    print()

def create_dot_file(adj_matrix, filename):
    with open(filename, 'w') as file:
        # Write the header of the DOT file
        file.write("graph {\n")
        # Loop through all the vertices
        for i in range(len(adj_matrix)):
            # Loop through all the adjacent vertices
            for j in range(i, len(adj_matrix[i])):
                # If there is an edge between i and j, add it to the DOT file
                if adj_matrix[i][j] > 0 and i != j:
                    file.write(f"    {i+1} -- {j+1} [label=\"{adj_matrix[i][j]}\"];\n")
        # Write the footer of the DOT file
        file.write("}")
        subprocess.run([f'dot -Tpng {filename} -o {filename}.png'], shell=True)

create_dot_file(village_graph, 'village_graph.dot')
