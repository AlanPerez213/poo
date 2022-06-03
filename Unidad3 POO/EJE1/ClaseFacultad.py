from xml.dom.minidom import Identified
from ClaseCarreras import Carrera
class Facultad:
    __cod=int
    __nombre=''
    __direcciom=''
    __localidad=''
    __provincia=''
    __telefono=''
    __carreras=[]
    def __init__(self,c,n,d,l,p,t,al=[]):
        self.__cod=c
        self.__nombre=n
        self.__direcciom=d
        self.__localidad=l
        self.__provincia=p
        self.__telefono=t
        self.__carreras=[]
        for i in al:
            idfacultad=i[0]
            idcarrera=i[1]
            nombre=i[2]
            fecha=i[3]
            duracion=i[4]
            titulo=i[5]
            nuevacarrera=Carrera(idfacultad,idcarrera,nombre,fecha,duracion,titulo)
            self.__carreras.append(nuevacarrera)  
    def getid(self):
        return int(self.__cod)
    def muestra(self):
        print("\\CARRERAS//")
        for i in self.__carreras:
            print(i.getnom())
    def getnombre(self):
        return self.__nombre
    def buscarCarrera(self,nom):
        pos=0
        bandera=False
        while pos < len(self.__carreras) and bandera== False:
            if self.__carreras[pos].getnom() == nom:
                print("Codigo de carrera: {} {} ".format(self.__carreras[pos].getcos(),self.__carreras[pos].getcod()))
                return True
            else:
                pos+=1