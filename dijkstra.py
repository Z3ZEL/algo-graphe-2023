from graph_drone import Graph_drone

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph


    def get_adjacent_vertices(self, v):
        adjacent_vertices = []
        for i in range(self.graph.num_vertices):
            if self.graph.adj_matrix[v][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_next_vertex(self, distance, visited, start_index):
        vertices = self.get_adjacent_vertices(start_index)
        print(vertices)
        min_distance = -1
        min_index = -1
        for i in vertices:
            if not visited[i] and (min_distance == -1 or distance[i] < min_distance):
                min_distance = distance[i]
                min_index = i
        return min_index




    def caculate(self, start_pos):
        #init map at -1
        map = [[-1 for _ in range(self.graph.num_vertices)] for _ in range(self.graph.num_vertices)]
        #init distance at -1
        distance = [-1 for _ in range(self.graph.num_vertices)]
        #init visited at False
        visited = [False for _ in range(self.graph.num_vertices)]

        #init start position

        start_index = self.graph.pos_to_index(start_pos[0], start_pos[1])
        print(start_index)

        distance[start_index] = 0  #set distance to 0
        visited[start_index] = True  #set visited to True



        #set map to start index
        map[start_pos[0]][start_pos[1]] = 0 #DISTANCE FROM START TO START IS 0

        current = start_index
        while True:
            adjacent_vertices = self.get_adjacent_vertices(start_index)
            for i in adjacent_vertices:
                if not visited[i]:
                    if distance[i] == -1 or distance[i] > distance[current] + self.graph.adj_matrix[current][i]:
                        distance[i] = distance[current] + self.graph.adj_matrix[current][i]
                    
            visited[current] = True
            current = self.get_next_vertex(distance, visited, start_index)
            

        
        for i in range(self.graph.num_vertices):
            (x,y) = self.graph.index_to_pos(i)
            map[x][y] = distance[i]
        return map


            
            



        


