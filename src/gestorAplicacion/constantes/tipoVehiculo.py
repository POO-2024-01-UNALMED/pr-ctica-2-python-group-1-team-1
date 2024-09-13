from enum import Enum

# Enumeración que representa los tipos de vehículos que pueden estar asociados a la terminal
# y la respectiva capacidad de pasajeros según su tipo.
class TipoVehiculo(Enum):
    BUS = 42
    TAXI = 4
    VANS = 15
    ESCALERA = 50

    # Constructor para la clase TipoVehiculo.
    # @param capacidad, la capacidad asociada según el tipo de vehículo.
    def __init__(self, capacidad):
        self.capacidad = capacidad

    # Método para obtener la capacidad en base a un vehículo.
    # @return la capacidad respectiva del vehículo.
    def getCapacidad(self):
        return self.capacidad