class calefactor:
    __marca=''
    __modelo=''
    __costo=float
    def __init__(self,m,mo):
        self.__marca=m
        self.__modelo=mo
        self.__costo=0
    def setcosto(self,costo):
        self.__costo=costo
        print(self.__costo)
    def getcosto(self):
        return self.__costo
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo