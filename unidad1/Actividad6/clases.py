class Viajero ():
    __numero=None
    __DNI=None
    __nombre=None
    __apellido=None
    __millasacum=None
    def __init__(self,numero,DNI,nombre,apellido,millasacum):
        self.__numero=numero
        self.__DNI=DNI
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasacum=millasacum
    def total_millas(self):
         return self.__millasacum
    def __add__(self,cantM):#recibe como parametro cantidad de millas recorridas en el ultimo viaje
        self.__millasacum = self.__millasacum + cantM
        a=Viajero(self.__numero,self.__DNI,self.__nombre,self.__apellido,self.__millasacum)
        return a

    def __sub__(self,cantC):
        print("cantidad de millas {}".format(self.__millasacum))
        if((cantC)<=(self.__millasacum)):
            print("canje posible")
            self.__millasacum = self.__millasacum-cantC
            print(" millas obtenidas despues de la modificacion {}".format(self.__millasacum))

        else:
            print("error")
    def getnumero (self):
        return self.__numero
    def __gt__(self,otro):
        if (self.__millasacum > otro.__millasacum):
            return True
        else:
            return False
    def __str__(self):
        return " %4s  %4s  %8s"% (self.__nombre,self.__apellido,self.__millasacum)
    def getmillas(self):
        return self.__millasacum
        


