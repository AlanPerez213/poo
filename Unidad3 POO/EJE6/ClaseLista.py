from zope.interface import implementer
from ClaseNodo import Nodo
from ejer5 import Coleccion
from heladera import Heladera
from televisor import televisor
from Lavarropas import Lavarropas
@implementer(Coleccion)
class ListaAparatos:
    __comienzo=None
    __actual=None 
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0            
            raise StopIteration    
        else:        
            dato=self.__actual.getDato()
            self.__indice+=1  
            self.__actual=self.__actual.getSiguiente()        
            return dato
    def toJson(self):
        aparatos=[]
        for v in self:
            aparatos.append(v.toJson())
        dic=dict(__class__=self.__class__.__name__,datos=aparatos)
        return dic
    def AgregarAparato(self,algo):
        try:
            if isinstance(algo,Lavarropas) or isinstance(algo,Heladera) or isinstance(algo,televisor):
                nodo=Nodo(algo)
                if(self.__comienzo==None):
                        nodo.setSiguiente(self.__comienzo)
                        self.__comienzo=nodo
                        self.__actual=nodo
                        self.__tope+=1
                else:
                    aux=self.__comienzo
                    while(aux.getSiguiente()!=None):
                        aux=aux.getSiguiente()
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope+=1
                
                print ("*** APARATO AGREGADO CON EXITO ***")   
                
            else:
                raise TypeError()
        except TypeError:
            print('No es un vehiculo')
    def InsertarAparato(self,pos,dato):
        try: 
            if (pos>=0 and pos<=self.__tope):
                nodo=Nodo(dato)
                if(pos==0):
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__tope+=1
                else:
                    aux=self.__comienzo
                    num=1
                    while(num<pos):
                        aux=aux.getSiguiente()
                        num+=1
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope+=1
        except IndexError:
            print('Posicion Fuera De Rango') 
    def MostrarAparato(self,pos):
        try:
            if(type(pos)==int):
                if(pos==0):
                    return 'Aparato' +self.__comienzo.getNombreClase()
                else:
                    aux=self.__comienzo
                    bandera=False
                    i=1
                    while aux != None and not bandera:
                        if pos==i:
                            bandera=True
                        else:
                            i+=1
                            aux=aux.getSiguiente()
                    if bandera:
                        return 'Aparato' +aux.getNombreClase()
            else:
                pass
        except IndexError:
            print('Posicion No Valida')                                     
    def mostarMarca(self):
        aux=self.__comienzo
        contH=0
        contT=0
        contL=0
        while(aux!= None):
            if isinstance(aux.getDato(),Heladera) and aux.getDato().getmarca().lower()=='phillips':
                contH+=1
            if isinstance(aux.getDato(),televisor) and aux.getDato().getmarca().lower()=='phillips':
                contT+=1
            if isinstance(aux.getDato(),Lavarropas) and aux.getDato().getmarca().lower()=='phillips':
                contL+=1
            aux=aux.getSiguiente()
        print('Heladeras CON MARCA phillips {}'.format(contH))
        print('Televisores con Marca phillips {}'.format(contT))
        print('Lavarropas con Marca phillips {}'.format(contL))
    def busacaLabarropas(self):
        aux=self.__comienzo
        while (aux!= None):
            if isinstance(aux.getDato(),Lavarropas) and aux.getDato().getcarga().lower()=='superior':
                print(aux.getDato())
            aux=aux.getSiguiente
    def mostrarAparato(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getDato())
            importe=aux.getDato().importe()
            print('Importe {}'.format(importe))
        print('')
