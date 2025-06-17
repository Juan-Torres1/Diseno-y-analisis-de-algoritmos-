from gv import guardar_grafo
from grafo import Grafo

# Malla
# Generamos grafo de mallas con 50 nodos
grafo_malla_50 = Grafo(dirigido=False)
grafo_malla_50.grafo_malla(5, 10)
guardar_grafo(grafo_malla_50, "grafo_malla_50_nodos")
# Generamos grafo de mallas con 200 nodos
grafo_malla_200 = Grafo(dirigido=False)
grafo_malla_200.grafo_malla(10, 20)
guardar_grafo(grafo_malla_200, "grafo_malla_200_nodos")
# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
guardar_grafo(grafo_malla_500, "grafo_malla_500_nodos")

# Erdös y Rényi
# Generamos grafo Erdös y Rényi con 50 nodos y 200 aristas
grafo_erdos_50_200 = Grafo(dirigido=False)
grafo_erdos_50_200.grafo_erdos_renyi(50, 200)
guardar_grafo(grafo_erdos_50_200, "grafo_erdos_50_200")
# Generamos grafo Erdös y Rényi con 200 nodos y 800 aristas
grafo_erdos_200_800 = Grafo(dirigido=False)
grafo_erdos_200_800.grafo_erdos_renyi(200, 800)
guardar_grafo(grafo_erdos_200_800, "grafo_erdos_200_800")
# Generamos grafo Erdös y Rényi con 500 nodos y 2500 aristas
grafo_erdos_500_2500 = Grafo(dirigido=False)
grafo_erdos_500_2500.grafo_erdos_renyi(500, 2500)
guardar_grafo(grafo_erdos_500_2500, "grafo_erdos_500_2500")

# Gilbert
# generamos grafo con modelo de Gilbert 50 nodos y probabilidad 0.5
grafo_gilbert_50_05 = Grafo(dirigido=False)
grafo_gilbert_50_05.grafo_gilbert(50, 0.5)
guardar_grafo(grafo_gilbert_50_05, "grafo_gilbert_50_05")
# generamos grafo con modelo de Gilbert 200 nodos y probabilidad 0.3
grafo_gilbert_200_03 = Grafo(dirigido=False)
grafo_gilbert_200_03.grafo_gilbert(200, 0.3)
guardar_grafo(grafo_gilbert_200_03, "grafo_gilbert_200_03")
# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.02
grafo_gilbert_500_002 = Grafo(dirigido=False)
grafo_gilbert_500_002.grafo_gilbert(500, 0.02)
guardar_grafo(grafo_gilbert_500_002, "grafo_gilbert_500_002")

# Geográfico simple
# generamos grafo con modelo geográfico simple con 50 nodos y r=0.5
grafo_geografico_50_05 = Grafo(dirigido=False)
grafo_geografico_50_05.grafo_geografico(50, 0.5)
guardar_grafo(grafo_geografico_50_05, "grafo_geografico_50_05")
# generamos grafo con modelo geográfico simple con 200 nodos y r=0.3
grafo_geografico_200_03 = Grafo(dirigido=False)
grafo_geografico_200_03.grafo_geografico(200, 0.3)
guardar_grafo(grafo_geografico_200_03, "grafo_geografico_200_03")
# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.1)
guardar_grafo(grafo_geografico_500_01, "grafo_geografico_500_01")

# Barabási-Albert
# generamos grafo con modelo Barabási-Albert con 50 nodos y grado 10
grafo_babarasi_50_10 = Grafo(dirigido=False)
grafo_babarasi_50_10.grafo_barabasi_albert(50, 10, False, False)
guardar_grafo(grafo_babarasi_50_10, "grafo_babarasi_50_10")
# generamos grafo con modelo Barabási-Albert con 200 nodos y grado 7
grafo_babarasi_200_07 = Grafo(dirigido=False)
grafo_babarasi_200_07.grafo_barabasi_albert(200, 7)
guardar_grafo(grafo_babarasi_200_07, "grafo_babarasi_200_07")
# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 12
grafo_babarasi_500_12 = Grafo(dirigido=False)
grafo_babarasi_500_12.grafo_barabasi_albert(500, 15)
guardar_grafo(grafo_babarasi_500_12, "grafo_babarasi_500_12")

# Dorogovtsev-Mendes
# generamos grafo con modelo Dorogovtsev-Mendes con 50 nodos
grafo_dorogovtsev_mendes_50 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_50.dorogovtsev_mendes(50)
guardar_grafo(grafo_dorogovtsev_mendes_50, "grafo_dorogovtsev_mendes_50")
# generamos grafo con modelo Dorogovtsev-Mendes con 200 nodos
grafo_dorogovtsev_mendes_200 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_200.dorogovtsev_mendes(200)
guardar_grafo(grafo_dorogovtsev_mendes_200, "grafo_dorogovtsev_mendes_200")
# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")

