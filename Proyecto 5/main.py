from gv import guardar_grafo
from grafo import Grafo

# Mallas
# Generamos grafo de mallas con 100 nodos
#grafo_malla_100 = Grafo(dirigido=False)
#grafo_malla_100.grafo_malla(5, 10)
#grafo_malla_100.layout()
#guardar_grafo(grafo_malla_100, "grafo_malla_100_nodos")

# Generamos grafo de mallas con 500 nodos
#grafo_malla_500 = Grafo(dirigido=False)
#grafo_malla_500.grafo_malla(50, 10)
#grafo_malla_500.layout()
#guardar_grafo(grafo_malla_500, "grafo_malla_500_nodos")


# Erdös y Rényi
# Generamos grafo Erdös y Rényi con 100 nodos y 600 aristas
#grafo_erdos_100_600 = Grafo(dirigido=False)
#grafo_erdos_100_600.grafo_erdos_renyi(100, 600)
#grafo_erdos_100_600.layout()
#guardar_grafo(grafo_erdos_100_600, "grafo_erdos_100_600")

# Generamos grafo Erdös y Rényi con 500 nodos y 2500 aristas
#grafo_erdos_500_2500 = Grafo(dirigido=False)
#grafo_erdos_500_2500.grafo_erdos_renyi(500, 2500)
#grafo_erdos_500_2500.layout()
#guardar_grafo(grafo_erdos_500_2500, "grafo_erdos_500_2500")


# Gilbert
# generamos grafo con modelo de Gilbert 100 nodos y probabilidad 0.5
#grafo_gilbert_100_05 = Grafo(dirigido=False)
#grafo_gilbert_100_05.grafo_gilbert(100, 0.5)
#grafo_gilbert_100_05.layout()
#guardar_grafo(grafo_gilbert_100_05, "grafo_gilbert_100_05")

# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.02
#grafo_gilbert_500_002 = Grafo(dirigido=False)
#grafo_gilbert_500_002.grafo_gilbert(500, 0.02)
#grafo_gilbert_500_002.layout()
#guardar_grafo(grafo_gilbert_500_002, "grafo_gilbert_500_002")


# Geográfico simple
# generamos grafo con modelo geográfico simple con 100 nodos y r=0.5
#grafo_geografico_100_05 = Grafo(dirigido=False)
#grafo_geografico_100_05.grafo_geografico(100, 0.5)
#grafo_geografico_100_05.layout()
#guardar_grafo(grafo_geografico_100_05, "grafo_geografico_100_05")

# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
#grafo_geografico_500_01 = Grafo(dirigido=False)
#grafo_geografico_500_01.grafo_geografico(500, 0.15)
#grafo_geografico_500_01.layout()
#guardar_grafo(grafo_geografico_500_01, "grafo_geografico_500_01")


# Barabási-Albert
# generamos grafo con modelo Barabási-Albert con 100 nodos y grado 10
#grafo_babarasi_100_10 = Grafo(dirigido=False)
#grafo_babarasi_100_10.grafo_barabasi_albert(100, 10, False, False)
#grafo_babarasi_100_10.layout()
#guardar_grafo(grafo_babarasi_100_10, "grafo_babarasi_100_10")

# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 12
#grafo_babarasi_500_12 = Grafo(dirigido=False)
#grafo_babarasi_500_12.grafo_barabasi_albert(500, 15)
#grafo_babarasi_500_12.layout()
#guardar_grafo(grafo_babarasi_500_12, "grafo_babarasi_500_12")


# Dorogovtsev-Mendes
# generamos grafo con modelo Dorogovtsev-Mendes con 100 nodos
#grafo_dorogovtsev_mendes_100 = Grafo(dirigido=False)
#grafo_dorogovtsev_mendes_100.dorogovtsev_mendes(100)
#grafo_dorogovtsev_mendes_100.layout()
#guardar_grafo(grafo_dorogovtsev_mendes_100, "grafo_dorogovtsev_mendes_100")

# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
grafo_dorogovtsev_mendes_500.layout()
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")
