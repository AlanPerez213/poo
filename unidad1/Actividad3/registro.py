class Registro:
    __dia=0
    __hora=0
    __temperatura=0
    __humedad=0
    __presionAtmosferica=0
    def __init__(self,d,h,t,hu,p):
        self.__dia=d
        self.__hora=h
        self.__temperatura=t
        self.__humedad=hu
        self.__presionAtmosferica=p
    def getdia(self):
        return self.__dia
    def gethora(self):
        return self.__hora
    def gettem(self):
        return self.__temperatura
    def gethume(self):
        return self.__humedad
    def getpre(self):
        return self.__presionAtmosferica