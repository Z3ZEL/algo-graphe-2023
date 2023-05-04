from graph_encoding import decode_graph_string
from graph_drone import Graph_drone
import random

###--------PARAMETERS--------
#TODO: SET PARAMETERS IN COMMAND LINE

N = 10 #WORLD SIZE
village_number = 3


#GENERATE RANDOM VILLAGE 

world_string = ''

for x in range(village_number):
    (x, y) = (random.randint(0,N-1), random.randint(0,N-1))
    world_string += str(x+1)+': (' +str(x)+','+str(y)+')\n'
    world_string += 'D: '+'(' +str(x)+','+str(y)+')\n'
    
graph = decode_graph_string(N, world_string)

graph.print_world()
graph.print_data()
    









