from persona import Persona 
class Pasajero(Persona):
    def __init__(self,tipo, id, edad, nombre):
        self._tipoPasajero = tipo
        self._viaje = None
        super.__init__(id, edad, nombre)
    
    
    
    def nuevoPasajero(self, tipo, id, edad, nombre):
        return Pasajero(tipo, id, edad, nombre)
    
    # Método get para el atributo _tipoPasajero
    def getTipoPasajero(self):
        """Devuelve el tipo de pasajero."""
        return self._tipoPasajero

    # Método set para el atributo _tipoPasajero
    def setTipoPasajero(self, tipo):
        """Establece el tipo de pasajero."""
        self._tipoPasajero = tipo

    # Método get para el atributo viaje
    def getViaje(self):
        """Devuelve el viaje asociado al pasajero."""
        return self._viaje

    # Método set para el atributo viaje
    def setViaje(self, viaje):
        """Establece el viaje asociado al pasajero."""
        self._viaje = viaje