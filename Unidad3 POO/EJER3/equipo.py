from contrato import Contrato
import datetime
class Equipo:
    __id=int
    __nombreE=''
    __ciudad=''
    __ListaContrato=[]
    def __init__(self,id,n,c):
        self.__id=id
        self.__nombreE=n
        self.__ciudad=c
        self.__ListaContrato=[]
    def __str__(self):
        s="\nid del equipo :{}".format(self.__id)
        s+="\nNombre del equipo :{}".format(self.__nombreE)
        s+="\nciudad :{}".format(self.__ciudad)
        s+="\n"
        return s
    def agregaContrato(self,contrato):
        if isinstance(contrato,Contrato):
            self.__ListaContrato.append(contrato)
            print('se agrego contrato en equipo')
    def getnom(self):
        return self.__nombreE
    def getid(self):
        return self.__id
    def buscarfecha(self):
        if self.__ListaContrato != None:
            fecha=str(input('ingresar fecha actual:'))
            for i in self.__ListaContrato:
                if i.getfF() == i.getfF():
                    print(i)
    def calcular(self):
        acum=0
        if len(self.__ListaContrato)!=0:
            for i in self.__ListaContrato:
                acum+=self.__ListaContrato[i].getmonto()
            print("Monto total a pagar {}".format(acum))
