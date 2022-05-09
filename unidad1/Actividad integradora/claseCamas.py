class Camas:
    __id=0
    __habitacion=0
    __estado=bool
    __NyA=None
    __diagnosico=''
    __fechaI=''
    __fechaA=''
    def __init__(self,i,h,e,na,d,fi,fa):
        self.__id=i
        self.__habitacion=h
        self.__estado=e
        self.__NyA=na
        self.__diagnosico=d
        self.__fechaI=fi
        self.__fechaA=fa
    def getnom(self):
        return str(self.__NyA)
    def getid(self):
        return int(self.__id)
    def getdiag(self):
        return str(self.__diagnosico)
    def __str__(self):
        #s = "\n id : {} ".format(self.__id1)
        s = "\nPaciente: {0:10} \t\t Cama: {0:11} \t Habitacion: {1:10}\n ".format(self.__NyA,self.__id,self.__habitacion)
        s += "Diagnostico {0:10} \t Fecha de internaciom: {1:10} \n ".format(self.__diagnosico,self.__fechaI)
        s += "Fecha de alta: {0:10} \n".format(self.__fechaA)
        return s
        #return " %4s  %6.2s  %8.2s"% (self.__NyA,self.__id,self.__habitacion)
    
        
