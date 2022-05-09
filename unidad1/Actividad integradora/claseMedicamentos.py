class Medicamentos:
    __idcama=0
    __idM=0
    __nomComercial=''
    __Monodroga=''
    __Presentacion=''
    __cantAplicada=0
    __precioT=0
    def __init__(self,i,id,n,m,p,c,pt):
        self.__idcama=i
        self.__idM=id
        self.__nomComercial=n
        self.__Monodroga=m
        self.__Presentacion=p
        self.__cantAplicada=c
        self.__precioT=pt
    def getid(self):
        return self.__idcama
    def __str__(self):
        return " %10s %1s\t  %10.2s  %11.2s  %10.2s"% (self.__nomComercial,self.__Monodroga,self.__Presentacion,self.__cantAplicada,self.__precioT)
       