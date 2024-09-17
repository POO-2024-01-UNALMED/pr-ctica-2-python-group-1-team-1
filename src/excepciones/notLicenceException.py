from src.excepciones.exceptionError1 import ExceptionError1
from tkinter import messagebox

class notLicenceException(ExceptionError1):
    def __init__(self,conductorNombre):
        mensaje = conductorNombre + " no tiene la licencia activa."
        super().__init__(mensaje)
       
