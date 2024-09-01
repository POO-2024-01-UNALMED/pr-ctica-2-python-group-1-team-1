from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self, id, edad, nombre, genero, historial, experiencia, dinero, facturas, diasRestantesContrato, diasTrabajados):
        self.id = id
        self.edad = edad
        self.nombre = nombre
        self.genero = genero
        self.historial = historial
        self.experiencia = experiencia
        self.dinero = dinero
        self.facturas = facturas
        self.diasRestantesContrato = diasRestantesContrato
        self.diasTrabajados = diasTrabajados

    @abstractmethod
    def identificarse(self):
        pass

     # Getters
    def getId(self):
        return self.id

    def getEdad(self):
        return self.edad

    def getNombre(self):
        return self.nombre

    def getGenero(self):
        return self.genero

    def getHistorial(self):
        return self.historial

    def getExperiencia(self):
        return self.experiencia

    def getDinero(self):
        return self.dinero

    def getFacturas(self):
        return self.facturas

    def getDiasRestantesContrato(self):
        return self.diasRestantesContrato

    def getDiasTrabajados(self):
        return self.diasTrabajados

    # Setters
    def setId(self, id):
        self.id = id

    def setEdad(self, edad):
        self.edad = edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setGenero(self, genero):
        self.genero = genero

    def setHistorial(self, historial):
        self.historial = historial

    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def setDinero(self, dinero):
        self.dinero = dinero

    def setFacturas(self, facturas):
        self.facturas = facturas

    def setDiasRestantesContrato(self, diasRestantesContrato):
        self.diasRestantesContrato = diasRestantesContrato

    def setDiasTrabajados(self, diasTrabajados):
        self.diasTrabajados = diasTrabajados