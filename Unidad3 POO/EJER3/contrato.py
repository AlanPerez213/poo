class Contrato:
    __fechaI=''
    __fechaF=''
    __pagoMenusal=float
    __jugador=''
    __equipo=''
    def __init__(self,fi,ff,p,jugador,equipo):
        self.__fechaI=fi
        self.__fechaF=ff
        self.__pagoMenusal=p
        self.__jugador=jugador
        self.__equipo=equipo
    def getequipo(self):
        return self.__equipo
    def getmonto(self):
        return self.__pagoMenusal
    def gethorafinal(self):
        return self.__fechaF
    def getfF(self):
        return self.__fechaF
    def getJugador(self):
        return self.__jugador
    def getfechaI(self):
        return self.__fechaI
    def __str__(self):
        s ="\nFecha Inicio :{}".format(self.__fechaI)
        s+="\nFecha Final :{}".format(self.__fechaF)
        s+="\nPago Mensual :{}".format(self.__pagoMenusal)
        s+="\nJugador : {}".format(self.__jugador)
        s+="\nEquipo : {}".format(self.__equipo)
        s+="\n"
        return s