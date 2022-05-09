from claseCamas import Camas
from claseMedicamentos import Medicamentos
import csv
class listacamas:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def cargarcamas(self):
        archivo=open('camas.csv')
        reader=csv.reader(archivo,delimiter=';')
        b=True
        for i in reader:
            
            if b==True:
                b=False
            else:
                self.__lista.append(Camas(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    def buscar(self,nombre,lis):
        
        for fila in self.__lista:
            nom=fila.getnom()
            if nom==nombre:
                print (fila)
                id=int(fila.getid())
                lis.mostrar(id)
    def mostrar(self,diagnostico,lis):

        for fila in self.__lista:
            d=fila.getdiag()
            if d==diagnostico:
                print(fila)