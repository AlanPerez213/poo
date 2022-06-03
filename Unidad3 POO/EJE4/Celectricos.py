from calefactores import calefactor


class CalefactoresElectricos(calefactor):
    __potencia=float
    def __init__(self,m,mo,p):
        super().__init__(m,mo)
        self.__potencia=p
    def calculo(self,costo,consumo):
        costo=(int(self.__potencia)/1000)*consumo*costo
        return costo
    def getp(self):
        return self.__potencia
    