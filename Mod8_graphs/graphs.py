

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = [] ## List of Nodes

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return self.name + str(self.neighbors)

    def __str__(self):
        return self.name + str(self.neighbors)



class Graph:

    def __init__(self):
        self.nodes = [] ## List of nodes

    def add_node(self, node_name: str):
        self.nodes.append(Node(node_name))

    def add_edge(self, src_name: str, dest_name: str):
        source_node, dest_node = None, None
        for node in self.nodes:
            if node.name == src_name:
                source_node = node
            elif node.name == dest_name:
                dest_node = node
            ## TODO: Break if we have already found source and dest nodes

        source_node.add_neighbor(dest_node)

    def __repr__(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.nodes)

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'E')

print(graph)
