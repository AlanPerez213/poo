from zlib import DEF_BUF_SIZE


class Ventana:
    __titulo=""
    __xSUPERIORIZQUIERDO=0
    __ySUPERIORIZQUIERDO=0
    __xINFERIORDERECHO=0
    __yINFERIORDERECHO=0
    def __init__(self,t,x=0,y=0,xi=500,yi=500):
        self.__titulo=t
        self.__xSUPERIORIZQUIERDO=x
        self.__ySUPERIORIZQUIERDO=y
        self.__xINFERIORDERECHO=xi
        self.__yINFERIORDERECHO=yi
    def mostrar(self):
        print("X superior izquierdo {} Y superior derecho {} / X inferior izquierdo {} Y inferior derecho".format(self.__xSUPERIORIZQUIERDO,self.__ySUPERIORIZQUIERDO,self.__xINFERIORDERECHO,self.__yINFERIORDERECHO))

    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__xINFERIORDERECHO - self.__xSUPERIORIZQUIERDO
    def ancho(self):
        return self.__yINFERIORDERECHO - self.__ySUPERIORIZQUIERDO
    def moverDerecha(self,valor = 1):
        if self.__xSUPERIORIZQUIERDO < self.__xINFERIORDERECHO:
            self.__xINFERIORDERECHO += valor
            self.__xSUPERIORIZQUIERDO +=valor
    def moverIzquierda(self,izquierda=1):
        if self.__xSUPERIORIZQUIERDO < self.__xINFERIORDERECHO:
            self.__xINFERIORDERECHO -= izquierda
            self.__xSUPERIORIZQUIERDO -= izquierda
    def bajar(self,valor):
        if self.__ySUPERIORIZQUIERDO < self.__yINFERIORDERECHO:
            self.__yINFERIORDERECHO -= valor
            self.__ySUPERIORIZQUIERDO -= valor
    def subir(self,valor):
        if self.__ySUPERIORIZQUIERDO < self.__yINFERIORDERECHO:
            self.__yINFERIORDERECHO += valor
            self.__ySUPERIORIZQUIERDO += valor