from graph_encoding import decode_graph_file
import dijkstra as dj

graph = decode_graph_file(10, 'world.txt')
graph.print_data()
graph.print_world()
graph.print_vilage_constrains()

dijkstra = dj.Dijkstra(graph)
print(dijkstra.caculate((0,0)))

# graph.print_adj_matrix()
