class menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3,
            4:self.op4
            }
    def opcion(self,op,lista,numero):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>4):
            func()
        else:
            func(lista,numero)
    def salir(self,lista,numero):
        print("udted salio del programa")
    def op1(self,lista,numero):
        viaj = lista.buscar(numero)
        if(viaj != -1):
            print("para el numero ingresado {} la canidad de millas es {}".format(numero,viaj.total_millas()))
        else:
            print("dato no valido")
    def op2(self,lista,numero):
        millas=int(input("ingresar la cantidad de millas a acumular: "))
        viaj = lista.buscar(numero)
        if (viaj != -1):
            print("para el numero ingresado {} se le acumularan estas millas {}".format(numero,viaj.Acum_millas(millas)))
        else:
            print("dato no valido")
    def op3(self,lista,numero):
        canje=int(input("ingresar millas a canjear: "))
        viaj = lista.buscar(numero)
        if(viaj != -1):
            viaj.Canjer_millas(canje)
        else:
            print("dato no valido")
    def op4(self,lista,numero):
        lista.salir()
        
    


        

