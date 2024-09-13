import math
import random

class Vehiculo ():

    _listaVehiculos = []

    def __init__ (self, placa, modelo, precio, velocidadPromedio, tipo, transportadora):

        self._conductores = []
        self._estado = True
        self._reparando = False
        self._mecanicoAsociado = None
        self._fechaHoraReparacion = 0

        self._integridad = 90
        self._placa = placa
        self._modelo = modelo
        self._precio = precio
        self._velocidadPromedio = velocidadPromedio
        self._tipo = tipo
        self._capacidad = tipo.getCapacidad()
        self._transportadora = transportadora
        Vehiculo._listaVehiculos.append(self)

    def viaje (self, kilometros):

        if (self.disponibilidad()): #Quitar if?

            self.reduccionIntegridad(kilometros)
            self.accidente()
    
    def disponibilidad (self):
        
        if (self._integridad > 0 and self.verificarConductor()):

            self._estado = True
            return (self._estado)
        
        self._estado = False
        return (self._estado)
    
    def accidente (self):

        if (random.randint(0,100) < 5):

            self._integridad = 0
            self._estado = False

    def reduccionIntegridad (self, duracionViaje):

        self._integridad = math.round(self._integridad - (duracionViaje * random.randint(0,2) / 10))

    def asociarConductor (self, conductor):
        
        self._conductores.append(conductor)

    def quitarConductor (self, conductor):

        self._conductores.remove(conductor)

    def quitarConductorPorId(self, id):
        """Metodo que sirve para quitar un conductor asociado al vehículo."""

        for conductor in self._conductores:

            if conductor.getId() == id:
                self._conductores.remove(conductor)

    def reparacion (self):

        self._integridad = 100
        self._estado = True

    def verificarConductor (self):

        if (len(self._conductores) == 0):

            return (False)
        
        return (True)
    
    #getters and setters

    def setIntegridad (self, integridad):

        self._integridad = integridad
    
    def getIntegridad (self):

        return (self._integridad)
    
    def setPlaca (self, placa):

        self._placa = placa
    
    def getPlaca (self):

        return (self._placa)
    
    def setModelo (self, modelo):

        self._modelo = modelo
    
    def getModelo (self):

        return (self._modelo)
    
    def setPrecio (self, precio):

        self._precio = precio

    def getPrecio (self):

        return (self._precio)
    
    def setVelocidadPromedio (self, velocidad):

        self._velocidadPromedio = velocidad

    def getVelocidadPromedio (self):

        return(self._velocidadPromedio)
    
    def getTipo (self):

        return (self._tipo)
    
    def setCapacidad (self, capacidad):

        self._capacidad = capacidad

    def getCapacidad (self):

        return (self._capacidad)
    
    def setConductores (self, conductores):

        self._conductores = conductores

    def getConductores (self):

        return (self._conductores)
    
    def setTransportadora (self, transportadora):

        self._transportadora = transportadora

    def getTransportadora (self):

        return (self._transportadora)
    
    def setEstado (self, estado):

        self._estado = estado
    
    def getEstado (self):

        return (self._estado)
    
    def setMecanicoAsociado (self, mecanico):

        self._mecanicoAsociado = mecanico

    def getMecanicoAsociado (self):

        return (self._mecanicoAsociado)
    
    def setFechaHoraReparacion (self, hora):

        self._fechaHoraReparacion = hora

    def getFechaHoraReparacion (self):

        return (self._fechaHoraReparacion)
    
    def setReparando (self, reparando):

        self._reparando = reparando

    def isReparando (self):

        return (self._reparando)
    
    @classmethod
    def setListaVehiculos (cls, vehiculos):

        Vehiculo._listaVehiculos = vehiculos

    @classmethod
    def getListaVehiculos (cls):

        return (Vehiculo._listaVehiculos)




