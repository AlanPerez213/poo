from ManejadorCamas import listacamas
from ManejadorMedicamentos import listaM
if __name__=="__main__":
    lista=listacamas()
    lis=listaM()
    lista.cargarcamas()
    lis.cargarmedicamentos()
    nombre=str(input("Ingresar nombre y apellio del pacinte a buscar: "))
    lista.buscar(nombre,lis)
    diag=str(input("Ingresar diagnostico del pacinte a buscar: "))
    lista.mostrar(diag,lis)
    #cama=Camas()
    #medicamento=Medicamentos()
    #cama.cargarcamas()
    #medicamento.()
    