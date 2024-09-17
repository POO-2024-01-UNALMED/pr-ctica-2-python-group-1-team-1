from src.excepciones.exceptionError2 import ExceptionError2
from tkinter import messagebox

class NoViajesErrorModalidad(ExceptionError2):
    def __init__(self, modalidad):
        super().__init__(f"No hay viajes Disponibles {modalidad}")
