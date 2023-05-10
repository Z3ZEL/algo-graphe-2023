import graph_drone as G

def decode_graph_line(graph, village_constrains, line):
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
        graph.add_wall(x1,y1,x2,y2)

        ##
        for j in range(x1, x2 + 1):
            for i in range(y1, y2 + 1):
                graph.world[i][j] = 'X'
    elif entity == 'E':
        #Check if there is a 'R' in constrain and replace it by -1
        line = line.replace('R', '0')

        v1, v2 = map(int, line.split(':')[1].strip()[1:-1].split(','))
        village_constrains.append((v1,v2))

def make_constrains(graph, village_constrains):
    #Check if world definition contains constrains, if not, init no constrains
    #WIP
    graph.init_village_constrains()
    if(len(village_constrains) != 0):
        graph.remove_all_village_constrains()
        for constrain in village_constrains:
            (v1,v2) = constrain
            graph.add_village_constrain(v1+1, v2+1)

def decode_graph_file(N, filename):
    with open(filename, 'r') as file:
        graph = G.Graph_drone(N)

        village_constrains = []

        for line in file:   
            decode_graph_line(graph, village_constrains, line)

        make_constrains(graph, village_constrains)
        return graph


def decode_graph_string(N, strings):
    strings = strings.split('\n')
    graph = G.Graph_drone(N)
    village_constrains = []
    for line in strings:
        decode_graph_line(graph, village_constrains, line)
    make_constrains(graph, village_constrains)
    return graph