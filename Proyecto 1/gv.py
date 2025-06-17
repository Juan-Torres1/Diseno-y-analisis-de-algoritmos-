"""
Se define el metodo para guardar el grafo
mediante la libreria pydot para hacer una traduccion de nuestro grafo a lenguage .dot
y guardamos el archivo en un archivo graphviz(.gv)
"""
import pydot


def guardar_grafo(grafo, nombre_grafo=None):
    if grafo.es_dirigido():
        pydot_graph = pydot.Dot(graph_type="digraph")
    else:
        pydot_graph = pydot.Dot(graph_type="graph", strict=True)

    # Traduccion de los nodos
    for nodo in grafo.get_nodos().values():
        node = pydot.Node(nodo.get_etiqueta())
        pydot_graph.add_node(node)

    # Traduccion de las aristas
    for edge in grafo.get_aristas():
        etiqueta_nodo_fuente = edge.get_nodo_fuente().get_etiqueta()
        etiqueta_nodo_destino = edge.get_nodo_destino().get_etiqueta()

        pydot_edge = pydot.Edge(etiqueta_nodo_fuente, etiqueta_nodo_destino)

        pydot_graph.add_edge(pydot_edge)

    pydot_graph.write_raw(nombre_grafo + ".gv")  # Escribimos el grafo en un archivo .gv