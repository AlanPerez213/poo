from Novedades import novedades
import csv
class manejanovedades:
    __listaN=[]
    def __init__(self):
        self.__listaN=[]   
    def cargar(self):
        archivo=open('novedades.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=False
        for i in reader:
            if bandera==False:
                bandera=True
            else:
                p=novedades(i[0],i[1],i[2],i[3])
                self.__listaN.append(p)
        archivo.close()
    def buscar(self,i,sueldo):
        for j in self.__listaN:
            
            if j.getl()==i:
                c=self.__listaN[j].getcod()
                if c=='A':
                    sueldo+=sueldo
                else:
                    sueldo-=sueldo   
        return sueldo     
    def muestra(self,cod):
        print("Codigo         Concepto       Importe")
        for i in self.__listaN:
            if i.getleg() == cod:
                print("{0:10}     {1:10}     {2:10}".format(i.getcod(),i.getcon(),i.getimporte()))