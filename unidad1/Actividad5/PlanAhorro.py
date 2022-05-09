class plan:
    __cuotas=12
    __lisitar=10
    __cod=0
    __modelo=''
    __pesos=0
    __vercion=""
   
    def __init__(self,c,m,p,v):
        self.__cod=c
        self.__modelo=m
        self.__pesos=p
        self.__vercion=v
    @classmethod
    def getcuotas(cls):
        return cls.__cuotas
    @classmethod
    def getlisitar(cls):
        return cls.__lisitar
    @classmethod
    def setlisitar(cls,nuevo):
        cls.__lisitar=nuevo
    def getcodigo(self):
        return self.__cod
    def getmodelo(self):
        return self.__modelo
    def getvercion(self):
        return self.__vercion
    def setprecio(self,precio):
        self.__pesos=precio
    def getvalor(self):
        return (self.__pesos / self.__cuotas) + self.__pesos * 0.10