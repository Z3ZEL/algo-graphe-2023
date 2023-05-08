from graph_encoding import decode_graph_string
from graph_drone import Graph_drone
from dijkstra import Dijkstra
from math import sqrt
import subprocess
import random

###--------PARAMETERS--------
#TODO: SET PARAMETERS IN COMMAND LINE

N = 100 #NODE NUMBER
V = 5 #VILLAGE NUMBER
K = 2 #DRONE NUMBER

n = int(sqrt(N)) #WORLD SIZE

#RANDOM INSTANCE SEED
random.seed(1)


#GENERATE RANDOM VILLAGE 

world_string = ''

for v in range(V):
    (x, y) = (random.randint(0,n-1), random.randint(0,n-1))
    world_string += str(v+1)+': (' +str(x)+','+str(y)+')\n'
    if v < K:
        world_string += 'D: '+'(' +str(x)+','+str(y)+')\n'


    
graph = decode_graph_string(n, world_string)

graph.print_world()
graph.print_data()



# DIJKSTRA ALGORITHM

algo = Dijkstra(graph)


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
        subprocess.run([f'circo -Tpng {filename} -o {filename}.png'], shell=True)

create_dot_file(village_graph, 'village_graph.dot')


def closest_drone_to(drones, village ,village_graph):
    min = 1000000000
    index = -1
    for drone in drones:
        if village_graph[village][drone] <= min:
            min = village_graph[village][drone]
            index = drone
    return(min,index)

def closest_village_to(villages, drone ,village_graph):
    min = 1000000000
    index = -1
    for village in villages:
        if village_graph[drone][village] <= min:
            min = village_graph[drone][village]
            index = village
    return(min,index)

def village_order_1(graph,village_graph):                                               #First idea : for each village get the closest drone 
    t_loss = 0
    drones = list(map(graph.drone_to_village_index,graph.drones))
    already_seen = drones
    villages = [ i for i in range(len(graph.villages)) ]
    while( len(already_seen) != len(villages)):
        for village in villages :   
            if village not in already_seen: 
                (t_min,index_drone) = closest_drone_to(drones,village,village_graph)        #get the idnex of the closest drone to the village
                print(village, (t_min,index_drone))
                t_loss+=t_min                                                             
                drones[index_drone] = village                                               #move the drone to its new location 
                already_seen.append(village)

    return t_loss

print(village_order_1(graph,village_graph))

def village_order_2(graph,village_graph):                                               #Second idea : for each drone move it to the closest village 
    t_loss = 0
    drones = list(map(graph.drone_to_village_index,graph.drones))
    already_seen = drones.copy()
    villages = []
    for i in range(len(village_graph)):
        if i not in already_seen:
            villages.append(i)
    while(len(villages) > 0):
        t_tot = []  
        for drone_index in range(len(drones)) :
            if(len(villages) ==0):
                break
            (t_min,village_index) = closest_village_to(villages,drones[drone_index],village_graph)
            print(drones[drone_index] ,(t_min,village_index))
            drones[drone_index] = village_index                                               #move the drone to its new location 
            already_seen.append(village_index)
            villages.remove(village_index)
            t_tot.append(t_min)
        t_loss += max(t_tot)
        
    return t_loss

print(village_order_2(graph,village_graph))
