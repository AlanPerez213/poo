from manejadorContrato import Arreglo
from equipo import Equipo
from contrato import Contrato
from jugador import Jugador
class menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3,
            4:self.op4,
            5:self.op5
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
        arregloContrato=Arreglo(3)
        eq=str(input('ingresar equipo:'))
        ju=str(input('ingresar nombre del jugador:'))
        unequipo=arre.buscarEquipo(eq)#
        if isinstance(unequipo,Equipo):
            print('equipo valido')
        unjugador=lis.buscarJugador(ju)#
        if isinstance(unjugador,Jugador):
            print('jugador valido')
        fechaI=str(input('ingresar fecha inicial del contrato:'))
        fechaF=str(input('ingresr fecha final del contrato:'))
        monto=float(input('ingresar monto a pagar del jugador:'))
        con=Contrato(fechaI,fechaF,monto,unjugador,unequipo)
        unequipo.agregaContrato(con)
        unjugador.Agregar(con)
        arregloContrato.agregar(con)

    def op2(self,arre,lis):
        id=int(input('ingresar id del equipo:'))
        arregloContrato=Arreglo(3)
        equi=arregloContrato.buscar(id)
        print(equi)
        if isinstance(equi,Equipo):
            equi.buscarfecha()
        else:
            print('id mal ingresado')
    def op3(self,arre,lis):
        arregloContrato=Arreglo(3)
        id=int(input('ingresar dni del jugador:'))
        arregloContrato.mostrarjugador(id)
        
    def op4(self,arre,lis):
        arre.salir()
    def op5(self,arre,lis):
        NombreE=str(input("Ingresar nombre de equipo"))
        unequipo=arre.buscarEquipo(NombreE)
        if isinstance(unequipo,Equipo):
            print('equipo valido')
            unequipo.calcular()
        arregloContrato=Arreglo(3)
        arregloContrato.guardarArchivo()