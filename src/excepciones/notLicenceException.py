from src.excepciones.exceptionError1 import exceptionError1
from tkinter import messagebox

class notLicenceException(exceptionError1):
    def __init__(self,conductorNombre):
        super().__init__("Error de contratacion")
        messagebox.showerror("Error al contratar", "No se puede contratar a " + conductorNombre + " ya que tiene no tiene la licencia activa.")
