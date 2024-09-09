from gestorAplicacion.usuarios.pasajero import Pasajero
from gestorAplicacion.usuarios.conductor import Conductor
from gestorAplicacion.administrativo.terminal import Terminal
from gestorAplicacion.administrativo.viaje import Viaje
from gestorAplicacion.administrativo.vehiculo import Vehiculo
from gestorAplicacion.administrativo.transportadora import Transportadora
from gestorAplicacion.administrativo.taller import Taller
from multimethod import multimethod
import random

class Factura:
    # Atributos de clase
    totalFacturas = 0  # Número total de facturas creadas
    _facturasCreadas = []  # Lista que almacena todas las facturas creadas

    @multimethod
    def __init__(self, total: int, pasajero: Pasajero, terminal: Terminal, conductor: Conductor, viaje: Viaje, vehiculo: Vehiculo, transportadora: Transportadora):
        """
        Constructor para la clase Factura, este objeto estará asociado con un pasajero.
        @param total: El valor total de la factura.
        @param pasajero: El pasajero asociado a la factura.
        @param terminal: La terminal donde se generó la factura.
        @param conductor: El conductor asociado al viaje en la factura.
        @param viaje: El viaje asociado a la factura.
        @param vehiculo: El vehículo asociado a la factura.
        @param transportadora: La transportadora que genera la factura.
        """
        self._numeroFactura = int(random.uniform(0, 10000))  # Genera un número de factura aleatorio
        self._total = total  # Valor total de la factura
        self._pasajero = pasajero  # Pasajero asociado a la factura
        self._terminal = terminal  # Terminal asociada a la factura
        self._conductor = conductor  # Conductor asociado a la factura
        self._viaje = viaje  # Viaje asociado a la factura
        self._vehiculo = vehiculo  # Vehículo asociado a la factura
        self._transportadora = transportadora  # Transportadora asociada a la factura
        # self.trayecto = "Pendiente", implementación clase viaje y enums para obtener salida y llegada del viaje
        self._facturasPasajeros = 1  # Número de facturas asociadas a pasajeros (para estadísticas)
        Factura.totalFacturas += 1  # Incrementa el número total de facturas
        Factura._facturasCreadas.append(self)  # Añade la factura a la lista de facturas creadas

    @multimethod
    def __init__(self, total: int, terminal: Terminal):
        """
        Constructor para la clase Factura, este objeto estará asociado con una transportadora.
        @param total: El valor total de la factura.
        @param terminal: La terminal donde se generó la factura.
        """
        self._numeroFactura = int(random.uniform(0, 10000))  # Genera un número de factura aleatorio
        self._total = total  # Valor total de la factura
        self._terminal = terminal  # Terminal asociada a la factura
        Factura.totalFacturas += 1  # Incrementa el número total de facturas
        Factura._facturasCreadas.append(self)  # Añade la factura a la lista de facturas creadas

    # Métodos getters y setters
    
    def getNumeroFactura(self):
        """
        Método para obtener el número de la factura.
        @return: Número de la factura.
        """
        return self._numeroFactura

    def setNumeroFactura(self, numeroFactura: int):
        """
        Establece o modifica el número de la factura.
        @param numeroFactura: El número de la factura.
        """
        self._numeroFactura = numeroFactura

    def getTotal(self):
        """
        Método para obtener el total de la factura.
        @return: Total de la factura.
        """
        return self._total

    def setTotal(self, total: float):
        """
        Establece o modifica el total de la factura.
        @param total: El total de la factura.
        """
        self._total = total

    @staticmethod
    def getTotalFacturas():
        """
        Método para obtener el número total de facturas creadas.
        @return: Número total de facturas.
        """
        return Factura.totalFacturas

    @staticmethod
    def getFacturasCreadas():
        """
        Método para obtener la lista de todas las facturas creadas.
        @return: Lista de facturas creadas.
        """
        return Factura._facturasCreadas
