import Algoritmos as a 

def main():
    try:

       #Malla
       #30 nodos
       grafogridGraph=a.gridGraph(10, 5, directed=False)
       grafogridGraph.save_to_graphviz('Malla50')
       #200 nodos
       grafogridGraph=a.gridGraph(10, 20, directed=False)
       grafogridGraph.save_to_graphviz('Malla200')
       #500 nodos
       grafogridGraph=a.gridGraph(10, 50, directed=False)
       grafogridGraph.save_to_graphviz('Malla500')

       #Erdos
       #30 nodos
       grafoErdos=a.ErdosRenyiGraph(50, 50, directed=False)
       grafoErdos.save_to_graphviz('Erdos50')
       #200 nodos
       grafoErdos=a.ErdosRenyiGraph(200, 200, directed=False)
       grafoErdos.save_to_graphviz('Erdos200')
       #500 nodos
       grafoErdos=a.ErdosRenyiGraph(500, 500, directed=False)
       grafoErdos.save_to_graphviz('Erdos500')

       #Gilbert
       #30 nodos
       grafoGilbert=a.gilbertGraph(50, 0.02, directed=False)
       grafoGilbert.save_to_graphviz('Gilbert50')
       #200 nodos
       grafoGilbert=a.gilbertGraph(200, 0.01, directed=False)
       grafoGilbert.save_to_graphviz('Gilbert200')
       #500 nodos
       grafoGilbert=a.gilbertGraph(500, 0.01, directed=False)
       grafoGilbert.save_to_graphviz('Gilbert500')

       #Geografico
       #30 nodos
       geographicGraph=a.geographicGraph(50, 0.5, directed=False)
       geographicGraph.save_to_graphviz('Geografico50')
       #200 nodos
       geographicGraph=a.geographicGraph(200, 0.3, directed=False)
       geographicGraph.save_to_graphviz('Geografico200')
       #500 nodos
       geographicGraph=a.geographicGraph(500, 0.1, directed=False)
       geographicGraph.save_to_graphviz('Geografico500')

       #Barabasi
       #30 nodos
       grafoBarabasiAlbert=a.grafoBarabasiAlbert(50, 2, dirigido=False)
       grafoBarabasiAlbert.save_to_graphviz('BarabasiAlbert50')
       #200 nodos
       grafoBarabasiAlbert=a.grafoBarabasiAlbert(200, 3, dirigido=False)
       grafoBarabasiAlbert.save_to_graphviz('BarabasiAlbert200')
       #500 nodos
       grafoBarabasiAlbert=a.grafoBarabasiAlbert(500, 5, dirigido=False)
       grafoBarabasiAlbert.save_to_graphviz('BarabasiAlbert500')

       #Dorogovtsev
       #30 nodos
       grafoDorogovtsevMendes=a.grafoDorogovtsevMendes(n=50, dirigido=False)
       grafoDorogovtsevMendes.save_to_graphviz('DorogovtsevMendes50')
       #200 nodos
       grafoDorogovtsevMendes=a.grafoDorogovtsevMendes(n=200, dirigido=False)
       grafoDorogovtsevMendes.save_to_graphviz('DorogovtsevMendes200')
       #500 nodos
       grafoDorogovtsevMendes=a.grafoDorogovtsevMendes(n=500, dirigido=False)
       grafoDorogovtsevMendes.save_to_graphviz('DorogovtsevMendes500')

    except Exception as err:
        print(err)

main()

