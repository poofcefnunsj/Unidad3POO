import os

from manejadorLibros import manejadorLibros

from claseMenu import Menu

if __name__ == '__main__':
    libros = manejadorLibros()

    libros.cargarDatos()

    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op, libros)
        salir = op == 3
    print(salir)
