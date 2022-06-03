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
    def opcion(self,op,mp,mn):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>4):
            func()
        else:
            func(mp,mn)
    def salir(self,mp,mn):
        print("udted salio del programa")
    def op1(self,mp,mn):
        i=int(input("ingrsar legasgo: "))
        mp.buscar(i,mn)
    def op2(self,mp,mn):
        mp.ordenar()
        mp.mostrar(mn)
    def op3(self,mp,mn):
        mp.sueldomasbajo()
    def op4(self,mp,mn):
        print("")
    def op5(self,mp,mn):
        mp.salir()