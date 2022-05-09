class Menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3
        }
    def opcion(self,op,lista=[]):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>3):
            func()
        else:
            func(lista)
    def op1(self,lista):
        lista.item1()
    def op2(self,lista):
        lista.item2()
    def op3(self,lista):
        codigo=int(input("Codigo de plan a buscar"))
        lista.item3(codigo)

