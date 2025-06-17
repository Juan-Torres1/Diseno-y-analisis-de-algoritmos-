"""
La clase grafo posee un diccionario para almacenar objetos de tipo
nodo y las aristas se guardan en una estructura tipo set
"""
from arista import Arista
from nodo import Nodo
from gv import mostrar_grafo
import random
import itertools
import math
import collections
from collections import defaultdict
from collections import deque
import nodo
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = {}  # diccionario para almacenar los nodos con su etiqueta como llave
        self.__aristas = set()  # mantiene las aristas guardadas en un conjunto
        self.__dirigido = dirigido  # parametro para saber si el grafo es dirigido

    def __str__(self):  # sobreescritura del metodo string
        imp_cadena = ""
        nodos_copy=self.nodos
        for llave in nodos_copy.copy():
            if str(nodos_copy[llave])=="":
               # nodos_copy.pop(llave)
                pass
            else:
                new_string = str(nodos_copy[llave]).replace(llave, "")
                if  not new_string.startswith(llave):
                    if new_string.startswith(" --"):
                        imp_cadena += llave + new_string + '\n'
                    else:
                        if new_string.endswith("-- "):
                            t = new_string.rsplit('--', 1)
                            u = ''.join(t)
                        else:
                            t = new_string.rsplit('--',1)
                            u = ''.join(t)
                        if u=='':
                            u=''
                        imp_cadena += "{0} -- ".format(llave) + u + '\n'



        return imp_cadena

    def add_nodo(self, etiqueta,distancia=0):  # metodo para añadir nodos al grafo
        if etiqueta not in self.nodos:
            self.nodos[etiqueta] = Nodo(etiqueta,distancia, self.__dirigido)

    def add_arista(self, etiqueta_inicio, etiqueta_final,peso=1):  # metodo para añadir aristas al grafo
        nodo_fuente = self.get_nodo(etiqueta_inicio)
        nodo_final = self.get_nodo(etiqueta_final)
        mirror_edge = None
        if (nodo_fuente or nodo_final) is None:  # si no existe el nodo fuente o el nodo destino salta el error
            #print(type(nodo_fuente),type(nodo_final))
            raise ValueError("No se puede encontrar el nodo fuente  o el nodo destino ")
        if self.__dirigido:  # Si el grafo es dirigido se agrega la arista tal cual
            arista = Arista(nodo_fuente, nodo_final,peso, self.__dirigido)
        else:
            for aristaen in self.get_aristas():
                nodo_fuente_arista = aristaen.get_nodo_fuente()
                nodo_destino_arista = aristaen.get_nodo_destino()

                if (nodo_destino_arista == nodo_fuente) and (nodo_fuente_arista == nodo_final):
                    mirror_edge = True
            if not mirror_edge:
                arista = Arista(nodo_fuente, nodo_final,peso, self.__dirigido)
            else:
                #print(type(nodo_fuente))
                #print(type(nodo_final))
                arista = Arista(nodo_final, nodo_fuente,peso, self.__dirigido)

        nodo_fuente.add_arista(arista)

        if nodo_fuente != nodo_final:
            nodo_final.add_arista(arista)

        self.__aristas.add(arista)

    def remove_arista(self, etiqueta_inicio, etiqueta_final):  # metodo para eliminar aristas en el grafo
        nodo_fuente = self.get_nodo(etiqueta_inicio)
        nodo_destino = self.get_nodo(etiqueta_final)

        if (nodo_fuente or nodo_destino) is None:
            raise ValueError("No se encontro el nodo fuente o el nodo destino en el grafo")

        arista = Arista(nodo_fuente, nodo_destino, self.__dirigido)

        if arista not in self.__aristas:
            raise ValueError(
                "no se encuentra la arista  {0} en el grafo".format(str(Arista)))

        nodo_fuente.remove_arista(arista)
        nodo_destino.remove_arista(arista)
        self.__aristas.remove(arista)

    def remove_nodo(self, etiqueta_nodo):  # metodo para eliminar nodos en el grafo
        if etiqueta_nodo not in self.nodos:
            raise ValueError(
                "No se encontro el nodo {0} en el grafo".format(etiqueta_nodo))

        nodo = self.nodos[etiqueta_nodo]

        copia_aristas_entrantes = nodo.get_aristas_entrantes().copy()  # Removemos la entrada de las aristas entrantes
        for arista in copia_aristas_entrantes:
            nodo_adyacente = arista.get_nodo_fuente()
            nodo_adyacente.remove_arista(arista)

            if arista in self.__aristas:
                self.__aristas.remove(arista)

        copia_aristas_salientes = nodo.get_aristas_salientes().copy()
        for arista in copia_aristas_salientes:  # Removemos la entrada de las aristas salientes
            adjacent_vertex = arista.get_nodo_destino()
            adjacent_vertex.remove_arista(arista)

            if arista in self.__aristas:
                self.__aristas.remove(arista)

        self.nodos.pop(etiqueta_nodo)

        nodos = self.get_nodos()
        for nodo in nodos:
            aristas = nodos[nodo].get_aristas()
            copia_aristas = aristas.copy()
            for arista in aristas:
                nodo = arista.get_nodo_fuente()
                if nodo.get_etiqueta() == etiqueta_nodo:
                    copia_aristas.remove(arista)
                nodo.set_aristas(copia_aristas)

    # empieza la definicion de getters
    def get_nodo(self, etiqueta):
        return self.nodos.get(etiqueta)

    def get_nodos(self): #metodo para obtener los nodos
        return self.nodos

    def get_aristas(self): # Metodo para obtener aristas
        return self.__aristas

    def get_grado(self, etiqueta):  # Metodo para obtener el grado
        if self.es_dirigido():
            grado = len(self.get_nodo(etiqueta).get_aristas_entrantes()) + \
                    len(self.get_nodo(etiqueta).get_aristas_salientes())
        else:
            grado = len(self.get_nodo(etiqueta).get_aristas_salientes())
        return grado

    def es_dirigido(self):  # Metodo que regresa si el grafo es dirigido
        return self.__dirigido

    # comienza la definicion de los metodos para generar grafos aleatorios
    def grafo_malla(self, m, n):
        for i in range(m * n):  # se comienza creando los n nodos
            self.add_nodo(str(i))
        for j in range(m):
            # print("j:"+str(j))
            index_horizontal = j * n
            # print("index:"+str(index_horizontal))
            for i in range(index_horizontal, index_horizontal + n):
                # print("esa es:"+str(i))
                # if(i<10):
                if (i != (n - 1) + index_horizontal):
                    # print("agregando arista {0},{1}".format(i,(i+1)))
                    self.add_arista(str(i), str(i + 1),random.randrange(1,1000))
                if j != (m - 1):
                    # print("agregando arista {0},{1}".format(i, (i + n)))
                    self.add_arista(str(i), str(i + n),random.randrange(1,1000))
        return self

    def grafo_erdos_renyi(self, n, m, dirigido=False, auto=False):  # metodo para generar modelo de ErdosRenyi
        self.__dirigido = dirigido
        for i in range(n):
            self.add_nodo(str(i))
        while len(self.get_aristas()) != m:
            n1 = (random.randrange(n))
            n2 = (random.randrange(n))
            if not auto:
                if n1 != n2:
                    self.add_arista(str(n1), str(n2),random.randrange(1,1000))
            else:
                self.add_arista(str(n1), str(n2),random.randrange(1,1000))
        #print(len(self.get_aristas()))
        return self

    def grafo_gilbert(self, n, p, dirigido=False, auto=False):
        self.__dirigido = dirigido
        for i in range(n):
            self.add_nodo(str(i))
        for i in range(n):
            for j in range(n):
                if not auto:
                    if (i != j):
                        if random.random() <= p:
                            # print("creando arista ({0},{1})".format(i,j))
                            self.add_arista(str(i), str(j),random.randrange(1,1000))
        #print(len(self.get_aristas()))
        return self

    def dorogovtsev_mendes(self, n, dirigido=False):
        self.__dirigido = dirigido
        for i in range(3):
            self.add_nodo(str(i))
        self.add_arista("0", "1",random.randrange(1,1000))
        self.add_arista("0", "2",random.randrange(1,1000))
        self.add_arista("1", "2",random.randrange(1,1000))
        # print(self.get_grado("0"))
        while len(self.get_nodos()) != n:
            nodo_nuevo = str(len(self.get_nodos()) + 1)
            self.add_nodo(nodo_nuevo)
            arista_random = random.choice(list(self.get_aristas()))
            nodo_fuente = arista_random.get_nodo_fuente()
            etiqueta_nodo_fuente = nodo_fuente.get_etiqueta()
            nodo_destino = arista_random.get_nodo_destino()
            etiqueta_nodo_destino = nodo_destino.get_etiqueta()
            self.add_arista(nodo_nuevo, etiqueta_nodo_fuente,random.randrange(1,1000))
            self.add_arista(nodo_nuevo, etiqueta_nodo_destino,random.randrange(1,1000))
        #print("numero de nodos: {}".format(len(self.get_nodos())))
        #print("numero de aristas: {}".format(len(self.get_aristas())))
        return self

    def grafo_barabasi_albert(self, n, d, dirigido=False, auto=False):
        self.__dirigido = dirigido
        for i in range(n):  # se generan n nodos
            self.add_nodo(str(i))
        for i in range(n):  # iteramos entre todos los posibles pares
            for j in range(n):
                if not auto:  # si no se permiten autociclos
                    if i != j:
                        # print("El grado del nodo {0} es {1}".format(j, self.get_grado(str(j))))
                        # probamos en base a la probabilidad que depende del grado del nodo
                        if (self.get_grado(str(j)) < d) and (self.get_grado(str(i)) < d):
                            p = 1 - (self.get_grado(str(j)) / d)
                            if random.random() <= p:  # si el numero random es menor o igual a la probailidad se crea
                                # print("creando arista ({0},{1})".format(i, j))
                                self.add_arista(str(i), str(j),random.randrange(1,1000))
                else:  # lo  mismo pero si se permiten autociclos
                    if (self.get_grado(str(j)) < d) and (self.get_grado(str(i)) < d):
                        p = 1 - (self.get_grado(str(j)) / d)
                        if random.random() <= p:
                            # print("creando arista ({0},{1})".format(i, j))
                            self.add_arista(str(i), str(j),random.randrange(1,1000))
        #print(len(self.get_aristas()))
        return self

    def grafo_geografico(self, n, r, dirigido=False, auto=False):  # metodo para generar el modelo geografico
        self.__dirigido = dirigido  # parametro dirigido
        for i in range(n):  # se crean n nodos
            self.add_nodo(str(i))
        posicion_nodos = {}  # diccionario para mantener las cordenadas de los nodos
        for nodo in self.get_nodos():  # asignamos cordenadas  a los nodos
            llave = nodo
            posicion_random = (round(random.random(),3), round(random.random(),3))
            posicion_nodos.update({llave: posicion_random})
        combinaciones = itertools.combinations(posicion_nodos, 2)  # todos los posibles pares si el grafo es no dirigido
        permutaciones = itertools.permutations(posicion_nodos, 2)  # todos los posibles pares si el grafi es dirigido
        if not dirigido:  # si el grafo es no dirigido usamos las combinaciones para comparar la distancia de los pares
            for combinacion in combinaciones:
               # print(combinacion)
                nodo_fuente = combinacion[0]
                nodo_destino = combinacion[1]
                cordenadas_nodo_fuente = posicion_nodos.get(combinacion[0])
                cordenadas_nodo_destino = posicion_nodos.get(combinacion[1])
                nodo_fuente_x = cordenadas_nodo_fuente[0]
                nodo_fuente_y = cordenadas_nodo_fuente[1]
                nodo_destino_x = cordenadas_nodo_destino[0]
                nodo_destino_y = cordenadas_nodo_destino[1]
                # calculamos la distancia entre pares
                distancia = math.sqrt((nodo_destino_x - nodo_fuente_x) ** 2 + (nodo_destino_y - nodo_fuente_y) ** 2)
                # print(distancia)
                # si la distancia es menor o igual a r se genera la arista ente pares
                if (distancia <= r):
                    self.add_arista(nodo_fuente, nodo_destino,random.randrange(1,1000))
        else:  # lo mismo pero cuando el grafo es no dirigido usamos permutaciones
            for permutacion in permutaciones:
               # print(permutacion)
                nodo_fuente = permutacion[0]
                nodo_destino = permutacion[1]
                cordenadas_nodo_fuente = posicion_nodos.get(permutacion[0])
                cordenadas_nodo_destino = posicion_nodos.get(permutacion[1])
                nodo_fuente_x = cordenadas_nodo_fuente[0]
                nodo_fuente_y = cordenadas_nodo_fuente[1]
                nodo_destino_x = cordenadas_nodo_destino[0]
                nodo_destino_y = cordenadas_nodo_destino[1]
                distancia = math.sqrt((nodo_destino_x - nodo_fuente_x) ** 2 + (nodo_destino_y - nodo_fuente_y) ** 2)
                # print(distancia)
                if (distancia <= r):
                    self.add_arista(nodo_fuente, nodo_destino,random.randrange(1,1000))
        return self
    def get_nodos_adyacentes(self,node): #metodo para obtener nodos adyacentes
        nodos_adyacentes=[]
        nodo=self.get_nodo(node)
        for arista in nodo.get_aristas():
            if arista.get_nodo_fuente()!=nodo:
                nodos_adyacentes.append(arista.get_nodo_fuente().get_etiqueta())
            else:
                nodos_adyacentes.append(arista.get_nodo_destino().get_etiqueta())
        return nodos_adyacentes
    def get_hijos(self,node): #metodo para obtener hijos dado un nodo
        nodos_adyacentes=[]
        nodo=self.get_nodo(node)
        for arista in nodo.get_aristas():
            if arista.get_nodo_fuente()==nodo:
                nodos_adyacentes.append(arista.get_nodo_destino().get_etiqueta())
        return nodos_adyacentes
    def get_padres(self,node): #metodo para obtener los ancestros de un nodo
        nodos_adyacentes=[]
        nodo=self.get_nodo(node)
        for arista in nodo.get_aristas():
            if arista.get_nodo_fuente()!=nodo:
                nodos_adyacentes.append(arista.get_nodo_fuente().get_etiqueta())
        return nodos_adyacentes

    def get_peso_arista(self, u, v):
        nodo=self.get_nodo(u)
        aristas= nodo.get_aristas()
        for arista in aristas:
            if (self.get_nodo(v).get_etiqueta()== arista.get_nodo_fuente().get_etiqueta()
                    or self.get_nodo(v).get_etiqueta()== arista.get_nodo_destino().get_etiqueta()):
                return  arista.get_peso()
    def bfs(self, s): # Metodo de algoritmo de busqueda bfs
        queue = deque([s]) # cola que nos permitira guadar los nodos para ejecutar el algoritmo bfs
        capa = {s: 0} # creamos la capa 0
        ancestro = {s: None} # diccionario que nos permitira guardar los nodos y la relacion con sus hijos
        arbol = Grafo() #creamos un nuevo objeto de tipo grafo para generar el arbol que nos da el algoritmo bfs
        while queue: #mientras haya elementos en la cola
            nodo = queue.popleft() #extraemos el nodo de la cola
            arbol.add_nodo(nodo) #agregamos el nodo al arbol
            for n in self.get_nodos_adyacentes(nodo):#agregamos los nodos adyacentes al nodo a su respectiva capa
                if n not in capa:
                    queue.append(n)
                    capa[n] = capa[nodo] + 1
                    ancestro[n] = nodo

        for key in ancestro: #se agregan todas las aristas al arbol
            if ancestro[key]!=None:
                arbol.add_arista(ancestro[key], key)

        return arbol

    def dfs_i(self, s): #Metodo de algoritmo de busqueda dfs iterativo
        arbol_dfs = Grafo() #creamos un nuevo objeto tipo grafo para almacenar el arbol creado por el algoritmo
        explorados = [s] # agregamos el nodo fuente a la lista de explorados
        #print(explorados)
        arbol_dfs.add_nodo(s)   #agregamos el nodo fuente al arbol
        u = self.get_nodo(s)
        stack = [] #inicializamos el stack
        while len(explorados)<len(self.get_nodos()):
            #print(stack)
            #print(explorados)
            #print("explorando:{}".format(u))
            aristas = u.get_aristas()
            for arista in aristas:   # añadir al stack todos los nodos adyacentes a u
                #print(arista)
                #print("etiqueta de U:{}".format(u.get_etiqueta()))
                #print("Nodo fuente:{}".format(arista.get_nodo_fuente()))
                #print("Nodo destino:{}".format(arista.get_nodo_destino()))
                if str(u.get_etiqueta()) == str(arista.get_nodo_fuente()): #verificamos la direccion de la arista
                    comp=True
                else:
                    comp=False
                v = arista.get_nodo_destino() if comp else arista.get_nodo_fuente()
                #print("u:{} y v:{}".format(u,v))
                if str(v) not in explorados: #se agrega al stack la arista del nodo explorado
                    stack.append((u.get_etiqueta(), v.get_etiqueta()))
            if not stack:
                break
            padre, hijo = stack.pop() # hacemos pop al stack
            if hijo not in explorados:
                arbol_dfs.add_nodo(hijo)
                #print(padre,hijo)
                arbol_dfs.add_arista(padre,hijo) # se agrega la arista nueva al arbol
                explorados.append(hijo) # se agrega el  nodo explorado a la lista de explorados

            u = self.get_nodo(hijo)
            #print("nuevo u:{}".format(u))

        return arbol_dfs



    def dfs_r(self, u): #Metodo de algoritmo de busqueda dfs recursivo

        arbol_dfs = Grafo()
        explorados = set()
        self.recursive_tool(u, arbol_dfs, explorados)

        return arbol_dfs

    def recursive_tool(self, u, arbol_dfs, explorados):

        arbol_dfs.add_nodo(u)
        explorados.add(u)
        u=self.get_nodo(u)
        aristas = u.get_aristas()

        for arista in aristas:
            v = arista.get_nodo_destino().get_etiqueta()
            if str(u.get_etiqueta()) == str(arista.get_nodo_fuente()):  # verificamos la direccion de la arista
                comp = True
            else:
                comp = False
            v = arista.get_nodo_destino().get_etiqueta() if comp else arista.get_nodo_fuente().get_etiqueta()
            if v in explorados:
                continue
            arbol_dfs.add_nodo(arista.get_nodo_fuente().get_etiqueta()) #se agegan los nodos correspondientes a la arista al grafo
            arbol_dfs.add_nodo(arista.get_nodo_destino().get_etiqueta())#se agegan los nodos correspondientes a la arista al grafo
            #print(arista.get_nodo_fuente().get_etiqueta(),arista.get_nodo_destino().get_etiqueta())
            arbol_dfs.add_arista(arista.get_nodo_fuente().get_etiqueta(),arista.get_nodo_destino().get_etiqueta())
            self.recursive_tool(v, arbol_dfs, explorados)

    def Dijkstra(self, s):
        arbol_caminos=Grafo() # se crea el objeto que contendra el arbol de caminos minimos
        self.__dist = dist = dict() #diccionario para almacenar distancias
        self.__prev = prev = dict() #diccionario util para almacenar los padres
        explorado= set()            # con esta estructura se matiene un seguimiento de los nodos ya explorados
        cola_prioridad = set()      # cola de prioridad

        dist[s] = 0 # hacemos la distancia de el nodo fuente 0
        prev[s] = s # agregamos a la estructura el nodo fuente
        cola_prioridad.add(s)   # agregamos el nodo fuente a la cola de prioridades

        while cola_prioridad:
            u = min(cola_prioridad, key=dist.get) #obtener el elemento con el valor minimo en la cola de prioridad
            for nodo in self.get_nodos_adyacentes(u): # para cada nodo en los nodos adyacentes al nodo u
                if nodo in explorado:
                    continue
                actualizar_distancia = self.get_distancia(u) + self.get_peso_arista(u, nodo) # actualizamos distancia
                if actualizar_distancia < self.get_distancia(nodo): #si es menor se almacena la nueva distancia
                    dist[nodo] = actualizar_distancia
                    prev[nodo] = u
                    cola_prioridad.add(nodo) # se agrega el nodo adyacente a u  a la cola de prioridad
            cola_prioridad.remove(u) # removemos u de la cola de prioridad
            explorado.add(u) # agregamos el nodo u a los nodos ya explorados
        nodos=self.get_nodos() # obtenemos los nodos del arbol original
        #print(self.get_nodos())
        arbol_caminos.add_nodo(s,0) # agregamos el nodo fuente al arbol de caminos
        caminos=dict() #estructura para mantener los caminos minimos desde el nodo fuente hacia cada uno de los nodos
        for nodo in nodos:
            arbol_caminos.add_nodo(nodo, self.get_distancia(nodo)) # agregamos el nodo al arbol de caminos minimos
            caminos[nodo]=self.get_camino(nodo) # utilizamos la funcion que nos ayuda a construir el camino y lo guardamos
        for camino in caminos.values(): # agregamos las aristas del arbol caminos minimos
            for index in range(0,len(camino)-1):
                peso = self.get_peso_arista(camino[index], camino[index+1])
                #print(camino)
                #print(camino[index])
                #print(camino[index+1])
                arbol_caminos.add_arista(camino[index],camino[index+1], peso)
        return  arbol_caminos

    def get_distancia(self, u): #funcion que ayuda al calculo de las distancias
       
        return self.__dist.get(u, math.inf)

    def get_camino(self, s): #funcion util para la constriccion del arbol de caminos

        path = [s]
        index=0
        while self.__prev[s] != s:
            s = self.__prev[s]
            path.append(s)

        return path[::-1]
    