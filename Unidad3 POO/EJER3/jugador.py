from contrato import Contrato
class Jugador:
    __nombre=''
    __dni=''
    __ciudadN=''
    __paisOrigen=''
    __FechaNaciomiemto=''
    __listaContrato=[]
    def __init__(self,n,d,c,p,f):
        self.__nombre=n
        self.__dni=d
        self.__ciudadN=c
        self.__paisOrigen=p
        self.__FechaNaciomiemto=f
        self.__listaContrato=[]
    def __str__(self):
        s ="\nNombre :{}".format(self.__nombre)
        s+="\nDni :{}".format(self.__dni)
        s+="\nCiudad Natal :{}".format(self.__ciudadN)
        s+="\nPais Origen : {}".format(self.__paisOrigen)
        s+="\nFecha Nacimiento : {}".format(self.__FechaNaciomiemto)
        s+="\n"
        return s
    def getdni(self):
        return self.__dni
    def getnombre(self):
        return self.__nombre
    def Agregar(self,contrato):
        if isinstance(contrato,Contrato):
            self.__listaContrato.append(contrato)
            print('Contrato agregado')
