import Algoritmos as a

def main():
    try:

        #Nodo raiz para algoritmos BFS, DFS Interativo y DFS Recirsivo
        rootNode='0:0'
        #Malla

        #30 Nodos  
        grafogridGraph=a.gridGraph(6, 5, directed=False)
        grafogridGraph.save_to_graphviz('Malla30')
        grafogridGraphBFS=grafogridGraph.bfs(rootNode)
        grafogridGraph.save_to_graphviz('Malla30bfs')
        grafogridGraphBFS=grafogridGraph.dfs_iterative(rootNode)
        grafogridGraph.save_to_graphviz('Malla30dfs_iterativo')
        grafogridGraphBFS=grafogridGraph.dfs_recursive(rootNode)
        grafogridGraph.save_to_graphviz('Malla30dfs_recursivo')
        print("Nodos del grafo:", grafogridGraph.nodes)
        #100 Nodos
        grafogridGraph=a.gridGraph(10, 10, directed=False)
        grafogridGraph.save_to_graphviz('Malla100')
        grafogridGraphBFS=grafogridGraph.bfs(rootNode)
        grafogridGraph.save_to_graphviz('Malla100bfs')
        grafogridGraphBFS=grafogridGraph.dfs_iterative(rootNode)
        grafogridGraph.save_to_graphviz('Malla100dfs_iterativo')
        grafogridGraphBFS=grafogridGraph.dfs_recursive(rootNode)
        grafogridGraph.save_to_graphviz('Malla100dfs_recursivo')
        print("Nodos del grafo:", grafogridGraph.nodes)
        #500 nodos
        grafogridGraph=a.gridGraph(50, 10, directed=False)
        grafogridGraph.save_to_graphviz('Malla500')
        grafogridGraphBFS=grafogridGraph.bfs(rootNode)
        grafogridGraph.save_to_graphviz('Malla500bfs')
        grafogridGraphBFS=grafogridGraph.dfs_iterative(rootNode)
        grafogridGraph.save_to_graphviz('Malla500dfs_iterativo')
        grafogridGraphBFS=grafogridGraph.dfs_recursive(rootNode)
        grafogridGraph.save_to_graphviz('Malla500dfs_recursivo')
        print("Nodos del grafo:", grafogridGraph.nodes)

    except Exception as err:
        print(err)

main()
