from graph_encoding import decode_graph_string
from graph_drone import Graph_drone
from dijkstra import Dijkstra
from math import sqrt
import random

###--------PARAMETERS--------
#TODO: SET PARAMETERS IN COMMAND LINE

N = 100 #NODE NUMBER
V = 3 #VILLAGE NUMBER
K = 2 #DRONE NUMBER

n = int(sqrt(N)) #WORLD SIZE

#RANDOM INSTANCE SEED
random.seed(1)


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



# PRIM ALGORITHM

algo = Dijkstra(graph)

path = algo.caculate(graph.get_drone(0))

print(path)











