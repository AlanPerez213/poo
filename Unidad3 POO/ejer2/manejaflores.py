import numpy as np
from flores import Flores
class Arreglo:
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimencion,incremento=5):
        self.__arreglo=np.empty(dimencion,dtype=Flores)
        self.__cantidad=0
        self.__dimension=dimencion
    def agregar(self,flor):
        if (self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=flor
        self.__cantidad+=1
    def buscar(self,idflor):
        bandera=False
        i=0
        while((i< self.__cantidad)and(bandera==False)):
            if str(idflor == self.__arreglo[i].getcos()):
                self.__arreglo[i].setcontador()
                bandera=True
        return self.__arreglo[i]