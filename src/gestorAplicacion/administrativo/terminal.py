# Importaciones: 

class Terminal:
    # Atributos de clase
    cantidadSedes = 0
    transportadoras  = []
    reservas = []
    viajes = []
    viajesEnCurso = []
    historial = []
    facturas = []
    pasajeros = []
    listaTerminales = [] # Para serializar
    
    # Inicializador
    def __init__(self, nombre, dinero, capacidadVehiculos, transportadoras, viajes, viajesEnCurso, destinos, comision, ubicacion, administrador):
        self._nombre = nombre
        self._dinero = dinero
        self._capacidadVehiculos = capacidadVehiculos
        Terminal.transportadoras = transportadoras
        Terminal.viajes = viajes
        Terminal.viajesEnCurso = viajesEnCurso
        Terminal._reservas = []
        Terminal._historial = []
        self._destinos = destinos # Propios de cada terminal
        self.vehiculosTerminal = [] # Propios de cada terminal
        self._comision = comision
        self._ubicacion = ubicacion
        self._administrador = administrador
        Terminal.cantidadSedes += 1

    # Sobrecarga de Inicializadores (Sin administrador)
    def __init__(self, nombre, dinero, capacidadVehiculos, transportadoras, viajes, viajesEnCurso, destinos, comision, ubicacion):
        self._nombre = nombre
        self._dinero = dinero
        self._capacidadVehiculos = capacidadVehiculos
        Terminal.transportadoras = transportadoras
        Terminal.viajes = viajes
        Terminal.viajesEnCurso = viajesEnCurso
        Terminal._reservas = []
        Terminal._historial = []
        self._destinos = destinos # Propios de cada terminal
        self.vehiculosTerminal = [] # Propios de cada terminal
        self._comision = comision
        self._ubicacion = ubicacion
        Terminal.cantidadSedes += 1

    def transportadorasViajeDisponible():
        pass

    def obtenerTransportadorasUnicas():
        pass

    def viajesDestino():
        pass

    def transportadorasViajeDisponible(self): # SA
        pass

    def viajesDisponibles(): # Para que se usa???
        pass

    def masRapido():
        pass

    def obtenerViajeMasProximo():
        pass

    def masEconomico():
        pass

    def viajesParaRegularesYDiscapacitados():
        pass

    # Sobrecarga
    def viajesParaRegularesYDiscapacitados():
        pass

    def viajesParaVips():
        pass

    # Sobrecarga
    def viajesParaVips():
        pass

    def viajesParaEstudiantes():
        pass

    # Sobrecarga
    def viajesParaEstudiantes():
        pass

    # Programación por Vehiculo ()
    def programarViaje():
        pass

    # Programación por Conductor ()
    def programarViaje():
        pass

    def cancelarViajeAbsoluto():
        pass

    def cancelarViaje():
        pass

    def consultarCapacidad():
        pass

    def denegarReserva():
        pass

    def calcularGanancias():
        pass

    def agregarVehiculoTerminal():
        pass

    def removerVehiculoTerminal():
        pass

    def fechasDisponibles():
        pass

    def horasDisponibles():
        pass

    # Métodos Get y Set

    # Get y Set para nombre
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    # Get y Set para dinero
    def getDinero(self):
        return self._dinero
    
    def setDinero(self, dinero):
        self._dinero = dinero

    # Get y Set para capacidad de vehículos
    def getCapacidadVehiculos(self):
        return self._capacidadVehiculos
    
    def setCapacidadVehiculos(self, capacidadVehiculos):
        self._capacidadVehiculos = capacidadVehiculos

    # Get y Set para destinos
    def getDestinos(self):
        return self._destinos
    
    def setDestinos(self, destinos):
        self._destinos = destinos

    # Get y Set para comisión
    def getComision(self):
        return self._comision
    
    def setComision(self, comision):
        self._comision = comision

    # Get y Set para ubicación
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    # Get y Set para administrador
    def getAdministrador(self):
        return self._administrador
    
    def setAdministrador(self, administrador):
        self._administrador = administrador

    @classmethod
    def getTransportadoras(cls):
        return cls.transportadoras

    @classmethod
    def setTransportadoras(cls, transportadoras):
        cls.transportadoras = transportadoras

    @classmethod
    def getViajes(cls):
        return cls.viajes

    @classmethod
    def setViajes(cls, viajes):
        cls.viajes = viajes

    @classmethod
    def getViajesEnCurso(cls):
        return cls.viajesEnCurso

    @classmethod
    def setViajesEnCurso(cls, viajesEnCurso):
        cls.viajesEnCurso = viajesEnCurso

    @classmethod
    def getReservas(cls):
        return cls.reservas

    @classmethod
    def setReservas(cls, reservas):
        cls.reservas = reservas

    @classmethod
    def getHistorial(cls):
        return cls.historial

    @classmethod
    def setHistorial(cls, historial):
        cls.historial = historial

    @classmethod
    def getFacturas(cls):
        return cls.facturas

    @classmethod
    def setFacturas(cls, facturas):
        cls.facturas = facturas

    @classmethod
    def getPasajeros(cls):
        return cls.pasajeros

    @classmethod
    def setPasajeros(cls, pasajeros):
        cls.pasajeros = pasajeros

    @classmethod
    def getListaTerminales(cls):
        return cls.listaTerminales

    @classmethod
    def setListaTerminales(cls, listaTerminales):
        cls.listaTerminales = listaTerminales
