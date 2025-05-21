import Algoritmos as a

def main():
    try:

        #Nodo raiz 
        rootNode= 0

        #DijkstraMalla
        #30 Nodos  
        grafogridGraph=a.gridGraph(6, 5, directed=False)  
        dijkstra=grafogridGraph.dijkstra(rootNode)
        grafogridGraph.save_to_graphviz('DijkstraMalla30')
        print("Nodos del grafo:", grafogridGraph.nodes)
        print("Aristas del grafo:", grafogridGraph.edges)   


    except Exception as err:
        print(err)

main()
