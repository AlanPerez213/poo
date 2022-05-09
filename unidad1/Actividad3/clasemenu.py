class menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3,
            4:self.op4
            }
    def opcion(self,op,Matriz):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>4):
            func()
        else:
            func(Matriz)
    def salir(self,Matriz):
        print("udted salio del programa")
    def op1(self,Matriz):
        for i in range(2):
            for j in range(2):
                Matriz[i][j].mostrar()

    def op2(self,Matriz):

        for i in range(2):
            for j in range(2):
                acum=acum + Matriz[i.getdia()-1][j.gethora()-1].gettem()
                cont=cont+1
        print("Temperatura promedio por mes {}".format(acum/cont))
        print("Hola")
       
    def op3(self,Matriz):
        dia=(int(input("ingresar un dia: ")))
        for j in range(2):
            print("{}     {}    {}".format("Hora","Temperatura","Humedad","Precion"))
            print("{}     {}    {}".format(Matriz[dia-1][j.gethora()-1].gethora(),Matriz[dia-1][j.gethora()-1].gettem(),Matriz[dia-1][j.gethora()-1].gethume(),Matriz[dia-1][j.gethora()-1].getpre()))   
    def op4(self,Matriz):
        Matriz.salir()