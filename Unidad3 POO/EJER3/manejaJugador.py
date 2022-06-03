from jugador import Jugador
class lista:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def agregar(self,algo):
        if isinstance(algo,Jugador):
            self.__lista.append(algo)
            print('lista de jugadores cargada')
    def buscarJugador(self,ju):
        bandera=False
        i=0
        while i< len(self.__lista) and bandera==False:
            if(self.__lista[i].getjugador == ju):
                bandera=True
            i+=1
        return self.__lista[i]