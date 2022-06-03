from Aparato import Electrodomestico


class Lavarropas(Electrodomestico):
    __capasidad=int
    __velocidad=int
    __programas=int
    __carga=str
    def __init__(self, ma, mo, c, pa, pr,ca,ve,pro,carga):
        super().__init__(ma, mo, c, pa, pr)
        self.__capasidad=ca
        self.__velocidad=ve
        self.__programas=pro
        self.__carga=carga
    def __str__(self):
        super().__str__()
        print("Capacidad {}".format(self.__capasidad))
        print("Revoluciones por cegundo {}".format(self.__velocidad))
        print("Cantidad de programas {}".format(self.__programas))
        print("Carga {}".format(self.__carga))
        return ''
    def getcarga(self):
        return self.__carga
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
        if self.__capasidad>= 5:
            importe=super().getprecio()+(super().getprecio()*0.01)
        else:
            importe=super().getprecio()+(super().getprecio()*0.03)
        #es el precio base, mas: el 1% si la capacidad de lavado es menor o igual a 5 kg , 3% si la capacidad de lavado supera los 5 kg.
        return importe
    def toJson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict( 
                marca=self.getmarca(),
                modelo=self.getmodelo(),
                color=self.getcolor(),
                pais=self.getprecio(),
                precio=self.getprecio(),
                capasidad=self.__capasidad,
                velocidad=self.__velocidad,
                programas=self.__programas,
                carga=self.__carga

            )
        )
        return d
