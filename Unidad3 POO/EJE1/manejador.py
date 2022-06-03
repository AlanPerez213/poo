from msilib.schema import Font
from ClaseFacultad import Facultad
import csv
class manejador:
    __Lista=[]
    def __init__(self):
        self.__lista=[]
    def cargar(self):
        facultad=open('Facultades.csv')
        reader=csv.reader(facultad,delimiter=",")
        fila=next(reader)
        bandera=True
        
        print("Facultad")
        while bandera:
            #print(fila)
            lista=[]
            print("Carreras")
            filaCarreras=next(reader)
            while bandera and fila[0]==filaCarreras[0]:
                lista.append(filaCarreras)
                #print(filaCarreras)
                try:
                    filaCarreras=next(reader)
                except StopIteration:
                    bandera=False
            facu=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],lista)
            fila=filaCarreras           
            self.__Lista.append(facu)
        facultad.close()
    def buscar(self,id):
        pos=0
        bandera=False
        while pos < len(self.__Lista) and bandera == False:
            if self.__Lista[pos].getid() == id:
                print("Nombre de la facultad: {}".format(self.__Lista[pos].getnombre()))
                self.__Lista[pos].muestra()
                bandera=True
            else:
                pos+=1
    def buscarnombre(self,nom):
        pos=0
        bandera=False
        while pos < len(self.__Lista) and bandera == False:
            if pos < len(self.__Lista):
                algo=self.__Lista[pos].buscarCarrera(nom)
                if algo== True:
                    bandera=True
                    print("Facultad|| {} ||".format(self.__Lista[pos].getnombre()))              
            else:
                pos+=1
    def iterar(self):
        for i in self.__Lista:
            print(i.getnombre())
            i.mo()