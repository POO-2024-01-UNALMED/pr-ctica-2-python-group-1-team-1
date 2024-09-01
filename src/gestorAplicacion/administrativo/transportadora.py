class Transportadora:
    _transportadoras = [] #No se utiliza

    def __init__(self, nombre, dinero, conductores, pasajeros, vehiculos,
                 viajesAsignados, destinoAsignado, terminal, taller, viajesTerminados, dueño, estrellas):
        self._nombre = nombre
        self._dinero = dinero
        self._conductores = conductores
        self._pasajeros = pasajeros
        self._vehiculos = vehiculos
        self._viajesAsignados = viajesAsignados
        self._destinoAsignado = destinoAsignado
        self._terminal = terminal
        self._taller = taller
        self._viajesTerminados = viajesTerminados
        self._dueño = dueño
        self._estrellas = estrellas
        Transportadora._transportadoras.append(self)
        self._conductoresDespedidos = []


    # Métodos get

    # Devuelve el nombre de la transportadora
    def getNombre(self):
        return self._nombre

    # Devuelve el dinero disponible de la transportadora
    def getDinero(self):
        return self._dinero

    # Devuelve la lista de conductores de la transportadora
    def getConductores(self):
        return self._conductores

    # Devuelve la lista de pasajeros de la transportadora
    def getPasajeros(self):
        return self._pasajeros

    # Devuelve la lista de vehículos de la transportadora
    def getVehiculos(self):
        return self._vehiculos

    # Devuelve la lista de viajes asignados a la transportadora
    def getViajesAsignados(self):
        return self._viajesAsignados

    # Devuelve el destino asignado a la transportadora
    def getDestinoAsignado(self):
        return self._destinoAsignado

    # Devuelve la terminal de la transportadora
    def getTerminal(self):
        return self._terminal

    # Devuelve el taller asignado a la transportadora
    def getTaller(self):
        return self._taller

    # Devuelve la lista de viajes terminados por la transportadora
    def getViajesTerminados(self):
        return self._viajesTerminados

    # Devuelve el nombre del dueño de la transportadora
    def getDueño(self):
        return self._dueño

    # Devuelve la calificación en estrellas de la transportadora
    def getEstrellas(self):
        return self._estrellas
    
    @classmethod
    def getTransportadoras(cls):
        """Devuelve la lista de todas las instancias de Transportadora."""
        return cls._transportadoras

    # Métodos set

    # Establece el nombre de la transportadora
    def setNombre(self, nombre):
        self._nombre = nombre

    # Establece el dinero disponible de la transportadora
    def setDinero(self, dinero):
        self._dinero = dinero

    # Establece la lista de conductores de la transportadora
    def setConductores(self, conductores):
        self._conductores = conductores

    # Establece la lista de pasajeros de la transportadora
    def setPasajeros(self, pasajeros):
        self._pasajeros = pasajeros

    # Establece la lista de vehículos de la transportadora
    def setVehiculos(self, vehiculos):
        self._vehiculos = vehiculos

    # Establece la lista de viajes asignados a la transportadora
    def setViajesAsignados(self, viajesAsignados):
        self._viajesAsignados = viajesAsignados

    # Establece el destino asignado a la transportadora
    def setDestinoAsignado(self, destinoAsignado):
        self._destinoAsignado = destinoAsignado

    # Establece la terminal de la transportadora
    def setTerminal(self, terminal):
        self._terminal = terminal

    # Establece el taller asignado a la transportadora
    def setTaller(self, taller):
        self._taller = taller

    # Establece la lista de viajes terminados por la transportadora
    def setViajesTerminados(self, viajesTerminados):
        self._viajesTerminados = viajesTerminados

    # Establece el nombre del dueño de la transportadora
    def setDueño(self, dueño):
        self._dueño = dueño

    # Establece la calificación en estrellas de la transportadora
    def setEstrellas(self, estrellas):
        self._estrellas = estrellas

    @classmethod
    def setTransportadoras(cls, transportadoras):
        """Establece la lista de instancias de Transportadora."""
        cls._transportadoras = transportadoras