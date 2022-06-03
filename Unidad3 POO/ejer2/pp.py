from flores import Flores
from manejaflores import Arreglo
from manejaramos import lista
from clasemenu import menu
import csv
if __name__ == '__main__':
    archi=open('Flores.csv')
    arre=Arreglo(10)
    lis=lista()
    reader=csv.reader(archi,delimiter=',')
    b=True
    for i in reader:
        if b == True:
            b=False
        else:
            f=Flores(i[0],i[1],i[2],i[3])
            
            arre.agregar(f)
    Menu=menu()
    op=None
    
    while(op!=4):
        print("|----------------------------------------------|")
        print("| Ingresar 1 registrar ramo                    |")
        print("| Ingresar 2 mostrar 5 flores mas vendidas     |")
        print("| Ingresar 3 mostrar por tamaño                |")
        print("| Ingresar 4 para salir                        |")
        print("|----------------------------------------------|")
        op=int(input("ingresar opcion: "))
        Menu.opcion(op,arre,lis)
            
