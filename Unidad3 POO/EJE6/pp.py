from ClaseLista import ListaAparatos
from ClaseDecodificador import ObjectEnconder
from ClaseMenu import Menu
if __name__ == "__main__":
    Aparato=ListaAparatos()
    Json=ObjectEnconder()
    Diccionario=Json.LeerArchivo('aparatos electronicos.json')
    Aparatos=Json.DecodificarDiccionario(Diccionario)
    menu=Menu()
    ban=False
    while not ban:
        
        print("1. Insertar un Aparato  ")
        print("2. Agregar un Aparato")
        print("3. Mostrar por pantalla qué tipo de objeto.")
        print("4. Mostrar Aparato cuya marca sea phillips ")
        print("5. Mostrar la marca de todos los lavarropas que tienen carga superior")
        print("6. Mostrar todos los aparatos ")
        print("7. Guardar ")
        print("0. Salir")
        op=int(input("Ingrese su opcion."))
        menu.opcion(op,Aparato)
        ban= op == 0