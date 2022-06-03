from Personas import persona
import csv
class manejapersona:
    __listaP=[]
    def __init__(self):
        self.__listaP=[]
    def cargar(self):
        archivo=open('personal.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=False
        for i in reader:
            if bandera==False:
                bandera=True
            else:
                p=persona(i[0],i[1],i[2],i[3],i[4])
                self.__listaP.append(p)
        archivo.close()
    def buscar(self,i,mn):
        bandera=False
        j=0
        while i< len(self.__listaP) and bandera==False:
            if int(self.__listaP[j].getl())==i:
                sueldo=self.__listaP[j].getsueldo()
                algo=mn.buscar(i,sueldo)
                print("sueldo a liquidar {} :".format(algo))
                bandera=True
            
    def ordenar(self):
        self.__listaP.sort()
    def mostrar(self,mn):
        for i in self.__listaP:
            print(i)
            cod=i.getl()
            mn.muestra(cod)
    def sueldomasbajo(self):
        menor=100000000
        for i in self.__listaP:
            if menor > i.getsueldo():
                print("hola")
                menor=i.getsueldo()
        print("sueldo mas bajo a cobrar del personal :{}".format(menor))