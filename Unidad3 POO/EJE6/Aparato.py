class Electrodomestico:
    __marca=''
    __modelo=''
    __color=''
    __paisFabricacion=''
    __precioBase=float
    def __init__(self,ma,mo,c,pa,pr):
        self.__marca=ma
        self.__modelo=mo
        self.__color=c
        self.__paisFabricacion=pa
        self.__precioBase=pr
    def __str__(self):
        print("Marca {}".format(self.__marca))
        print("Modelo {}".format(self.__modelo))
        print("Color {}".format(self.__color))
        print("Pais de Fabricacion {}".format(self.__paisFabricacion))
        print("Precio Base".format(self.__precioBase))
        return ''
    def toJson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.__marca,
                modelo=self.__modelo,
                color=self.__color,
                pais=self.__paisFabricacion,
                precio=self.__precioBase
            )
        )
        return d
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getcolor(self):
        return self.__color
    def getpais(self):
        return self.__paisFabricacion
    def getprecio(self):
        return self.__precioBase
