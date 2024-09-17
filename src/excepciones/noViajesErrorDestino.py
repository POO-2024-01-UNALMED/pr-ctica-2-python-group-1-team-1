from src.excepciones.exceptionError2 import ExceptionError2
from tkinter import messagebox

class NoViajesErrorDestino(ExceptionError2):
    def __init__(self, destino):
        super().__init__(f"No hay viajes para este destino{destino}")
        messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponibles para este destino")