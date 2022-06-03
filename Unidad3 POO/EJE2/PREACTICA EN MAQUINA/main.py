from clasemenu import menu
from manejadorpersona import manejapersona
from manejadornovedades import manejanovedades
import csv

if __name__ == "__main__":
    mp=manejapersona()
    mn=manejanovedades()
    mp.cargar()
    mn.cargar()
    Menu=menu()
    op=None
    
    while(op!=4):
        print("|---------------------------------------------------|")
        print("| Ingresar 1 obtener suldo                          |")
        print("| Ingresar 2 listar                                 |")
        print("| Ingresar 3 obtener suldo mas bajo                 |")
        print("| Ingresar 5 para salir                             |")
        print("|---------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        
        Menu.opcion(op,mp,mn)