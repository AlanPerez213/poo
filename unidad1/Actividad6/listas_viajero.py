from clases import Viajero
class ListasViajero():
    __lista=[]
    def __init__(self):
       self.__lista=[]
    def crearviajero(self,viajero):
        if (type(viajero == Viajero)):
            self.__lista.append(viajero)
    def getlong(self):
        return len(self.__lista)
    def buscar (self,num):
       i=0
       bandera = False
       while(i<len(self.__lista) and bandera ==False):
           if self.__lista[i].getnumero() == int(num):
               bandera=True
               return i
           else:
               i= i+1   
       if(i<len(self.__lista)):
           return -1     
    def Acum_Millas(self,m,v):
        self.__lista[v]=self.__lista[v]+m
        a=self.__lista[v].getmillas()
        return a
        
    def ordenar(self):
        self.__lista.sort(reverse=True)
    def mostrar(self):
        for fila in self.__lista:
            print(fila)