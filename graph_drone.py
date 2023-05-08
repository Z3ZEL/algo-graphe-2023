class Graph_drone:

    def __init__(self, N):
        self.num_vertices = N * N
        self.N = N
        self.adj_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        self.__init_adj_matrix()
        self.world = [[0 for _ in range(N)] for _ in range(N)]
        self.villages = {}
        self.villages_constrain = []
        self.drones = []

    def __init_adj_matrix(self):
        for i in range(self.num_vertices):
            if i%self.N != self.N - 1:
                self.adj_matrix[i][i+1] = 1
            if i%self.N != 0:
                self.adj_matrix[i][i-1] = 1
            if i < self.num_vertices - self.N:
                self.adj_matrix[i][i+self.N] = 1
            if i >= self.N:
                self.adj_matrix[i][i-self.N] = 1
            if i < self.num_vertices - self.N and i%self.N != self.N - 1:
                self.adj_matrix[i][i+self.N+1] = 1
            if i < self.num_vertices - self.N and i%self.N != 0:
                self.adj_matrix[i][i+self.N-1] = 1
            if i >= self.N and i%self.N != self.N - 1:
                self.adj_matrix[i][i-self.N+1] = 1
            if i >= self.N and i%self.N != 0:
                self.adj_matrix[i][i-self.N-1] = 1
        

    def pos_to_index(self, x, y):
        return self.N * y + x
    def index_to_pos(self, index):
        return (index%self.N, index//self.N)
    
    def is_wall(self, x, y):
        i = self.pos_to_index(x,y)
        for r in range(self.num_vertices):
            if(self.adj_matrix[i][r] != 0):
                return False
            if(self.adj_matrix[r][i] != 0):
                return False
        return True

    def add_edge(self, v1, v2, weight=1):
        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def get_adjacent_vertices(self, v):
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.adj_matrix[v][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices
    
    def add_wall(self,x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                index = self.pos_to_index(x,y)
                for neigh in self.get_adjacent_vertices(index):
                    self.remove_edge(index,neigh)
    
    def get_edge_weight(self, v1, v2):
        return self.adj_matrix[v1][v2]
    
    def add_village(self, index, x, y):
        self.villages[index] = (x, y)

    def get_village(self, village):
        return self.villages[village]
    
    def get_villages(self):
        return self.villages.keys()
    
    def remove_village(self, village):
        del self.villages[village]

    ###-----CONSTRAINS-----
    def init_village_constrains(self):
        '''Init all vilage constrains, by default everything is set to 1, there is no constrain, all villages can be reached from any village'''
        self.remove_all_village_constrains()
        for i in range(len(self.villages_constrain)):
            for j in  range(len(self.villages_constrain[0])):
                self.villages_constrain[i][j] = 1
    def remove_all_village_constrains(self):
        '''Set village constrains to 0, nothing can be reached'''
        self.villages_constrain = [[0 for _ in range(len(self.villages)+1)] for _ in range(len(self.villages)+1)]
    def add_village_constrain(self, src, dst):
        '''Add a constrain from src to dst, the village dst can be reached from the src village'''
        src -= 1
        dst -= 1
        self.villages_constrain[src][dst] = 1
    def remove_village_constrain(self, src, dst):
        '''Remove a constrain from the src to dst, the village dst can be no longer reachable from the village src'''
        src -= 1
        dst -= 1
        self.villages_constrain[src][dst] = 0
    def can_reach_village(self, src, dst):
        '''Return true if the village dst can be reached from the src village'''
        src -= 1
        dst -= 1
        return self.villages_constrain[src][dst] == 1
    


    ###--------------------

    def add_drone(self, drone):
        self.drones.append(drone)

    def get_drone(self, index):
        return self.drones[index]
    
    def move_drone(self, index, x, y):
        self.drones[index] = (x, y)
    
    def get_drones(self):
        return self.drones
    
    def remove_drone(self, drone):
        del self.drones[drone]

    def drone_to_village_index(self,drone):
        for index in range(1,len(self.villages)+1):
            if(drone == self.villages[index]):
                return index - 1
        return None
    
    def print_world(self):
        print("World :")
        world_string = [[0 for _ in range(self.N)] for _ in range(self.N)]
        for x in range(self.N):
            for y in range(self.N):
                if self.is_wall(x, y):
                    world_string[y][x] = 'X'
                else:
                    world_string[y][x] = '0' 
        for village in self.villages:
            (x, y) = self.villages[village]
            world_string[y][x] = village
        for drone in self.drones:
            (x, y) = drone
            world_string[y][x] = 'D'
        for x in range(self.N):
            for y in range(self.N):
                print(world_string[x][y], end=' ')
            print("- "+str(x))
        for _ in range(self.N):
            print("-", end=' ')
        print()
        for x in range(self.N):
            print(x, end=' ')
        print()

    def print_matrix(matrix):
        '''Print any matrix'''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=' ')
            print()
    def print_adj_matrix(self):
        print("Adjacency Matrix :")
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[0])):
                print(self.adj_matrix[i][j], end=' ')
            print()
    def print_adj_matrix_readable(self):
        '''
        Print the adj matrix with (x,y) coordinates
        '''
        print("Adjacency Matrix :")
        for i in range(len(self.adj_matrix)):
            print(self.index_to_pos(i), end=' : ')
            for j in range(len(self.adj_matrix[0])):
                if self.adj_matrix[i][j] != 0:
                    print(self.index_to_pos(j), end=' ')
            print()
    def print_data(self):
        print("Villages :", self.villages)
        print("Drones :", self.drones)

    def print_vilage_constrains(self):
        print("Village constrains :")
        for i in range(len(self.villages_constrain)):
            for j in range(len(self.villages_constrain[0])):
                if(self.villages_constrain[i][j] == 1):
                    print(str(i) + ' --> ' + str(j))
    def __len__(self):
        return self.num_vertices
    def __str__(self):
        return str(self.adj_matrix)