from Clases import Graph 
from random import seed
from random import randint 
from random import random 


#Genera grafo de malla
def gridGraph(m, n, directed=False):

    graph = Graph(directed=directed)
    
    # Crear nodos
    for i in range(m):
        for j in range(n):
            graph.add_node(f"{i}:{j}")
            
    
    # Crear aristas
    for i in range(m):
        for j in range(n):
            if i < m:  # Conectar con el nodo de abajo
                graph.add_edge((f"{i}:{j}"), (f"{i + 1}:{j}"))
            if j < n:  # Conectar con el nodo de la derecha
                graph.add_edge((f"{i}:{j}"), (f"{i}:{j + 1}"))
    
    return graph

#Genera un grado de Erdos-Renyi
from random import sample

# Genera un grafo de Erdös y Rényi (Gn,m)
def ErdosRenyiGraph(n, m, directed=False):
    graph = Graph(directed=directed)
    
    # Crear nodos
    for i in range(n):
        graph.add_node(i)
    
    # Generar todas las posibles aristas entre pares de nodos
    possible_edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    
    # Seleccionar m aristas al azar
    if m > len(possible_edges):
        raise ValueError("El número de aristas m excede el número posible de aristas.")
    
    selected_edges = sample(possible_edges, m)
    
    # Agregar las aristas seleccionadas al grafo
    for edge in selected_edges:
        edge_from, edge_to = edge
        graph.add_edge(edge_from, edge_to)
        
    
    return graph

#Genera grafo de Gilbert
def gilbertGraph(n, p, directed=False):
    
    graph = Graph(directed=directed)
    
    # Crear nodos
    for i in range(n):
        graph.add_node(i)
    
    # Crear aristas con probabilidad p
    for i in range(n):
        for j in range(n):
            if i != j:  # Evitar bucles
                if random() < p:  # Conectar con probabilidad p
                    graph.add_edge(i, j)
    
    return graph

#Genera grafo Geográfico simple
from math import sqrt

def geographicGraph(n, r, directed=False):
    graph = Graph(directed=directed)
    positions = {}

    # Crear nodos con posiciones aleatorias
    for i in range(n):
        x, y = random(), random()  # Coordenadas aleatorias en [0, 1]
        graph.add_node(i)
        positions[i] = (x, y)

    # Crear aristas si la distancia entre nodos es menor o igual a r
    for i in range(n):
        for j in range(n):
            if i != j:  # Evitar bucles
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if distance <= r:
                    graph.add_edge(i, j)

    return graph

#Genera variante del modelo Barabási-Albert
def grafoBarabasiAlbert(n, d, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabási-Albert.
    
    Args:
        n (int): Número de nodos (> 0).
        d (int): Número de aristas que cada nodo nuevo intentará crear (> 1).
        dirigido (bool): Si el grafo es dirigido o no.
    
    Returns:
        Graph: Objeto grafo generado.
    """
    if n <= 0 or d < 1:
        raise ValueError("El número de nodos debe ser mayor a 0 y d debe ser al menos 1.")
    if d >= n:
        raise ValueError("d debe ser menor que n para que el modelo sea válido.")

    graph = Graph(directed=dirigido)
    
    
    # Agregar los nodos restantes
    for new_node in range(n):
        graph.add_node(new_node)
        # Calcular la probabilidad de conexión basada en el grado de los nodos existentes
        existing_nodes = graph.get_nodes()
        # Seleccionar d nodos para conectar, proporcional al grado
        for node in existing_nodes:
            proba= (1-(graph.grade_node(node.get_value()) / d))
            if random() < proba:
                graph.add_edge(new_node, node.get_value())
        
    return graph

#Generar grafo del Modelo Dorogovtsev-Mendes
def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera un grafo aleatorio con el modelo Dorogovtsev-Mendes.
    
    Args:
        n (int): Número de nodos (≥ 3).
        dirigido (bool): Si el grafo es dirigido o no.
    
    Returns:
        Graph: Objeto grafo generado.
    """
    if n < 3:
        raise ValueError("El número de nodos debe ser al menos 3.")

    graph = Graph(directed=dirigido)
    
    # Crear los 3 nodos iniciales y conectarlos formando un triángulo
    for i in range(3):
        graph.add_node(i)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    if dirigido:
        graph.add_edge(1, 0)
        graph.add_edge(2, 1)
        graph.add_edge(0, 2)
    
    # Agregar los nodos restantes
    for new_node in range(3, n):
        graph.add_node(new_node)
        
        # Seleccionar una arista al azar
        edges = graph.get_edges()
        selected_edge = edges[randint(0, len(edges) - 1)]
        
        # Conectar el nuevo nodo a los extremos de la arista seleccionada
        u, v = selected_edge.get_nodes()
        graph.add_edge(new_node, u)
        graph.add_edge(new_node, v)
        if  dirigido:
            graph.add_edge(u, new_node)
            graph.add_edge(v, new_node)
    
    return graph

