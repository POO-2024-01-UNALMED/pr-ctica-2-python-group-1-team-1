from persona import Persona 
from gestorAplicacion.constantes.incentivo import Incentivo
class Pasajero(Persona, Incentivo):
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
    
    def descuento(self):
        
        dineroTransportadora = self.getViaje().getTransportadora().getDinero()
        self._viaje.getTransportadora().setDinero(dineroTransportadora - 50)
    
    def bonificacion(self):
        
        if (self.verificarBonificacion() == 0):
            
            self._dinero += 0
        
        elif (self.verificarBonificacion() == 5):
            
            self._dinero += Incentivo.INCENTIVOBASE
            dineroTrans = self._viaje.getTransportadora().getDinero()
            dineroTransportadoraluegoDeIncentivo = dineroTrans - Incentivo.INCENTIVOBASE
            self._viaje.getTransportadora().setDinero(dineroTransportadoraluegoDeIncentivo)
            
        
        elif (self.verificarBonificacion() == 10):
            
            self._dinero += Incentivo.INCENTIVOBASE * 2
            dineroTrans = self._viaje.getTransportadora().getDinero()
            dineroTransportadoraluegoDeIncentivo = dineroTrans - (Incentivo.INCENTIVOBASE * 2)
            self._viaje.getTransportadora().setDinero(dineroTransportadoraluegoDeIncentivo)
            
        self._dinero += Incentivo.INCENTIVOBASE * 3
        dineroTrans = self._viaje.getTransportadora().getDinero()
        dineroTransportadoraluegoDeIncentivo = dineroTrans - (Incentivo.INCENTIVOBASE * 2)
        self._viaje.getTransportadora().setDinero(dineroTransportadoraluegoDeIncentivo)

    def verificarBonificacion(self):
        
        viajesMismaTransportadora = 0
        
        for v in self.getHistorial():
            
            if (v.getTransportadora().getNombre() == self._viaje.getTransportadora().getNombre()):
                
                viajesMismaTransportadora += 1

        return viajesMismaTransportadora
        
        
        