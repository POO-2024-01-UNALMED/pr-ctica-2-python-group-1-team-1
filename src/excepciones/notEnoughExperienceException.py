from src.excepciones.exceptionError1 import ExceptionError1
from tkinter import messagebox

class NotEnoughExperienceException(ExceptionError1):
    def __init__(self,conductorNombre):
        mensaje = conductorNombre + " tiene menos de 5 años de experiencia."
        super().__init__(mensaje)
