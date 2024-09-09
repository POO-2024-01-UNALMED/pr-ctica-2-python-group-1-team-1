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

# /**
#  * 	Autores: Jaime Luis Osorio Gómez, Santiago Ochoa Cardona, Juan Camilo Marín Valencia, Johan Ramírez Marín, Jonathan David Osorio Restrepo.
#  *  Esta clase representa a una factura, la cuál tiene un numero, total, el total de facturas, la terminal, pasajero, conductor, viaje, vehículo
#  *  y transportadora asociada respectivamente a la factura, esta es útil ya que nos ayudará a llevar un registro de los diferentes pasajeros que 
#  *  hayan comprado un ticket para un viaje, también nos servirá para llevar el registro de pago a los conductores, mecánicos y las transportadoras
#  *  que hayan cancelado su respectivo monto a la terminal.
#  */  

class Factura:

    totalFacturas = 0
    _facturasCreadas = []

    @multimethod
    def __init__(self, total: int, pasajero: Pasajero, terminal: Terminal, conductor: Conductor, viaje: Viaje, vehiculo: Vehiculo, transportadora: Transportadora):
        
        self._numeroFactura = int(10000*(random.uniform(0, 10)))
        self._total = total
        self._pasajero = pasajero
        self._terminal = terminal
        self._conductor = conductor
        self._viaje = viaje
        self._vehiculo = vehiculo
        self._transportadora = transportadora
        self.trayecto = viaje.getSalida().name + "-" + viaje.getLlegada().name
        self._facturasPasajeros = 1
        Factura.totalFacturas += 1
        Factura._facturasCreadas.append(self)

    @multimethod
    def __init__(self, total: int, terminal : Terminal):
        
        self._numeroFactura = int(10000*(random.uniform(0, 10)))
        self._total = total
        self._terminal = terminal
        self._facturasTransportadora = 1
        Factura.totalFacturas += 1
        Factura._facturasCreadas.append(self)

    @multimethod
    def __init__ (self, total: int, transportadora: Transportadora, vehiculo: Vehiculo):
        
        self._numeroFactura = int(10000*(random.uniform(0, 10)))
        self._total = total
        self._transportadora = transportadora
        self._vehiculo = vehiculo
        self._facturasConductores = 1
        Factura.totalFacturas += 1
        Factura._facturasCreadas.append(self)

    @multimethod
    def __init__(self, total: int, transportadora: Transportadora, taller: Taller):
        
        self._numeroFactura = int(10000*(random.uniform(0, 10)))
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
    
    # Método para obtener el número de la factura asociado a una factura
    def getNumeroFactura(self):
        return self._numeroFactura

    # Establece o modifica el número de factura asociado a una factura
    def setNumeroFactura(self, numeroFactura):
        self._numeroFactura = numeroFactura

    # Método para obtener el total asociado a una factura
    def getTotal(self):
        return self._total

    # Establece o modifica el total asociado a una factura
    def setTotal(self, total):
        self._total = total

    # Método para obtener la terminal asociada a una factura
    def getTerminal(self):
        return self._terminal

    # Establece o modifica la terminal asociada a una factura
    def setTerminal(self, terminal):
        self._terminal = terminal

    # Método para obtener el pasajero asociado a una factura
    def getPasajero(self):
        return self._pasajero

    # Establece o modifica el pasajero asociado a una factura
    def setPasajero(self, pasajero):
        self._pasajero = pasajero

    # Método para obtener el conductor asociado a una factura
    def getConductor(self):
        return self._conductor

    # Establece o modifica el conductor asociado a una factura
    def setConductor(self, conductor):
        self._conductor = conductor

    # Método para obtener el viaje asociado a una factura
    def getViaje(self):
        return self._viaje

    # Establece o modifica el viaje asociado a una factura
    def setViaje(self, viaje):
        self._viaje = viaje

    # Método para obtener el vehículo asociado a una factura
    def getVehiculo(self):
        return self._vehiculo

    # Establece o modifica el vehículo asociado a una factura
    def setVehiculo(self, vehiculo):
        self._vehiculo = vehiculo

    # Método para obtener la transportadora asociada a una factura
    def getTransportadora(self):
        return self._transportadora

    # Establece o modifica la transportadora asociada a una factura
    def setTransportadora(self, transportadora):
        self._transportadora = transportadora

    # Método para obtener el taller asociado a una factura
    def getTaller(self):
        return self._taller

    # Establece o modifica el taller asociado a una factura
    def setTaller(self, taller):
        self._taller = taller

    # Método para obtener la fecha asociada a una factura
    def getFecha(self):
        return self._fecha

    # Establece o modifica la fecha asociada a una factura
    def setFecha(self, fecha):
        self._fecha = fecha

    # Método para obtener las facturas de transportadora asociadas a una factura
    def getFacturasTransportadora(self):
        return self._facturasTransportadora

    # Método para obtener las facturas de pasajeros asociadas a una factura
    def getFacturasPasajeros(self):
        return self._facturasPasajeros

    # Método para obtener las facturas de conductores asociadas a una factura
    def getFacturasConductores(self):
        return self._facturasConductores

    # Método para obtener las facturas de mecánico asociadas a una factura
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
