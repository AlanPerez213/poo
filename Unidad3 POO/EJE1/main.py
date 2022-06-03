from manejador import manejador
from clasemenu import menu
if __name__ =='__main__':
    lista=manejador()
    lista.cargar()
    #lista.iterar()
    Menu=menu()
    op=None
    
    while(op!=4):
        print("|----------------------------------------------|")
        print("| Ingresar 1 mostrar por codigo de facultad    |")
        print("| Ingresar 2 mostrar por nombre de carreara    |")
        print("|                                              |")
        print("| Ingresar 4 para salir                        |")
        print("|----------------------------------------------|")
        op=int(input("ingresar opcion: "))
        Menu.opcion(op,lista)