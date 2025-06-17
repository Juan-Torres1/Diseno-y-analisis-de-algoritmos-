"""
Aqui se define el metodo para guardar el grafo
Se hace uso de la libreria pydot para hacer una traduccion 
del grafo a lenguage .dot y se guarda el archivo en un archivo graphviz(.gv)
"""
import pydot
import os
import tempfile
from PIL import Image

def guardar_grafo(grafo, nombre_grafo=None):
    if grafo.es_dirigido():
        pydot_graph = pydot.Dot(graph_type="digraph")
    else:
        pydot_graph = pydot.Dot(graph_type="graph", strict=True)

    # Traduccion de los nodos
    for nodo in grafo.get_nodos().values():
        if nodo.get_distancia() != 0:
            node = pydot.Node(nodo.get_etiqueta(),
                              label="{} ({})".format(nodo.get_etiqueta(), str(nodo.get_distancia())))
        else:
            node = pydot.Node(nodo.get_etiqueta())
        pydot_graph.add_node(node)

    # Traduccion de las aristas
    for edge in grafo.get_aristas():
        etiqueta_nodo_fuente = edge.get_nodo_fuente().get_etiqueta()
        etiqueta_nodo_destino = edge.get_nodo_destino().get_etiqueta()
        peso = str(edge.get_peso())
        pydot_edge = pydot.Edge(etiqueta_nodo_fuente, etiqueta_nodo_destino)
        pydot_edge.set_label(peso)
        pydot_graph.add_edge(pydot_edge)

    pydot_graph.write_raw(nombre_grafo + ".gv")  # Escribimos el grafo en un archivo .gv
def mostrar_grafo(grafo):
    if grafo.es_dirigido():
        pydot_graph = pydot.Dot(graph_type="digraph")
    else:
        pydot_graph = pydot.Dot(graph_type="graph", strict=True)

    # Traduccion de los nodos
    for nodo in grafo.get_nodos().values():

        if nodo.get_distancia()!=0:
            node = pydot.Node(nodo.get_etiqueta(), label="{} ({})".format(nodo.get_etiqueta(),str(nodo.get_distancia())))
        else:
            node = pydot.Node(nodo.get_etiqueta())
        pydot_graph.add_node(node)

    # Traduccion de las aristas
    for edge in grafo.get_aristas():
        etiqueta_nodo_fuente = edge.get_nodo_fuente().get_etiqueta()
        etiqueta_nodo_destino = edge.get_nodo_destino().get_etiqueta()
        peso = str(edge.get_peso())
        pydot_edge = pydot.Edge(etiqueta_nodo_fuente, etiqueta_nodo_destino)
        pydot_edge.set_label(peso)
        pydot_graph.add_edge(pydot_edge)
    temp = tempfile.NamedTemporaryFile(delete=False)
    pydot_graph.write_png(temp.name)

    image = Image.open(temp.name)
    temp.close()

    image.show()
    os.unlink(temp.name)