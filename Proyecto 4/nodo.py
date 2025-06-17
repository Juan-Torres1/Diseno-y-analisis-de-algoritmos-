"""
La clase nodo sirve para crear objetos de tipo 
nodo con los atributos etiqueta, dirigido y aristas
"""


class Nodo:
    def __init__(self, etiqueta,dist=int(0), dirigido=False):  # Constructor de la clase
        self.__etiqueta = etiqueta  # identificador del nodo
        self.__dirigido = dirigido  # parametro dirigido se usa para saber si el grafo es dirigido
        self.__aristas = set()  # Estructura de datos tipo set, util para mantener las aristas conectadas al nodo
        self.__dist    = (dist)

    def __str__(self):  # Sobrescritura del metodo str
        cadena_retorno = ""
        for arista in self.__aristas:
            cadena_retorno += str(arista)

        return cadena_retorno

    def get_aristas(self):  # Getter de la arista regresa una arista especifica en el nodo
        return self.__aristas

    def get_etiqueta(self):  # Getter de la etiqueta regresa la etiqueta que identifica al nodo
        return self.__etiqueta

    # Getter de las aristas salientes, si el grafo es dirigido regresa las aristas que salen del nodo
    def get_aristas_salientes(self):
        if not self.__dirigido:
            return self.__aristas

        aristas_salientes = []
        for arista in self.__aristas:
            if arista.get_nodo_fuente() == self:
                aristas_salientes.append(arista)

        return aristas_salientes

    # Getter de las aristas entrantes, si el grafo es dirigido regresa las aristas que entran al nodo
    def get_aristas_entrantes(self):
        if not self.__dirigido:
            return self.__aristas

        aristas_entrantes = []
        for arista in self.__aristas:
            if arista.get_nodo_destino() == self:
                aristas_entrantes.append(arista)

        return aristas_entrantes

    # Metodo para agregar una arista
    def add_arista(self, arista):
        self.__aristas.add(arista)  # se agrega una arista al set que guarda las aristas del nodo

    def remove_arista(self, arista):
        if arista in self.__aristas:  # Si se encuentra la arista en el nodo se remueve la arista
            self.__aristas.remove(arista)  # se remueve una arista del set que guarda las aristas
        else:  # si no se encuentra la arista en el nodo lanza el sigueinte error
            raise ValueError(
                "No se pudo encontrar la arista {0} en el  nodo {1}".format(str(arista), str(self)))

    def set_aristas(self, aristas):  # Setter de las aristas
        self.__aristas = aristas
    def set_distancia(self,dist):
        self.__dist=dist
    def get_distancia(self):
        return self.__dist
    def set_etiqueta(self,etiqueta):
        self.__etiqueta=etiqueta

    def __str__(self):
        return self.__etiqueta
