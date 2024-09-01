from enum import Enum

class TipoPasajero(Enum):
    # Tipos de pasajeros con sus descuentos asociados
    ESTUDIANTE = 0.5
    DISCAPACITADO = 0.25
    REGULAR = 0.1
    VIP = 0

    def getDescuento(self):
        """Devuelve el descuento asociado al tipo de pasajero."""
        return self.value
