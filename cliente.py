#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funcion
import json
ruta_s= socket.socket()
#coneccion con el servidor
ruta_s.connect(("localhost",35000))
while True:
    datos_oper = []
    opt = raw_input('Ingrese usuario: ')
    datos_oper.append(opt)
    if(opt=='admin'):
        menu=funcion.menuadmin()
        listamenu = funcion.menu_lista(menu)
        optm = raw_input("Seleccione una opción ")
        datos_oper.append(optm)
        if optm == 'a':
            nom=raw_input("Nombre de la pelicula ")
            datos_oper.append(nom)
            cos = raw_input("Costo")
            datos_oper.append(cos)
            silla = raw_input("Silla ")
            datos_oper.append(silla)
            hora = raw_input("Hora")
            datos_oper.append(hora)
        if optm == 'b':
            ind = raw_input("Indice de la pelicula ")
            datos_oper.append(ind)
            datos_oper.append('')
            datos_oper.append('')
            datos_oper.append('')
        if optm == 'c':
            datos_oper.append('')
            datos_oper.append('')
            datos_oper.append('')
            datos_oper.append('')
        if optm == 'd':
            datos_oper.append('')
            datos_oper.append('')
            datos_oper.append('')
            datos_oper.append('')
    if (opt == 'cliente'):
        menu = funcion.menucte()
        listamenu = funcion.menu_lista(menu)
        optm = raw_input("Seleccione una opción ")
        datos_oper.append(optm)
        if optm == 'a':
            print "lista de pelitas"
        if optm == 'b':
            nom=raw_input("Nombre de la pelicula ")
            datos_oper.append(nom)
            nomcte = raw_input("Nombre cliente")
            datos_oper.append(nomcte)
            cedu = raw_input("cedula Cliente ")
            datos_oper.append(cedu)
            hora = raw_input("Hora")
            datos_oper.append(hora)

    cadena_envio = json.dumps(datos_oper)
    ruta_s.send(cadena_envio)

    datos = ruta_s.recv(1000)
    resp=json.loads(datos)
    print resp