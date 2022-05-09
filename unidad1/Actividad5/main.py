from PlanAhorro import plan
from listaPlanes import Lista
from ClaseMenu import Menu
if __name__=='__main__':         
    lis=Lista()
    lis.cargarlista()
    print("MENU")
    menu=Menu()
    op=None
    while(op!=4):
        print("|-------------------------------------------------------|")
        print("|1 para: mostrar datos del vehiculo y modificar suprecio|")
        print("|2 para mostrar monto para liscitar cada vehiculo       |")
        print("|3 para modificar las cuotas para licitar el vehiculo   |                                          |")
        print("|-------------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        menu.opcion(op,lis)


