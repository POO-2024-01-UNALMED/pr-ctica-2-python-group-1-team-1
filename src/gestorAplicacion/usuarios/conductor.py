from persona import Persona

class Conductor(Persona):
    conductores = []

    def __init__(self, id, edad, nombre, genero, historial, experiencia, dinero, estadoLicencia, vehiculo, transportadora, horario, numeroDePagosRecibidos):
        super.__init__(id, edad, nombre, genero, historial, experiencia, dinero)
        self._estadoLicencia = estadoLicencia
        self._vehiculo = vehiculo
        self._transportadora = transportadora
        self._horario = horario
        self._numeroDePagosRecibidos = numeroDePagosRecibidos
        Conductor.conductores.append(self)


    def identificarse(self):
        pass


    def tomarVehiculo(self, vehiculo):
        """Metodo para asociar un conductor al vehiculo que
	    va de parametro si el vehiculo tiene menos de 3 conductores."""

        if (len(vehiculo.get_conductores) < 3):
            vehiculo.asociarConductor(self)
            self._vehiculo = vehiculo

    def tieneVehiculo(self):
        """Metodo para saber si el conductor tiene un vehiculo"""

        if (self._vehiculo == None):
            return False
        else:
            return True
        
    def indemnizar(self):
        """Metodo para indemnizar el conductor al despedirlo"""
        self._dinero = (self.diasTrabajados * 0.5)

    def sumerUnDiaTrabajado(self):
        """Metodo para agregarle un dia trabajado al conductor"""
        self.diasTrabajados += 1

    def reinicioAtributos(self):
        """Metodo para reiniciar algunos atributos del conductor, 
	    este se usara cuando se despida o contrate un conductor
	    para que no haya errores en un futuro"""
        self.horario = []
        self.diasRestantesContrato = 0
        self.diasTrabajados = 0
        self.historial = []

    def desvincularYVincular(self, conductor, viaje):
        """Metodo para desvincular un viaje al conductor que invoco el metodo
	    y vincular el viaje al conductor que va de parametro"""
        conductor.get_horario().append(viaje)
        viaje.set_conductor(conductor)
        viaje.set_vehiculo(conductor.get_vehiculo())
        self.get_horario().remove(viaje)

    def vincularYDesvincular(self, conductor, viaje):
        """Metodo para vincular un viaje al conductor que invoco el metodo
	    y desvincular el viaje al conductor que va de parametro"""
        self.get_horario().append(viaje)
        viaje.set_conductor(self)
        viaje.set_vehiculo(self.get_vehiculo)
        conductor.get_horario().remove(viaje)


    #Getters and setters

    def bonoBienvenida(transportadora):
        """Metodo que le da un bono de bienvenida al conductor contratado"""

    def set_estado_licencia(self, estado_licencia):
        """Establece o modifica el estado de la licencia del conductor."""
        self.estado_licencia = estado_licencia

    def get_estado_licencia(self):
        """Obtiene el estado de la licencia del conductor."""
        return self.estado_licencia

    def set_vehiculo(self, vehiculo):
        """Establece o modifica el vehículo asociado al conductor."""
        self.vehiculo = vehiculo

    def get_vehiculo(self):
        """Obtiene el vehículo asociado al conductor."""
        return self.vehiculo

    def set_transportadora(self, transportadora):
        """Establece o modifica la transportadora vinculada al conductor."""
        self.transportadora = transportadora

    def get_transportadora(self):
        """Obtiene la transportadora vinculada al conductor."""
        return self.transportadora

    def set_horario(self, horario):
        """Establece o modifica el listado con el horario asociado al conductor."""
        self.horario = horario

    def get_horario(self):
        """Obtiene el listado con el horario del conductor."""
        return self.horario

    def get_numeroDePagosRecibidos(self):
        """Obtiene el número de pagos recibidos por el conductor."""
        return self._numeroDePagosRecibidos
    
    @staticmethod
    def getConductores():
        """Obtiene la lista de todos los conductores."""
        return Conductor.conductores