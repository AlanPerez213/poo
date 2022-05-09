from claseMedicamentos import Medicamentos
import csv
class listaM:
    __listaMedicamentos=[]
    def __init__(self):
        self.__listaMedicamentos=[]
    def cargarmedicamentos(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        b=True
        for i in reader:
            
            if b==True:
                b=False
            else:
                self.__listaMedicamentos.append(Medicamentos(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    def mostrar(self,id):
        print("Medicamento/Monodroga          precentacion      cantidad         precio")
        for objeto in self.__listaMedicamentos:
            i=int(objeto.getid())
            if id==i:
                print(objeto)