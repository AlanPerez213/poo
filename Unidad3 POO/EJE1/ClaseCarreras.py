class Carrera:
    __cod = int
    __cod2 = int
    __nombre =''
    __fechaInicio = ''
    __duracion =''
    __titulo = ''
    def __init__(self,c,c2,n,f,d,t):
        self.__cod=c
        self.__cod2=c2
        self.__nombre=n
        self.__fechaInicio=f
        self.__duracion=d
        self.__titulo=t
    def getcarreras(self):
        return self.__nombre
    def getduraciom(self):
        return self.__duracion
    def getnom(self):
        return self.__nombre
    def getcos(self):
        return self.__cod
    def getcod(self):
        return self.__cod2