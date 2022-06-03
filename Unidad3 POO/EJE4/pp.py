from Celectricos import CalefactoresElectricos
from Cgas import CalefacorGas
from manejaCalefactores import Arreglo
import csv

from calefactores import calefactor
if __name__=='__main__':
    arre=Arreglo(10)
    archivo=open('calefactor-a-gas.csv')
    reader=csv.reader(archivo,delimiter=',')
    bandera=True
    for i in reader:
        if bandera==True:
            bandera=False
        else:
            arre.agregar(CalefacorGas(i[0],i[1],i[2],i[3]))
    archivo.close()
    archivo=open('calefactor-electrico.csv')
    reader=csv.reader(archivo,delimiter=',')
    bandera=True
    for i in reader:
        if bandera==True:
            bandera=False
        else:
            arre.agregar(CalefactoresElectricos(i[0],i[1],i[2]))
    print('*****Item1*****')
    costo=float(input('Ingresar por teclado el  costo por m3:'))
    consumo=float(input('cantidad que se estima consumir en m3:'))
    arre.item1(costo,consumo)
    objeto1=arre.mostarmenor()
    print('*****Item2*****')
    costo=float(input('Ingresar por teclado el  costo por kilowatt/h:'))
    consumo=float(input('cantidad que se estima consumir por hora:'))
    arre.item2(costo,consumo)
    objeto2=arre.mostarmenor2()
    print('*****Item3*****')
    if(objeto1.getcosto()<objeto2.getcosto):
        print('Calefactor a GAS')
        print('Tipo de calefactor {} '.format(objeto1.getmodelo))
        print('Matricula {}'.format(objeto1.getm()))
        print('Calorias {} '.format(objeto1.getc))
    else:
        print('Calefactor a ELECTRICO')
        print('Tipo de calefactor {}'.format(objeto2.getmodelo()))
        print('Potencial {}'.format(objeto2.getp()))