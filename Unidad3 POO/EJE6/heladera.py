from Aparato import Electrodomestico


class Heladera(Electrodomestico):
    __capacidad=int
    __freezer=bool
    __cilicia=bool
    def __init__(self, ma, mo, c, pa, pr,ca,free,ci):
        super().__init__(ma, mo, c, pa, pr)
        self.__capacidad=ca
        self.__freezer=free
        self.__cilicia=ci
    def __str__(self):
        super().__str__()
        print("Capacidad {}".format(self.__capacidad))
        print("Frezzer {}".format(self.__freezer))
        print("Cilicia {}".format(self.__cilicia))
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
        if self.__freezer==True:
            importe=super().getprecio()+(super().getprecio()*0.05)
        else:
            importe=super().getprecio()+(super().getprecio()*0.01)
        if self.__cilicia==True:
            importe=importe+super().getprecio()+(super().getprecio()*0.1)
        #es el precio base más: 1% si no tiene freezer, 5% si tiene freezer, 10% si es cíclica.
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
                capacidad=self.__capacidad,
                freezer=self.__freezer,
                cilicia=self.__cilicia

            )
        )
        return d
