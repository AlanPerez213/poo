class persona:
    __legasgo=""
    __dni=int
    __apellido=""
    __nombre=""
    __sueldo=""
    def __init__(self,l,d,a,n,s):
        self.__legasgo=l
        self.__dni=d
        self.__apellido=a
        self.__nombre=n
        self.__sueldo=s
    def getl(self):
        return self.__legasgo
    def getsueldo(self):
        return int(self.__sueldo)
    def getnom(self):
        return self.__nombre
    def __gt__(self,otro):
        return self.getnom() < otro.getnom()
    def __it__(self,otro):
        return self.getsueldo() > otro.getsueldo()
    def __str__(self):
        s = "\nApellido: {0:10} \t\t Nombre: {0:11}\n ".format(self.__apellido,self.__nombre)
        s += "Dni: {0:10} \t \n ".format(self.__dni)
        s += "Sueldo Basico: {0:10} \n".format(self.__sueldo)
        return s