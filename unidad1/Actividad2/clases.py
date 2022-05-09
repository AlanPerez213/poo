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
    def Acum_millas(self,cantM):#recibe como parametro cantidad de millas recorridas en el ultimo viaje
        self.__millasacum += cantM
        return self.__millasacum

    def Canjer_millas(self,cantC):
        print("cantidad de millas {}".format(self.__millasacum))
        if((cantC)<=(self.__millasacum)):
            print("canje posible")
            self.__millasacum -= cantC
            print(" millas obtenidas despues de la modificacion {}".format(self.__millasacum))

        else:
            print("error")
    def getnumero (self):
        return self.__numero


