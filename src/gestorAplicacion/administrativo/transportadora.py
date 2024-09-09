class Transportadora:
    _transportadoras = [] #No se utiliza

    def __init__(self, nombre, dinero, conductores, conductoresRegistrados, pasajeros, vehiculos,
                 viajesAsignados, destinoAsignado, terminal, taller, viajesTerminados, dueño, estrellas):
        self._nombre = nombre
        self._dinero = dinero
        self._conductores = conductores
        self._conductoresRegistrados = conductoresRegistrados
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


    def encontrarConductor(self,id):
        from gestorAplicacion.usuarios.conductor import Conductor
        for conductor in self._conductores:
            if (conductor.getId() == id):
                return conductor
        return None
    
    def transportadorasViaje(viajes):#Sacar tansportadoras sin repetir
        transportadoras = []

        for viaje in viajes:
            transportadora = viaje.getVehiculo().getTransportadora()
            if transportadora not in transportadoras:
                transportadoras.append(transportadora)
    
        return transportadoras

    def ejegirViajeTransportadora(self, viajes):
        """Método para elegir el primer viaje que encuentre con la misma transportadora"""

        for viaje in viajes:
            if viaje.getVehiculo().getTransportadora():
                return viaje

    
    def despedirConductor(self, id):
        from gestorAplicacion.usuarios.conductor import Conductor

        conductor : Conductor = self.encontrarConductor(id)

        if (len(conductor.getHorario()) == 0):
            
            if conductor.getVehiculo() is None:
                conductor.quitarVehiculo()
                conductor.getTransportadora().getConductores().remove(conductor)
                conductor.indemnizar()
                conductor.reinicioAtributos()
                return "Se ha despedido a " + conductor.getNombre()
            
            if len(conductor.getVehiculo().getConductores()) >= 2:
                conductor.quitarVehiculo()
                conductor.getTransportadora().getConductores().remove(conductor)
                conductor.indemnizar()
                conductor.reinicioAtributos()
                return "Se ha despedido a " + conductor.getNombre()
            else:
                return "No es posible porque no hay mas conductores asignados al vehiculo asociado al conductor"
            
        else:
            return "No es posible porque el conductor tiene viajes programados"

    def mostrarConductRegistrados(self):
        mensaje = ""
        for conductor in self._conductoresRegistrados:
            mensaje += "Nombre: " + conductor.getNombre() + "#Id: " + str(conductor.getId()) + "\n"


    def contratarConductorId(self, id: int):
        from gestorAplicacion.usuarios.conductor import Conductor
        conductor : Conductor = None

        for driver in self._conductoresRegistrados:

            if driver.getId() == id:
                index = self._conductoresRegistrados.index(driver)
                conductor = self._conductoresRegistrados[index]
        
        return Transportadora.contratarConductor(conductor)
    
    def contratarConductor(self, conductor):

        if conductor == None:
            return "No se ha encontrado el conductor"
        else:

            if (conductor.getExperiencia() >= 5):

                if (conductor.getEstadoLicencia()):
                    conductor.reinicioAtributos()
                    self.getConductores().append(conductor)
                    self.getConductoresRegistrados().remove(conductor)
                    conductor.bonoBienvenida(conductor.getTransportadora())
                    return "Se contrato a " + conductor.getNombre() + " exitosamente"
                else:
                    return "No se pudo contratar a " + conductor.getNombre() + " porque no tiene licencia activa"
            else:
                return "No se pudo contratar a " + conductor.getNombre() + " porque tiene menos de cinco años de experiencia"

    def encontrarViaje(self, id):

        for viaje in self._viajesAsignados:

            if (viaje.getId() == id):
                return viaje
        return None

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
    
    def getConductoresRegistrados(self):
        """Devuelve la lista de conductores registrados de la transportadora"""
        return self._conductoresRegistrados

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

    def setConductoresRegistrados(self, conductoresRegistrados):
        """Establece la lista de conductores registrados de la transportadora"""
        self._conductoresRegistrados = conductoresRegistrados

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