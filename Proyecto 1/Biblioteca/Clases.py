#Clase Nodo
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}
    
    def add_neighbor(self, neighbor):
        weight = 1
        self.neighbors[neighbor] = weight
    
    def get_neighbors(self):
        """Devuelve los vecinos del nodo."""
        return list(self.neighbors.keys())

    def get_value(self):
        """Devuelve el valor del nodo."""
        return self.value

    def __repr__(self):
        return f"{self.value}"
    
#Clase arista
class Edge:
    def __init__(self, from_node, to_node, weight=1):
        self.from_node = from_node # Nodo origen
        self.to_node = to_node #Nodo destino
        self.weight = weight # Peso de la arista (1)
    
    def get_nodes(self):
        """Devuelve los nodos de la arista."""
        return self.from_node, self.to_node
    
    def get_weight(self):
        """Devuelve el peso de la arista."""
        return self.weight

    def __repr__(self):
        return f"{self.from_node.value} -- {self.to_node.value}"
    
#Clase grafo
class Graph:
    def __init__(self, directed=False):
        self.nodes = {} # Dicionario de nodos
        self.edges = [] # Lista de aristas
        self.directed = directed # Indica si el grafo es dirigido o no

    def add_node(self, value):
        """Agrega un nodo al grafo"""
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]

    def add_edge(self, from_value, to_value, weight=1):
        """Agrega una arista entre dos nodos."""
        # Verificar si los nodos existen
        from_node = self.add_node(from_value)
        to_node = self.add_node(to_value)

        # Crear la arista
        edge = Edge(from_node, to_node, weight)
        
        self.edges.append(edge)

        # Si el grafo no es dirigido, agregar la arista en ambos sentidos
        from_node.add_neighbor(to_node)
        if not self.directed:
            to_node.add_neighbor(from_node)
    
    def get_edges(self):
        """Devuelve todas las aristas del grafo."""
        return self.edges
        
    def get_nodes(self):
        """Devuelve todos los nodos del grafo."""
        return list(self.nodes.values())

    def grade_node(self, value):
        """Devuelve el grado de un nodo."""
        if value in self.nodes:
            return len(self.nodes[value].get_neighbors())
        else:
            print(f"Node {value} does not exist.")
            return 0

    
    def get_neighbors(self, value):
        """Devuelve los vecinos de un nodo."""
        if value in self.nodes:
            return [edge.to_node for edge in self.nodes[value].edges]
        else:
            print(f"Node {value} does not exist.")
            return []
        
    def display(self):
        """Muestra el grafo como lista de adyacencia."""
        for node in self.nodes.values():
            edges = ", ".join([f"({edge.to_node.value}, weight={edge.weight})" for edge in node.edges])
            print(f"{node.value}: {edges}")

    def save_to_graphviz(self, filename):
        """Guarda el grafo en un archivo con formato GraphViz."""
        
        f = open(str(filename+".dot"), "w")
        f.write(str('graph '+filename+'={\n'))
        f.write(";\n".join(str(nodo) for nodo in self.nodes))
        f.write(";\n")
        f.write(";\n".join(str(arista) for arista in self.edges))
        f.write(";\n}")
        f.close()
        print(f"Grafo guardado en {filename}")