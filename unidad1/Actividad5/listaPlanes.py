from traceback import print_tb
from PlanAhorro import plan
import csv
class Lista:
    __LISTA=[]
    def __init__(self):
        self.__LISTA=[]
    def cargarlista(self):
        archivo=open('./planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        b=True
        for fila in reader:
            if b:
                b= not b
            else:
                objeto=plan(fila[0],fila[1],fila[2])
                if type(objeto == plan):
                    self.__LISTA.append(objeto)
                else:
                    print("ERROR")
    def item1(self):
        for i in range(len(self.__LISTA)):
            print("Codigo de automovil {}".format(self.__LISTA[i].getcodigo()))
            print("Modelo del automovil {}".format(self.__LISTA[i].getmodelo()))
            print("Vercion del automovil {}".format(self.__LISTA[i].getvervion()))
            num=int(input("ingresar nuevo valor del automovil"))
            self.__LISTA[i].setprecio(num)
    def item2(self):
        for i in range(len(self.__LISTA)):
            valor=self.__LISTA[i].getvalor()
            print("valor de cuota {} para elvehiculo {}".format(plan.getcuotas()*valor,self.__LISTA[i].getcodigo()))
    def item3(self,cod):
        id=0
        while id < range(len(self.__LISTA)) and cod != self.__LISTA[id].getcodigo():
            if cod != self.__LISTA[id].getcodigo():
                id+=1
            else:
                self.__LISTA[id].setlisitar()