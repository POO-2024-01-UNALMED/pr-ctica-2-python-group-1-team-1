from src.excepciones.exceptionError2 import ExceptionError2
from tkinter import messagebox

class NoViajesErrorTipoPasajero(ExceptionError2):
    def __init__(self, tipoPasajero):
        super().__init__(f"No hay viajes para este tipo Pasajero {tipoPasajero.name}")
        messagebox.showinfo("Sin viajes disponibles", f"No hay viajes disponibles para este tipo de pasajero{tipoPasajero.name}")