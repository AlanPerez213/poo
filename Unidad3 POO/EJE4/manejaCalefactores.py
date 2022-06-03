import  numpy as np
from calefactores import calefactor
from Cgas import CalefacorGas
from Celectricos import CalefactoresElectricos
class Arreglo:
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimencion,incremento=5):
        self.__arreglo=np.empty(dimencion,dtype=calefactor)
        self.__cantidad=0
        self.__dimension=dimencion
    def agregar(self,calefactor):
        if (self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=calefactor
        self.__cantidad+=1
    def item1(self,costo,consumo):
        for i in self.__arreglo:
            if isinstance(i,CalefacorGas):
                #costo=self.__arreglo[i].calculo(costo,cosnumo)
                costo=i.calculo(costo,consumo)
                i.setcosto(costo)
                #self.__arreglo[i].setcosto(costo)
    def mostarmenor(self):
        menor=999999
        for i in self.__arreglo:
            if isinstance(i,CalefacorGas):
                if i.getcosto() < menor:
                    obj=i
                    menor=i.getcosto()  
        print('Marca {} Modelo {}'.format(obj.getmarca(),obj.getmodelo()))
        return obj
    def item2(self,costo,consumo):
        for i in self.__arreglo:
            if isinstance(i,CalefactoresElectricos):
                #costo=self.__arreglo[i].calculo(costo,cosnumo)
                costo=i.calculo(costo,consumo)
                i.setcosto(costo)
                #self.__arreglo[i].setcosto(costo)
    def mostarmenor2(self):
        for i in self.__arreglo:
            if isinstance(i,CalefactoresElectricos):
                if i.getcosto() < menor:
                    obj=i
                    menor=i.getcosto()  
        print('Marca {} Modelo {}'.format(obj.getmarca(),obj.getmodelo()))
        return obj
