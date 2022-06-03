import numpy as np
from equipo import Equipo
class Arreglo:
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimencion,incremento=5):
        self.__arreglo=np.empty(dimencion,dtype=Equipo)
        self.__cantidad=0
        self.__dimension=dimencion
    def agregar(self,equipo):
        if (self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=equipo
        self.__cantidad+=1
    def buscarEquipo(self,eq):
        b=False
        i=0
        while i< self.__cantidad and self.__arreglo[i].getnom != eq:
            i+=1
        if self.__arreglo[i].getnom == eq:
            return self.__arreglo[i]
    
