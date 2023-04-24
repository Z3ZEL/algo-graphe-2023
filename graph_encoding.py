import graph_drone as G

def decode_graph_file(N, filename):
    with open(filename, 'r') as file:
        graph = G.Graph_drone(N)
        for line in file:
            entity = line.split(':')[0].strip()
            if entity == 'D':
                x, y = map(int, line.split(':')[1].strip()[1:-1].split(','))
                graph.world[x][y] = 'D'
                graph.add_drone((x, y))
            elif entity.isdigit():
                x, y = map(int, line.split(':')[1].strip()[1:-1].split(','))
                graph.world[x][y] = int(entity)
                graph.add_village(int(entity), x, y)
            elif entity == 'X':
                coords_str = line.split(':')[1].strip()
                coords = coords_str.split(';')
                x1, y1 = map(int, coords[0][1:-1].split(','))
                x2, y2 = map(int, coords[1][2:-1].split(','))
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        graph.world[i][j] = 'X'
            elif entity == 'E':
                v1, v2 = map(int, line.split(':')[1].strip()[1:-1].split(','))
                graph.add_edge(v1, v2)
                #! Gerer les poids des aretes
    return graph

graph = decode_graph_file(10, 'world.txt')
graph.print_data()
graph.print_world()
# graph.print_adj_matrix()