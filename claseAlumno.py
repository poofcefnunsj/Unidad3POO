from clasePersonaHerenciaMultiple import Persona
class Alumno(Persona):
    __fechaIngreso=''
    __promedio=0.0
    __carrera=''
    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera,
                 codigoCargo, agrupamiento,catedra, sueldo):
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio,
             carrera, codigoCargo, agrupamiento,catedra, sueldo)
        self.__fechaIngreso=fechaIngreso
        self.__promedio=promedio
        self.__carrera=carrera
    def mostrarDatos(self):
        super().mostrarDatos()
        print('Datos del Alumno')
        print('Carrera: {}, fecha de ingreso: {}'.format(self.__carrera, self.__fechaIngreso))
        print('Promedio {0}'.format(self.__promedio))
