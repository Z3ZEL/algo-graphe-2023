from graph_drone import Graph_drone
import math as m;

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph


    def get_adjacent_vertices(self, v):
        adjacent_vertices = []
        for i in range(len(self.graph.adj_matrix[v])):
            if self.graph.adj_matrix[v][i] != 0:
                adjacent_vertices.append(i)
        return adjacent_vertices
    def get_next_vertex(self,Q, distance):
        min = m.inf
        min_index = -1
        for i in range(len(Q)):
            if distance[Q[i]] < min:
                min = distance[Q[i]]
                min_index = i
        return Q[min_index]
        




    def caculate(self, start_pos):
        #init distance at inf
        distance = [m.inf for _ in range(self.graph.num_vertices)]
        #init visited at False
        Q = [ i for i in range(self.graph.num_vertices)]

        #init start position

        start_index = self.graph.pos_to_index(start_pos[0], start_pos[1])
        distance[start_index] = 0  #set distance to 0
        current = start_index

        #DIJKSTRA ALGORITHM
        while len(Q) != 0:
            #get adjacent vertices
            current = self.get_next_vertex(Q, distance)
            Q.remove(current)
            #update distance
            for i in self.get_adjacent_vertices(current):
                if distance[i] > distance[current] + self.graph.adj_matrix[current][i]:
                    distance[i] = distance[current] + self.graph.adj_matrix[current][i]
        #replace inf by -1
        for i in range(len(distance)):
            if distance[i] == m.inf:
                distance[i] = -1
        return distance


            
            



        


