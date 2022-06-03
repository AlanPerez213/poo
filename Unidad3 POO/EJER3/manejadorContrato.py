import numpy as np
from contrato import Contrato
from jugador import Jugador
import csv
class Arreglo:
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimencion,incremento=5):
        self.__arreglo=np.empty(dimencion,dtype=Contrato)
        self.__cantidad=0
        self.__dimension=dimencion
    def agregar(self,contrato):
        if (self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=contrato
        self.__cantidad+=1
    def buscar(self,id):
        b=False
        i=0
        while i<self.__cantidad and b==False:
            obj=self.__arreglo[i].getequipo()
            print(obj)
            if obj.getid() == id:
                print('hola')
                b=True
            i+=1
            return obj
    def mostrarjugador(self,id):
        i=0
        bandera=False
        while i<self.__cantidad and bandera==False:
            jugador=self.__arreglo[i].getjugador()
            if isinstance(jugador,Jugador):
                if(jugador.getdni() == id):
                    print(jugador)
                    bandera=True
            i+=1
    def guardarArchivo(self):
        data = {}
        lista = []
        'DNI,Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.'
        for contrato in self.__arreglo:
            if contrato != None:
                equipo=contrato.getequipo()
                jugador=contrato.getJugador()
                fechai=contrato.getfechaI()
                fechaF=contrato.ggetfF()
                pago=contrato.getmonto()
                data={"dni":jugador.getdni(),"nombre del jugador":jugador.getnombre(),
                "Fecha de inicio":fechai,"Fecha de fin":fechaF,"Pago":pago}
                lista.append(data)
        print(lista)
        #archivo=open("inscripciones.csv","w")
        with open("contratos.csv","w") as archivo:
            nombres = ["dni","nombre del jugador","Fecha de inicio","Fecha de fin","Pago"]
            escribir = csv.DictWriter(archivo,fieldnames=nombres)
            escribir.writeheader()
            for datas in lista:
                escribir.writerow(datas)