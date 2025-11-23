from graph import Graph

myGraph = Graph()
myGraph.add_vertex("A")
myGraph.add_vertex("B")
myGraph.add_vertex("C")
myGraph.add_vertex("D")
print("Add Vertex")
myGraph.print_graph()

myGraph.add_edge('A','B')
myGraph.add_edge('C','A')
myGraph.add_edge('B','D')
myGraph.add_edge('A','D')
myGraph.add_edge('C','D')

print("Add edge")
myGraph.print_graph()
print("Remove D")
myGraph.remove_edge('A','D')
myGraph.print_graph()
