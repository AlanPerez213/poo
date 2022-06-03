from Aparato import Electrodomestico
class televisor(Electrodomestico):
    __tipoPantalla:str
    __pulgadas=float
    __definicion=str
    __conexionInternate=bool
    def __init__(self, ma, mo, c, pa, pr,tipo,pul,defi,con):
        super().__init__(ma, mo, c, pa, pr)
        self.__tipoPantalla=tipo
        self.__pulgadas=pul
        self.__definicion=defi
        self.__conexionInternate=con
    def __str__(self):
        super().__str__()
        print("Tipo de pantalla {}".format(self.__tipoPantalla))
        print("Pulgadas {}".format(self.__pulgadas))
        print("Definicion {}".format(self.__definicion))
        print("Conexion a Internet {}".format(self.__conexionInternate))
        return ''
    def getmarca(self):
        return super().getmarca()
    def getmodelo(self):
        return super().getmodelo()
    def getcolor(self):
        return super().getcolor()
    def getpais(self):
        return super().getpais()
    def getprecio(self):
        return super().getprecio()
    def importe(self):
        if self.__definicion.lower()=='sd':
            importe=super().getprecio()+(super().getprecio()*0.01)
        if self.__definicion.lower()=='hd':
            importe=super().getprecio()+(super().getprecio()*0.02)
        if self.__definicion.lower()=='full hd':
            importe=super().getprecio()+(super().getprecio()*0.02)
        if self.__conexionInternate ==True:
            importe=importe+(super().getprecio()*0.1)
        return importe
        #and 
        #es el precio base más: el 1% si el tipo de definición es SD, 2% si el tipo de definición es HD, 3% si el tipo de definición es FULL HD, mas 10% si tiene conexión a internet.
        return ''
    def toJson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict( 
                marca=self.getmarca(),
                modelo=self.getmodelo(),
                color=self.getcolor(),
                pais=self.getprecio(),
                precio=self.getprecio(),
                tipo=self.__tipoPantalla,
                pulgadas=self.__pulgadas,
                definicion=self.__definicion,
                conexxion=self.__conexionInternate
            )
        )
        return d
