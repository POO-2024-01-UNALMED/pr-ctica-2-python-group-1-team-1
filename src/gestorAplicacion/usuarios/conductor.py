# SOLUCIÓN IMPORTACIONES --------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#--------------------------------------------------------------------------------------

from gestorAplicacion.usuarios.persona import Persona

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

        if (len(vehiculo.getConductores) < 3):
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
        self._diasTrabajados += 1

    def reinicioAtributos(self):
        """Metodo para reiniciar algunos atributos del conductor, 
	    este se usara cuando se despida o contrate un conductor
	    para que no haya errores en un futuro"""
        self._horario = []
        self._diasRestantesContrato = 0
        self._diasTrabajados = 0
        self._historial = []

    def desvincularYVincular(self, conductor, viaje):
        """Metodo para desvincular un viaje al conductor que invoco el metodo
	    y vincular el viaje al conductor que va de parametro"""
        conductor.getHorario().append(viaje)
        viaje.setConductor(conductor)
        viaje.setVehiculo(conductor.getVehiculo())
        self.getHorario().remove(viaje)

    def vincularYDesvincular(self, conductor, viaje):
        """Metodo para vincular un viaje al conductor que invoco el metodo
	    y desvincular el viaje al conductor que va de parametro"""
        self.getHorario().append(viaje)
        viaje.setConductor(self)
        viaje.setVehiculo(self.getVehiculo())
        conductor.getHorario().remove(viaje)

    def quitarVehiculo(self):
        """Metodo para quitar el vehiculo si no tiene viajes programados"""

        if (len(self._horario) == 0):

            if (len(self._vehiculo().getConductores()) >= 2):
                self._vehiculo.quitarVehiculo(self.id)
                self._vehiculo = None
                return "Se ha desvinculado el vehiculo a " + self.nombre
            else:
                return "No se ha podido desvincular el vehiculo a " + self.nombre
        else:
            return "No se ha podido desvincular el vehiculo a " + self.nombre
        
    def mostrarViajes(self):
        mensaje = ""
        for viaje in self.getHorario(): 
            mensaje += "\n" + viaje.detallesViaje()
        
        return mensaje
    
    def tieneVehiculo(self):
        """Metodo para saber si el conductor tiene un vehiculo"""
        if self.getVehiculo() == None:
            return False
        else:
            return True
    

    def bonoBienvenida(transportadora):
        """Metodo que le da un bono de bienvenida al conductor contratado"""

    #Getters and setters

    def setEstadoLicencia(self, estadoLicencia):
        """Establece o modifica el estado de la licencia del conductor."""
        self._estadoLicencia = estadoLicencia

    def getEstadoLicencia(self):
        """Obtiene el estado de la licencia del conductor."""
        return self._estadoLicencia

    def setVehiculo(self, vehiculo):
        """Establece o modifica el vehículo asociado al conductor."""
        self._vehiculo = vehiculo

    def getVehiculo(self):
        """Obtiene el vehículo asociado al conductor."""
        return self._vehiculo

    def setTransportadora(self, transportadora):
        """Establece o modifica la transportadora vinculada al conductor."""
        self._transportadora = transportadora

    def getTransportadora(self):
        """Obtiene la transportadora vinculada al conductor."""
        return self._transportadora

    def setHorario(self, horario):
        """Establece o modifica el listado con el horario asociado al conductor."""
        self._horario = horario

    def getHorario(self):
        """Obtiene el listado con el horario del conductor."""
        return self._horario
    
    def setNumeroDePagosRecibidos(self, numeroDePagosRecibidos):
        """Establece el número de pagos recibidos por el conductor."""
        self._numeroDePagosRecibidos = numeroDePagosRecibidos

    def getNumeroDePagosRecibidos(self):
        """Obtiene el número de pagos recibidos por el conductor."""
        return self._numeroDePagosRecibidos
    
    @classmethod
    def getConductores(cls):
        """Obtiene la lista de todos los conductores."""
        return Conductor.conductores