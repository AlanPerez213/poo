from pickletools import read_float8
from manejadorEquipo import Arreglo
from manejaJugador import lista
from jugador import Jugador
from equipo import Equipo
from clasemenu import menu
import csv
if __name__== '__main__':
    arre=Arreglo(10)
    archivo=open('Equipos.csv')
    lis=lista()
    reader=csv.reader(archivo,delimiter=',')
    for i in reader:
        eq=Equipo(i[0],i[1],i[2])
        arre.agregar(eq)
    archivo.close()
    archivo=open('Jugadores.csv')
    reader=csv.reader(archivo,delimiter=',')
    bandera=False
    for i in reader:
        if bandera==False:
            bandera=True
        else:
            ju=Jugador(i[0],i[1],i[2],i[3],i[4])
    Menu=menu()
    op=None
    
    while(op!=4):
        print("|----------------------------------------------|")
        print("| Ingresar 1 registrar contrarto               |")
        print("| Ingresar 2 mostar por decha de conrato       |")
        print("| Ingresar 3 Mostrar por dni                   |")
        print("| Ingresar 5 importe total a pagar de un equipo|")
        print("| Ingresar 4 para salir                        |")
        print("|----------------------------------------------|")
        op=int(input("ingresar opcion: "))
        Menu.opcion(op,arre,lis)
    