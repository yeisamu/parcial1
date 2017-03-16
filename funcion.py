import json
def usuarios():
    lista=list()
    lista=[['yeison','Admin'],['cristian','Cliente']]
    cadena=json.dumps(lista)
    return cadena

def menuadmin():
    lista=['a. crear pelicula','b. eliminar pelicula','c. listar peliculas','d. ver peliculas  vendidas','e. sillas disponibles']
    cadena=json.dumps(lista)
    return cadena

def menucte():
    lista=['a. listar peliculas','b. Comprar entrada ','c. ver mi pelicula']
    cadena=json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i
def crearp(pelicula,nom,cos,silla,hora):
    pelcliente=[nom,cos,silla,hora]
    pelicula.append(pelcliente)

def eliminapel(pelicula,indice):
    pelicula.pop(int(indice))

def listarp(pelicula):
    for i in pelicula:
        print i
def ventat(venta,nom,cli,ced,hora):
    vencliente=[nom,cli,ced,hora]
    venta.append(vencliente)