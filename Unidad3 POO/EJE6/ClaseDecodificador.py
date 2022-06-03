import json
from pathlib import Path
from ClaseLista import ListaAparatos
#from Aparato import Electrodomestico
from heladera import Heladera
from Lavarropas import Lavarropas
from televisor import televisor

class ObjectEnconder(object):
 def GuardarArchivo(self,dic,archivo):
    with Path(archivo).open("w",encoding="UTF-8")as destino:
        json.dump(dic,destino,indent=4)
        destino.close()
 def LeerArchivo(self,archivo):
    with Path(archivo).open(encoding="UTF-8")as fuente:
        dic=json.load(fuente)
        fuente.close()
        return dic
 def DecodificarDiccionario(self,dic):
    bandera=False
    if '__class__' not in dic:
        bandera=-1
    else:
        class_name=dic['__class__']
        class_=eval(class_name)
        if(class_name=='ListaAparatos'):
            Aparatos=dic['aparatos']
            lista=class_()
            for i in range(len(Aparatos)):
                dAparato=Aparatos[i]
                class_name=dAparato.pop('__class__')
                class_=eval(class_name)
                atributos=dAparato['__atributos__']
                unAparato=class_(**atributos)
                lista.AgregarAparato(unAparato)
        return lista