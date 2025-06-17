"""Clase arista, sirve para crear un objeto de tipo arista con los atributos nodo de inicio y nodo final
Tamnién contiene al parámetro dirigido, que indica si la arista es dirigida o no."""

class Arista:
    # Constructor de la clase arista
    def __init__(self, nodo_inicio, nodo_final, dirigido=False):
        self.__nodo_inicio = nodo_inicio  # nodo fuente
        self.__nodo_final = nodo_final  # nodo destino

        self.__dirigido = dirigido  # parametro para seber si el grafo es dirigido

    # Sobreescritura del metodo str
    def __str__(self):
        if self.__dirigido:
            print_pattern = "{0}->{1}"
        else:
            print_pattern = "{0} -- {1} "
        return print_pattern.format(self.__nodo_inicio.get_etiqueta(), self.__nodo_final.get_etiqueta())

    # Getter del nodo fuente, regresa el nodo fuente de la aristas
    def get_nodo_fuente(self):
        return self.__nodo_inicio

    # Getter del nodo destino, regresa el nodo destino  de la aristas
    def get_nodo_destino(self):
        return self.__nodo_final

    # Sobrescritura de los metodos hash y eq
    def __eq__(self, otro):
        nodo_inicio_igual = self.__nodo_inicio == otro.get_nodo_fuente()
        nodo_final_igual = self.__nodo_final == otro.get_nodo_destino()

        return nodo_inicio_igual == nodo_final_igual == True

    def __hash__(self):
        return hash(self.__nodo_inicio.get_etiqueta() +
                    self.__nodo_final.get_etiqueta())