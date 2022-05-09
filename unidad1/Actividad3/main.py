from registro import Registro
from clasemenu import menu
import csv
if __name__=='__main__':
    Matriz=[]
    for i in range(2):
        Lista=[]
        for j in range(2):
            Lista.append(0)
        Matriz.append(Lista)
        print(Lista)
    archivo=open('Registro.csv')
    reader=csv.reader(archivo,delimiter=';')
    b=True
    for fila in reader:
        if b:
            b=not b
        else:
            Matriz[fila[0]][fila[1]]=Registro(fila[0],fila[1],fila[2],fila[3],fila[4])
    archivo.close()
    Menu=menu()
    op=None
    
    while(op!=4):
        print("|----------------------------------------------------|")
        print("| Ingresar 1 para Mmostrar de menor a mayor          |")
        print("| Ingresar 2 para Temperatura mensul para cada hor a |")
        print("| Ingresar 3 para Listar por dia                     |")
        print("| Ingresar 4 para salir                              |")
        print("|----------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        
        Menu.opcion(op,Matriz)


