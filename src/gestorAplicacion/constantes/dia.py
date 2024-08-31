from enum import Enum

class Dia(Enum):
    # Días de la semana
    LUN = 1
    MAR = 2
    MIER = 3
    JUE = 4
    VIE = 5
    SAB = 6
    DOM = 7

    def __init__(self, value):
        self._value_ = value

    def getValue(self):
        return self.value