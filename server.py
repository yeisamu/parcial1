from socket import socket,error
from threading import Thread
import funcion
import json
import time

pelicula = list()
ventas = list()
class Cliente(Thread):
    '''funcion que genera hilos'''
    def __init__(self,conexion,direccion):
        Thread.__init__(self)
        self.conexion=conexion
        self.direccion=direccion

    def run(self):
        while True:
            try:
                mensaje_c=self.conexion.recv(1024)
                dato_calcu = json.loads(mensaje_c)
                if dato_calcu[0] == 'admin':
                    if dato_calcu[1] == 'a':
                        resp = funcion.crearp(pelicula,dato_calcu[2], dato_calcu[3], dato_calcu[4], dato_calcu[5])
                        print pelicula
                    if dato_calcu[1] == 'b':
                        resp = funcion.eliminapel(pelicula, dato_calcu[2])
                        print pelicula
                    if dato_calcu[1] == 'c':
                        resp = funcion.listarp(pelicula)
                    if dato_calcu[1] == 'd':
                        data = funcion.listarp(ventas)
                        resp = json.dumps(data)
                elif dato_calcu[0] == 'cliente':
                    if dato_calcu[1] == 'a':
                        lispel = funcion.listarp(pelicula)
                    if dato_calcu[1] == 'b':
                        resp = funcion.ventat(ventas, dato_calcu[2], dato_calcu[3], dato_calcu[4], dato_calcu[5])
                        print ventas
                        resp=json.dumps(pelicula)
                        self.conexion.send(resp)
            except error:
                print ("[%s] Error de lectura" %self.name)
                break
            else:
                if mensaje_c != 'salir':
                    if mensaje_c:
                        self.conexion.send(mensaje_c)

def main():
    server=socket()
    server.bind(("localhost", 35000))
    server.listen(1)
    while True:
        con,dire=server.accept()
        hilo = Cliente(con,dire)
        hilo.start()

if __name__ == '__main__':
    main()
