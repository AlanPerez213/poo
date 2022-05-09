class ListasViajero():
    __lista=None
    def __init__(self):
       self.__lista=[]
    def crearviajero(self,viajero):
       self.__lista.append(viajero)
    def getlong(self):
        return len(self.__lista)
    def buscar (self,num):
       i=0
       while(i<len(self.__lista) and int(self.__lista[i].getnumero()) != int(num)):
           i= i+1
       if(i<len(self.__lista)):
            return self.__lista[i]
       else:
            return -1

    """
    def item1 (self,num):
       pos=self.__lista.buscar(num)
       if (pos != -1):
          print("para el numero ingresado {} la canidad de millas es {}".format(num,self.__lista[pos].total_millas()))
       else:
           print("no se a encontrado el viajero")
    """
    

        