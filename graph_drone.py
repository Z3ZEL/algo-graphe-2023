class Graph_drone:
    def __init__(self, N):
        self.num_vertices = N * N
        self.adj_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        self.world = [[0 for _ in range(N)] for _ in range(N)]
        self.villages = {}
        self.drones = []

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

    def get_edge_weight(self, v1, v2):
        return self.adj_matrix[v1][v2]
    
    def add_village(self, village, x, y):
        self.villages[village] = (x, y)

    def get_village(self, village):
        return self.villages[village]
    
    def get_villages(self):
        return self.villages.keys()
    
    def remove_village(self, village):
        del self.villages[village]

    def add_drone(self, drone):
        self.drones.append(drone)

    def get_drone(self, drone):
        return self.drones[drone]
    
    def get_drones(self):
        return self.drones
    
    def remove_drone(self, drone):
        del self.drones[drone]

    def print_world(self):
        print("World :")
        for i in range(len(self.world)):
            for j in range(len(self.world[0])):
                print(self.world[i][j], end=' ')
            print()

    def print_data(self):
        print("Villages :", self.villages)
        print("Drones :", self.drones)

    def __len__(self):
        return self.num_vertices

    def __str__(self):
        return str(self.adj_matrix)