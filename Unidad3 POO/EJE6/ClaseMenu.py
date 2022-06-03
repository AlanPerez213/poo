
from ClaseDecodificador import ObjectEnconder
from heladera import Heladera
from televisor import televisor
from Lavarropas import Lavarropas
import os
import time
class Menu:
    __switcher = None
    def  __init__ ( self ): 
        self.__switcher  = { 
            1: self.opcion1 ,
            2: self. opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            0: self.salir
        }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , vehiculos ):
        func = self . __switcher . get ( op , lambda:print ( "Opción no válida" ))
        func ( vehiculos )
    def salir ( self,vehiculos):
        os.system('cls')
        print ( 'Cerrando sistema...' )
        time.sleep(1)
    def opcion1(self,Aparato):
        os.system('cls')
        posicion=input("Ingrese la posicion a insertar: (Distinto de 0)")
        try:
            posicion=int(posicion)
            dato=self.datos(Aparato)
            Aparato.InsertarAparato(posicion-1,dato)
        except ValueError:
            print("Debe ingresar un numero entero...")
            time.sleep(1)

    def opcion2(self,Aparato):
        os.system('cls')
        dato=self.datos(Aparato)
        Aparato.AgregarAparato(dato)
        
    def opcion3(self,Aparato):
        os.system('cls')
        pos=input("Posicion: ")
        try:
            pos=int(pos)
            vehi=Aparato.MostrarAparato(pos-1)
            if(vehi!=None):
                print("{}".format(vehi))
                time.sleep(1)
        except ValueError:
            print("Debe ingresar un numero entero...")
            time.sleep(1)

    def opcion4(self,Aparato):
        os.system('cls')
        Aparato.mostarMarca()
    def opcion5(self,Aparatos):
        os.system('cls')
        Aparatos.busacaLabarropas()
        time.sleep(5)

    def opcion6(self,Aparatos):
        Aparatos.mostrarAparato()
    def opcion7(self,ve):
        os.system('cls')
        Nuevo=ve.toJson()
        Json=ObjectEnconder()
        Json.GuardarArchivo(Nuevo,('C:/Users/Alumno/Desktop/POO/unidad 3 poo/ejemplo/vehiculos.json'))
        print("*** ARCHIVO GUARDADO ***")
        time.sleep(1)
    def datos(self,Aparato):
        aparato=input("Heladera o Televisor o Lavarropas --> ")
        if (aparato.lower()=='heladera'):
            print('Eesto es una Heladera')
            modelo=input("Modelo: ")
            marca=input("Marca: ")
            color=input("Color: ")
            pais=input("pais De Fabricacion: ")
            precio=input("Precio Base: ")
            cap=input("Capacidad del Heladera: ")
            freezer=input("Capacidad del Heladera: ")
            cilicia=input("Cilicia del Heladera: ")
            objeto=Heladera(marca,modelo,color,pais,precio,cap,freezer,cilicia)
            
        if (aparato.lower()=='televisor'):
            print('Esto es un Televisor')
            modelo=input("Modelo: ")
            marca=input("Marca: ")
            color=input("Color: ")
            pais=input("pais De Fabricacion: ")
            precio=input("Precio Base: ")
            tipoPantalla=input("Tipo de pantalla: ")
            pulgadas=input("Pulgadas: ")
            definicion=input("Definicion de pantalla: ")
            conexionInternate=input("Coneccion a Internet: ")
            objeto=televisor(marca,modelo,color,pais,precio,tipoPantalla,pulgadas,definicion,conexionInternate)
            
        if (aparato.lower()=='lavarropas'):
            print('Esto es un Lavarropas')
            modelo=input("Modelo: ")
            marca=input("Marca: ")
            color=input("Color: ")
            pais=input("pais De Fabricacion: ")
            precio=input("Precio Base: ")
            capasidad=input("Capacidad del Labarropas: ")
            velocidad=input("Revoluciones del Lavarropas: ")
            programas=input("Cantidad de programas del Labarropas: ")
            carga=input("carga: ")
            objeto=Lavarropas(marca,modelo,color,pais,precio,capasidad,velocidad,programas,carga)
        return objeto    