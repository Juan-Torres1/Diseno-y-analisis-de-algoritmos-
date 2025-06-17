from gv import guardar_grafo
from grafo import Grafo

# Dorogovtsev-Mendes
# Grafo con modelo Dorogovtsev-Mendes con 30 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(30)
guardar_grafo(grafo_dorogovtsev_mendes_30, "grafo_dorogovtsev_mendes_30")
guardar_grafo(grafo_dorogovtsev_mendes_30.bfs("1"), "grafo_dorogovtsev_mendes_30_bfs")
guardar_grafo(grafo_dorogovtsev_mendes_30.dfs_i("1"), "grafo_dorogovtsev_mendes_30_dfs_i")
guardar_grafo(grafo_dorogovtsev_mendes_30.dfs_r("1"), "grafo_dorogovtsev_mendes_30_dfs_r")
# Grafo con modelo Dorogovtsev-Mendes con 100 nodos
grafo_dorogovtsev_mendes_100 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_100.dorogovtsev_mendes(100)
guardar_grafo(grafo_dorogovtsev_mendes_100, "grafo_dorogovtsev_mendes_100")
guardar_grafo(grafo_dorogovtsev_mendes_100.bfs("1"), "grafo_dorogovtsev_mendes_100_bfs")
guardar_grafo(grafo_dorogovtsev_mendes_100.dfs_i("1"), "grafo_dorogovtsev_mendes_100_dfs_i")
guardar_grafo(grafo_dorogovtsev_mendes_100.dfs_r("1"), "grafo_dorogovtsev_mendes_100dfs_r")
# Grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")
guardar_grafo(grafo_dorogovtsev_mendes_500.bfs("1"), "grafo_dorogovtsev_mendes_500_bfs")
guardar_grafo(grafo_dorogovtsev_mendes_500.dfs_i("1"), "grafo_dorogovtsev_mendes_500_dfs_i")
guardar_grafo(grafo_dorogovtsev_mendes_500.dfs_r("1"), "grafo_dorogovtsev_mendes_500_dfs_r")



