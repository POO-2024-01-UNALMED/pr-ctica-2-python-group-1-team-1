# Faltan las importaciones
from enum import Enum

class Destino(Enum):
    # Destinos Cercanos
    MEDELLIN = (0, 0)
    COOPACABANA = (0, 18)
    BELLO = (0, 10)
    ITAGUI = (0, -11)
    ENVIGADO = (0, -10)
    LAPINTADA = (60, -53)
    GUARNE = (33, 0)
    ANGELOPOLIS = (-45.8, 20)
    BARBOSA = (0, 42)
    RIONEGRO = (36, -5)
    CALDAS = (0, -22)
    GUATAPE = (79.6, -10)
    MARINILLA = (50, 0)
    SABANETA = (0, -14)
    LAESTRELLA = (0, -16)
    GIRARDOTA = (-23, 0)
    
    # Destinos Lejanos
    CARTAGENA = (151.24, 634.2)
    SANTAMARTA = (354.22, 750.63)
    BARRANQUILLA = (253.54, 384.56)
    LAGUAJIRA = (523, 840)
    BOGOTA = (398.49, -126.28)
    CALI = (-351.49, -267.65)
    BUENAVENTURA = (-429.95, -226.75)
    BUCARAMANGA = (325.52, 229)
    
    # Inicializador
    def __init__(self, ejeX, ejeY):
        self.ejeX = ejeX
        self.ejeY = ejeY

    """
        Método para obtener la coordenada en X asociada a un destino.
        Returns:
            La coordenada en X asociada al destino.
    """
    def getEjeX(self):
        return self.ejeX

    """
        Método para obtener la coordenada en Y asociada a un destino.
        Returns:
            La coordenada en Y asociada al destino.
    """
    def getEjeY(self):
        return self.ejeY

    """
        Metodo para ver si el string que se ingresa puede convertirse en uno de los destinos.
        Returns:
            False or True, según sea el caso.
    """
    @staticmethod
    def esDestinoValido(destinoDeseado):
        return destinoDeseado in Destino.__members__