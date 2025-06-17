from gv import guardar_grafo
from grafo import Grafo

# Malla
# Generamos grafo de malla con 50 nodos
grafo_malla_50 = Grafo(dirigido=False)
grafo_malla_50.grafo_malla(5, 10)
guardar_grafo(grafo_malla_50, "grafo_malla_50_nodos")
guardar_grafo(grafo_malla_50.Dijkstra("0"),"grafo_malla_50_nodos_Dijkstra")

# Generamos grafo de malla con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
guardar_grafo(grafo_malla_500, "grafo_malla_500_nodos")
guardar_grafo(grafo_malla_500.Dijkstra("1"), "grafo_malla_500_nodos_Dijkstra")


# Erdös y Rényi
# Generamos grafo Erdös y Rényi con 50 nodos y 250 aristas
grafo_erdos_50_250 = Grafo(dirigido=False)
grafo_erdos_50_250.grafo_erdos_renyi(30, 250)
guardar_grafo(grafo_erdos_50_250, "grafo_erdos_50_250")
guardar_grafo(grafo_erdos_50_250.Dijkstra("1"), "grafo_erdos_50_250_Dijkstra")

# Generamos grafo Erdös y Rényi con 500 nodos y 2500 aristas
grafo_erdos_500_2500 = Grafo(dirigido=False)
grafo_erdos_500_2500.grafo_erdos_renyi(500, 2500)
guardar_grafo(grafo_erdos_500_2500, "grafo_erdos_500_2500")
guardar_grafo(grafo_erdos_500_2500.Dijkstra("1"),"grafo_erdos_500_2500_Dijkstra")


# Gilbert
# Generamos grafo con modelo de Gilbert 50 nodos y probabilidad 0.5
grafo_gilbert_50_05 = Grafo(dirigido=False)
grafo_gilbert_50_05.grafo_gilbert(50, 0.5)
guardar_grafo(grafo_gilbert_50_05, "grafo_gilbert_50_05")
guardar_grafo(grafo_gilbert_50_05.Dijkstra("1"),"grafo_gilbert_50_05_Dijkstra")

# Generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.02
grafo_gilbert_500_002 = Grafo(dirigido=False)
grafo_gilbert_500_002.grafo_gilbert(500, 0.02)
guardar_grafo(grafo_gilbert_500_002, "grafo_gilbert_500_002")
guardar_grafo(grafo_gilbert_500_002.Dijkstra("1"),"grafo_gilbert_500_002_Dijkstra")


# Geográfico simple
# Generamos grafo con modelo geográfico simple con 50 nodos y r=0.5
grafo_geografico_50_05 = Grafo(dirigido=False)
grafo_geografico_50_05.grafo_geografico(50, 0.5)
guardar_grafo(grafo_geografico_50_05, "grafo_geografico_50_05")
guardar_grafo(grafo_geografico_50_05.Dijkstra("1"), "grafo_geografico_50_05_Dijkstra")

# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.15)
guardar_grafo(grafo_geografico_500_01, "grafo_geografico_500_01")
guardar_grafo(grafo_geografico_500_01.Dijkstra("1"), "grafo_geografico_500_01_Dijkstra")


# Barabási-Albert
# generamos grafo con modelo Barabási-Albert con 50 nodos y grado 10
grafo_babarasi_50_10 = Grafo(dirigido=False)
grafo_babarasi_50_10.grafo_barabasi_albert(50, 10, False, False)
guardar_grafo(grafo_babarasi_50_10, "grafo_babarasi_50_10")
guardar_grafo(grafo_babarasi_50_10.Dijkstra("1"), "grafo_babarasi_50_10_Dijkstra")

# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 12
grafo_babarasi_500_12 = Grafo(dirigido=False)
grafo_babarasi_500_12.grafo_barabasi_albert(500, 15)
guardar_grafo(grafo_babarasi_500_12, "grafo_babarasi_500_12")
guardar_grafo(grafo_babarasi_500_12.Dijkstra("1"), "grafo_babarasi_500_12_Dijkstra")


# Dorogovtsev-Mendes
# generamos grafo con modelo Dorogovtsev-Mendes con 50 nodos
grafo_dorogovtsev_mendes_50 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_50.dorogovtsev_mendes(50)
guardar_grafo(grafo_dorogovtsev_mendes_50, "grafo_dorogovtsev_mendes_50")
guardar_grafo(grafo_dorogovtsev_mendes_50.Dijkstra("1"), "grafo_dorogovtsev_mendes_50_Dijkstra")

# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")
guardar_grafo(grafo_dorogovtsev_mendes_500.Dijkstra("1"), "grafo_dorogovtsev_mendes_500_Dijkstra")


