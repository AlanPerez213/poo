class novedades:
    __legasgo=""
    __importe=float
    __concepto=""
    __cod=""
    def __init__(self,l,i,c,cod):
        self.__legasgo=l
        self.__importe=i
        self.__concepto=c
        self.__cod=cod
    def getleg(self):
        return self.__legasgo
    def getcod(self):
        return self.__cod
    def getcon(self):
        return self.__concepto
    def getimporte(self):
        return self.__importe
        
