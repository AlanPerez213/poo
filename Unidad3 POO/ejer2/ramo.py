class Ramo:
    __tamaño=str
    __listaF=[]
    def __init__(self,t):
        self.__tamaño=t
        self.__listaF=[]
    def agregarFlor(self,f):
        self.__listaF.append(f)
    def settamaño(self,tamaño):
        self.__tamaño=tamaño