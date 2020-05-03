class Prescripcion:
    __fecha=''
    __diagnostico=''
    __medicacion=''
    __presentacion=''
    __dosis=''
    __paciente=None
    __medico=None
    def __init__(self, fecha, diagnostico, medicacion, presentacion, dosis, medico, paciente):
        self.__fecha=fecha
        self.__diagnostico=diagnostico
        self.__medicacion=medicacion
        self.__presentacion=presentacion
        self.__dosis=dosis
        self.__medico=medico
        self.__paciente=paciente
        self.__medico.addPrescipcion(self)
        self.__paciente.addPrescripcion(self)
