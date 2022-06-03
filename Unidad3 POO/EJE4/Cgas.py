from calefactores import calefactor


class CalefacorGas(calefactor):
    __matricula=str
    __calorias=float
    def __init__(self, m,mo,matricula,calorias):
        super().__init__(m, mo)
        self.__matricula=matricula
        self.__calorias=calorias
    def calculo(self,costo,consumo):
        #costo=calrias/1000*cantidad m3*costo m3
        costo=(int(self.__calorias)/1000)*consumo*costo
        return costo
    def getm(self):
        return self.__matricula
    def getc(self):
        return self.__calorias