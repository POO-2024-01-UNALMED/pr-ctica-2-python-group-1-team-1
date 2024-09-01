from gestorAplicacion.usuarios.pasajero import Pasajero
from gestorAplicacion.usuarios.persona import Persona
from gestorAplicacion.usuarios.conductor import Conductor
from gestorAplicacion.usuarios.mecanico import Mecanico
from gestorAplicacion.administrativo.terminal import Terminal
from gestorAplicacion.administrativo.viaje import Viaje
from gestorAplicacion.administrativo.vehiculo import Vehiculo
from gestorAplicacion.administrativo.transportadora import Transportadora
from gestorAplicacion.administrativo.taller import Taller
from multimethod import multimethod
import random

class Factura:

    totalFacturas = 0
    _facturasCreadas = []

    @multimethod
    def __init__(self, total: int, pasajero: Pasajero, terminal: Terminal, conductor: Conductor, viaje: Viaje, vehiculo: Vehiculo, transportadora: Transportadora):
        
        self._numeroFactura = 10000*(random.uniform(0, 10))
        self._total = total
        self._pasajero = pasajero
        self._terminal = terminal
        self._conductor = conductor
        self._viaje = viaje
        self._vehiculo = vehiculo
        self._transportadora = transportadora
        ##self.trayecto = Pendiente, implementación clase viaje y enums
        self._facturasPasajeros = 1
        Factura.totalFacturas += 1
        Factura._facturasCreadas.append(self)

    @multimethod
    def __init__(self, total: int, terminal : Terminal):
        
        self._numeroFactura = 10000*(random.uniform(0, 10))
        self._total = total
        self._terminal = terminal
        self._facturasTransportadora = 1
        Factura.totalFacturas += 1
        Factura._facturasCreadas.append(self)

    @multimethod
    def __init__ (self, total: int, transportadora: Transportadora, vehiculo: Vehiculo):
        
        self._numeroFactura = 10000*(random.uniform(0, 10))
        self._total = total
        self._transportadora = transportadora
        self._vehiculo = vehiculo
        self._facturasConductores = 1
        Factura.totalFacturas += 1
        Factura._facturasCreadas.append(self)

    @multimethod
    def __init__(self, total: int, transportadora: Transportadora, taller: Taller):
        
        self._numeroFactura = 10000*(random.uniform(0, 10))
        self._total = total
        self._transportadora = transportadora
        self._taller = taller
        self._facturasMecanico = 1
        Factura.totalFacturas += 1
        Factura._facturasCreadas.append(self)

    @classmethod
    def crearFacturaPasajero(cls, total, pasajero, terminal, conductor, viaje, vehiculo, transportadora):
        
        return cls(total, pasajero, terminal, conductor, viaje, vehiculo, transportadora)
    
    @classmethod
    def crearFacturaConductor(cls, total, transportadora, vehiculo):
        
        return cls(total, transportadora, vehiculo)
    
    @classmethod
    def crearFacturaTransportadora(cls, total, terminal):
        
        return cls(total, terminal)
    
    def getNumeroFactura(self):

        return self._numeroFactura

    def setNumeroFactura(self, numeroFactura):

        self._numeroFactura = numeroFactura

    def getTotal(self):
        
        return self._total

    def setTotal(self, total):

        self._total = total

    def getTerminal(self):

        return self._terminal

    def setTerminal(self, terminal):
        
        self._terminal = terminal

    def getPasajero(self):

        return self._pasajero

    def setPasajero(self, pasajero):

        self._pasajero = pasajero

    def getConductor(self):

        return self._conductor

    def setConductor(self, conductor):

        self._conductor = conductor

    def getViaje(self):

        return self._viaje

    def setViaje(self, viaje):

        self._viaje = viaje

    def getVehiculo(self):

        return self._vehiculo

    def setVehiculo(self, vehiculo):

        self._vehiculo = vehiculo

    def getTransportadora(self):
        
        return self._transportadora

    def setTransportadora(self, transportadora):

        self._transportadora = transportadora

    def getTaller(self):

        return self._taller

    def setTaller(self, taller):

        self._taller = taller

    def getFecha(self):

        return self._fecha

    def setFecha(self, fecha):

        self._fecha = fecha

    def getFacturasTransportadora(self):

        return self._facturasTransportadora

    def getFacturasPasajeros(self):

        return self._facturasPasajeros

    def getFacturasConductores(self):
        
        return self._facturasConductores

    def getFacturaMecanico(self):

        return self._facturasMecanico

    @classmethod
    def setTotalFactura(cls, totalFacturas):

        cls._totalFacturas = totalFacturas

    @classmethod
    def getTotalFactura(cls):

        return cls._totalFacturas

    @classmethod
    def getFacturasCreadas(cls):

        return cls._facturasCreadas

    @classmethod
    def setFacturasCreadas(cls, facturasCreadas):

        cls._facturasCreadas = facturasCreadas
