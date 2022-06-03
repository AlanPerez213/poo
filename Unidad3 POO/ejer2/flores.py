class Flores:
    __Numero=int
    __Nombre=''
    __color=''
    __descripcion=''
    __contadorFlores=0
    def __init__(self,n,no,c,d):
        self.__Numero=n
        self.__Nombre=no
        self.__color=c
        self.__descripcion=d
        self.__contadorFlores=0
    def getflor(self):
        return str(self.__Nombre)
    def getcod(self):
        return self.__Numero
    def setcontador(self):
        self.__contadorFlores+=1