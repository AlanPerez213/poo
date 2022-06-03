class menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            4:self.op4
            }
    def opcion(self,op,lista):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>4):
            func()
        else:
            func(lista)
    def salir(self,lista,numero):
        print("udted salio del programa")
    def op1(self,lista):
        idf=int(input('Ingresar codigo de facultad: '))
        lista.buscar(idf)
    def op2(self,lista):
        nombre=str(input("Ingresar Nombrede carrera a buscar: "))
        lista.buscarnombre(nombre)
    def op4(self,lista,numero):
        lista.salir()
    
        
    