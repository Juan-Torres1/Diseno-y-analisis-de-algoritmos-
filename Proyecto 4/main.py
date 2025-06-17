from gv import guardar_grafo
from grafo import Grafo

# Malla 
# Generamos grafo de mallas con 50 nodos
grafo_malla_50 = Grafo(dirigido=False)
grafo_malla_50.grafo_malla(5, 10)
guardar_grafo(grafo_malla_50, "grafo_malla_50_nodos")
guardar_grafo(grafo_malla_50.KruskalD(),"grafo_malla_50_nodos_KruskalD")
guardar_grafo(grafo_malla_50.KruskalI(),"grafo_malla_50_nodos_KruskalI")
guardar_grafo(grafo_malla_50.Prim(),"grafo_malla_50_nodos_Prim")
# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
guardar_grafo(grafo_malla_500, "grafo_malla_500_nodos")
guardar_grafo(grafo_malla_500.KruskalD(), "grafo_malla_500_nodos_KruskalD")
guardar_grafo(grafo_malla_500.KruskalI(), "grafo_malla_500_nodos_KruskalI")
guardar_grafo(grafo_malla_500.Prim(), "grafo_malla_500_nodos_Prim")

# Erdös y Rényi
# generamos grafo Erdös y Rényi con 50 nodos y 250 aristas
grafo_erdos_50_250 = Grafo(dirigido=False)
grafo_erdos_50_250.grafo_erdos_renyi(50, 250)
guardar_grafo(grafo_erdos_50_250, "grafo_erdos_50_250")
guardar_grafo(grafo_erdos_50_250.KruskalD(), "grafo_erdos_50_250_KruskalD")
guardar_grafo(grafo_erdos_50_250.KruskalI(), "grafo_erdos_50_250_KruskalI")
guardar_grafo(grafo_erdos_50_250.Prim(), "grafo_erdos_50_250_Prim")
# generamos grafo Erdös y Rényi con 500 nodos y 2500 aristas
grafo_erdos_500_2500 = Grafo(dirigido=False)
grafo_erdos_500_2500.grafo_erdos_renyi(500, 2500)
guardar_grafo(grafo_erdos_500_2500, "grafo_erdos_500_2500")
guardar_grafo(grafo_erdos_500_2500.KruskalD(),"grafo_erdos_500_2500_KruskalD")
guardar_grafo(grafo_erdos_500_2500.KruskalI(),"grafo_erdos_500_2500_KruskalI")
guardar_grafo(grafo_erdos_500_2500.Prim(),"grafo_erdos_500_2500_Prim")

#Gilbert
# generamos grafo con modelo de Gilbert 50 nodos y probabilidad 0.5
grafo_gilbert_50_05 = Grafo(dirigido=False)
grafo_gilbert_50_05.grafo_gilbert(50, 0.5)
guardar_grafo(grafo_gilbert_50_05, "grafo_gilbert_50_05")
guardar_grafo(grafo_gilbert_50_05.KruskalD(),"grafo_gilbert_50_05_KruskalD")
guardar_grafo(grafo_gilbert_50_05.KruskalI(),"grafo_gilbert_50_05_KruskalI")
guardar_grafo(grafo_gilbert_50_05.Prim(),"grafo_gilbert_50_05_Prim")
# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.02
grafo_gilbert_500_002 = Grafo(dirigido=False)
grafo_gilbert_500_002.grafo_gilbert(500, 0.02)
guardar_grafo(grafo_gilbert_500_002, "grafo_gilbert_500_002")
guardar_grafo(grafo_gilbert_500_002.KruskalD(),"grafo_gilbert_500_002_KruskalD()")
guardar_grafo(grafo_gilbert_500_002.KruskalI(),"grafo_gilbert_500_002_KruskalI()")
guardar_grafo(grafo_gilbert_500_002.Prim(),"grafo_gilbert_500_002_Prim")

# Geográfico
# generamos grafo con modelo geográfico simple con 50 nodos y r=0.5
grafo_geografico_50_05 = Grafo(dirigido=False)
grafo_geografico_50_05.grafo_geografico(50, 0.5)
guardar_grafo(grafo_geografico_50_05, "grafo_geografico_50_05")
guardar_grafo(grafo_geografico_50_05.KruskalD(), "grafo_geografico_50_05_KruskalD")
guardar_grafo(grafo_geografico_50_05.KruskalI(), "grafo_geografico_50_05_KruskalI")
guardar_grafo(grafo_geografico_50_05.Prim(), "grafo_geografico_50_05_Prim")
# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.15)
guardar_grafo(grafo_geografico_500_01, "grafo_geografico_500_01")
guardar_grafo(grafo_geografico_500_01.KruskalD(), "grafo_geografico_500_01_KruskalD")
guardar_grafo(grafo_geografico_500_01.KruskalI(), "grafo_geografico_500_01_KruskalI")
guardar_grafo(grafo_geografico_500_01.Prim(), "grafo_geografico_500_01_Prim")

# Barabási-Albert
# generamos grafo con modelo Barabási-Albert con 50 nodos y grado 10
grafo_babarasi_50_10 = Grafo(dirigido=False)
grafo_babarasi_50_10.grafo_barabasi_albert(50, 10, False, False)
guardar_grafo(grafo_babarasi_50_10, "grafo_babarasi_50_10")
guardar_grafo(grafo_babarasi_50_10.KruskalD(), "grafo_babarasi_50_10_Kruskal_D")
guardar_grafo(grafo_babarasi_50_10.KruskalI(), "grafo_babarasi_50_10_Kruskal_I")
guardar_grafo(grafo_babarasi_50_10.Prim(), "grafo_babarasi_50_10_Prim")
# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 12
grafo_babarasi_500_12 = Grafo(dirigido=False)
grafo_babarasi_500_12.grafo_barabasi_albert(500, 15)
guardar_grafo(grafo_babarasi_500_12, "grafo_babarasi_500_12")
guardar_grafo(grafo_babarasi_500_12.KruskalD(), "grafo_babarasi_500_12_KruskalD")
guardar_grafo(grafo_babarasi_500_12.KruskalI(), "grafo_babarasi_500_12_KruskalI")
guardar_grafo(grafo_babarasi_500_12.Prim(), "grafo_babarasi_500_12_Prim")

# Dorogovtsev-Mendes
# generamos grafo con modelo Dorogovtsev-Mendes con 50 nodos
grafo_dorogovtsev_mendes_50 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_50.dorogovtsev_mendes(50)
guardar_grafo(grafo_dorogovtsev_mendes_50, "grafo_dorogovtsev_mendes_50")
guardar_grafo(grafo_dorogovtsev_mendes_50.KruskalD(), "grafo_dorogovtsev_mendes_50_KruskalD")
guardar_grafo(grafo_dorogovtsev_mendes_50.KruskalI(), "grafo_dorogovtsev_mendes_50_KruskalI")
guardar_grafo(grafo_dorogovtsev_mendes_50.Prim(), "grafo_dorogovtsev_mendes_50_Prim")
# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")
guardar_grafo(grafo_dorogovtsev_mendes_500.KruskalD(), "grafo_dorogovtsev_mendes_500_KruskalD")
guardar_grafo(grafo_dorogovtsev_mendes_500.KruskalI(), "grafo_dorogovtsev_mendes_500_KruskalI")
guardar_grafo(grafo_dorogovtsev_mendes_500.Prim(), "grafo_dorogovtsev_mendes_500_Prim")



