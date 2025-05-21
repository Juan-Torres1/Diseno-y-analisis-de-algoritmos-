import heapq
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
        f.write(";\n".join(str(node) for node in self.nodes))
        f.write(";\n")
        f.write(";\n".join(str(arista) for arista in self.edges))
        f.write(";\n}")
        f.close()
        print(f"Grafo guardado en {filename}")

#Proyecto 2 (Algoritmos BFS, DFS iterativo y recursivo)
        
        """Realiza una búsqueda en anchura (BFS) desde un nodo inicial."""
    def bfs(self, start_value):

        if start_value not in self.nodes:
            print(f"Node {start_value} does not exist.")
            return []

        visited = set()
        queue = [self.nodes[start_value]]
        bfs_order = []

        while queue:
            current_node = queue.pop(0)
            if current_node.value not in visited:
                visited.add(current_node.value)
                bfs_order.append(current_node.value)
                queue.extend(current_node.get_neighbors())

        return bfs_order

        """Realiza una búsqueda en profundidad (DFS) iterativa desde un nodo inicial."""
    def dfs_iterative(self, start_value):
        if start_value not in self.nodes:
            print(f"Node {start_value} does not exist.")
            return []

        visited = set()
        stack = [self.nodes[start_value]]
        dfs_order = []

        while stack:
            current_node = stack.pop()
            if current_node.value not in visited:
                visited.add(current_node.value)
                dfs_order.append(current_node.value)
                stack.extend(current_node.get_neighbors())

        return dfs_order

        """Realiza una búsqueda en profundidad (DFS) recursiva desde un nodo inicial."""
    def dfs_recursive(self, start_value, visited=None):
        if visited is None:
            visited = set()
        if start_value not in self.nodes:
            print(f"Node {start_value} does not exist.")
            return []

        visited.add(start_value)
        dfs_order = [start_value]

        for neighbor in self.nodes[start_value].get_neighbors():
            if neighbor.value not in visited:
                dfs_order.extend(self.dfs_recursive(neighbor.value, visited))

        return dfs_order

#Proyecto 3 (Algoritmo de Dijkstra)

    def dijkstra(self, start_value):
        if start_value not in self.nodes:
            print(f"Nodo {start_value} no existente.")
            return {}

        # Inicialización
        start_node = self.nodes[start_value]
        distances = {node: float('inf') for node in self.nodes.values()}
        distances[start_node] = 0
        visited = set()
        heap = [(0, start_node)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor in current_node.get_neighbors():
                # Buscar el peso real de la arista
                weight = 1
                for edge in self.edges:
                    if edge.from_node == current_node and edge.to_node == neighbor:
                        weight = edge.weight
                        break
                    if not self.directed and edge.from_node == neighbor and edge.to_node == current_node:
                        weight = edge.weight
                        break

                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        # Formatear los nombres de los nodos con la distancia
        result = {}
        for node, dist in distances.items():
            if dist < float('inf'):
                result[node.value] = dist
            else:
                result[node.value] = float('inf')
        return result
    