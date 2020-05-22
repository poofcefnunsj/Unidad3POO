from clasePunto2D import Punto2D
from clasePunto3D import Punto3D
from claseManejadorPuntos import Manejador
from claseObjectEncoder import ObjectEncoder
from claseMenuPuntos import Menu
if __name__=='__main__':
    jsonF=ObjectEncoder()
    puntos = Manejador()
    bandera=True
    while bandera:
        menu=Menu()
        opcion=menu.mostrarMenu()
        if opcion==1:
            print('Creando un nuevo Punto 2D')
            x=int(input('Coordenada x: '))
            y=int(input('Coordenada y: '))
            punto=Punto2D(x,y)
            puntos.agregarPunto(punto)
        else:
            if opcion==2:
                print('Creando un nuevo Punto 2D')
                x=int(input('Coordenada x: '))
                y=int(input('Coordenada y: '))
                z=int(input('Coordenada z: '))
                punto=Punto3D(x,y,z)
                puntos.agregarPunto(punto)
            else:
                if opcion==3:
                    d=puntos.toJSON()
                    jsonF.guardarJSONArchivo(d,'datosPuntos.json')
                else:
                    if opcion==4:
                        diccionario=jsonF.leerJSONArchivo('datosPuntos.json')
                        puntos=jsonF.decodificarDiccionario(diccionario)
                    else:
                        if opcion==5:
                            puntos.mostrarDatos()
                        else:
                            bandera=False
                            print('Ha seleccionado salir, hasta la vuelta')
