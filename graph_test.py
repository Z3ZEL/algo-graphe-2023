from graph_encoding import decode_graph_file

graph = decode_graph_file(10, 'world.txt')
graph.print_data()
graph.print_world()
graph.print_vilage_constrains()
# graph.print_adj_matrix()
