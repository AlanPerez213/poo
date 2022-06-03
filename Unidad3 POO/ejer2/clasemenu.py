from ramo import Ramo
from manejaflores import Arreglo
from flores import Flores
class menu():

    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3,
            4:self.op4
            }
    def opcion(self,op,arre,lis):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>4):
            func()
        else:
            func(arre,lis)
    def salir(self,lista,numero):
        print("udted salio del programa")
    def op1(self,arre,lis):
        tamaño=str(input('ingresar tamaño tenindo encuenta<chico=3 flores><mediano=6 flores><grande=9 flores> :'))
        ramo=Ramo(tamaño)
        
        if tamaño.lower()=='chico':
            i=3
            if tamaño.lower()=='mediano':
                i=6
            if tamaño.lower()=='grande':
                i=9
        #ramo.settamaño(tamaño)
        for j in range(i):
            print('cantidad de flores que tendra su ramo {}'.format(i))
            flor=int(input('ingresar el codigo de flor:'))
            FLOR=arre.buscar(flor)
            if isinstance(FLOR,Flores):
                ramo.agregarFlor(FLOR)
            else:
                print('no instancia error')
        
        lis.agrega(ramo) 
    def op2(self,arre,lis):
        nombre=str(input("Ingresar Nombrede carrera a buscar: "))
        
    def op3(self,arre,lis):
        print('')
    def op4(self,arre,lis):
        arre.salir()