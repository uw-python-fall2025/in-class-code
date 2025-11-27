
from heapq import heapify
from functools import total_ordering

@total_ordering
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = [] ## List of tuples: (Node, edge_weight)
        self.visited = False
        self.distance = 0

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f'{self.name}|{self.distance}: {self.neighbors}'
        # return self.name + str(self.neighbors)

    def __str__(self):
        return f'{self.name} | {self.distance}: {self.neighbors}'
        # return self.name + str(self.neighbors)

    def __lt__(self, other):
        return self.distance < other.distance



class Graph:

    def __init__(self):
        self.nodes = [] ## List of nodes

    def add_node(self, node_name: str):
        self.nodes.append(Node(node_name))

    def add_edge(self, src_name: str, dest_name: str, weight = 0):
        source_node, dest_node = None, None
        for node in self.nodes:
            if node.name == src_name:
                source_node = node
            elif node.name == dest_name:
                dest_node = node
            ## TODO: Break if we have already found source and dest nodes

        source_node.add_neighbor((dest_node, weight))

    def bfs(self, source: str):
        source_node = None
        for node in self.nodes:
            node.visited = False
            if node.name == source:
                source_node = node

        queue = []
        queue.append(source_node)

        while len(queue) > 0:
            cur_node = queue.pop(0)
            if cur_node.visited:
                continue
            cur_node.visited = True
            print(f'Visiting node {cur_node.name}')
            for neighbor in cur_node.neighbors:
                if not neighbor.visited:
                    queue.append(neighbor)

    def initialize_sssp(self, source: str):
        for node in self.nodes:
            node.visited = False
            node.distance = 10000 ## Instead of Inf
            if node.name == source:
                node.distance = 0



    def djikstra(self, source: str):
        ## Initialize SSSP
        self.initialize_sssp(source)

        ## Put everything in a priority queue
        heap = []
        heap.extend(self.nodes)
        heapify(heap)

        ## While we have more nodes in the queue:
        ##   Pop a node, relax all the neighbors of the node
        while len(heap) > 0:
            node = heap.pop(0)
            print(f'Visiting node {node.name}')
            ## Relax neighbors
            for neighbor in node.neighbors: ## neighbor is tuple
                print(f'Relaxing neighbor: {neighbor[0]}')
                new_distance = node.distance + neighbor[1]
                if new_distance < neighbor[0].distance:
                    print(f'Updating distance to neighbor: {neighbor[0]} is now {new_distance} but was {neighbor[0].distance}')
                    neighbor[0].distance = new_distance
            heapify(heap)
            ## TODO: print heap here to inspect and understand


    def __repr__(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.nodes)


demo = Graph()
demo.add_node('S')
demo.add_node('A')
demo.add_node('B')
demo.add_node('F')

demo.add_edge('S', 'A', 6)
demo.add_edge('S', 'B', 2)
demo.add_edge('B', 'A', 3)
demo.add_edge('A', 'F', 1)
demo.add_edge('B', 'F', 5)

print(demo)
demo.djikstra('S')

print(demo)




# graph = Graph()
# graph.add_node('A')
# graph.add_node('B')
# graph.add_node('C')
# graph.add_node('D')
# graph.add_node('E')
# graph.add_node('F')
#
# graph.add_edge('A', 'B')
# graph.add_edge('B', 'C')
# graph.add_edge('C', 'E')
# graph.add_edge('A', 'D')
# graph.add_edge('D', 'C')
# graph.add_edge('D', 'E')
#
#
# graph.bfs('A')
#
# # print(graph)
