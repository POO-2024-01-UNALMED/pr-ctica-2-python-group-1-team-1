from src.excepciones.exceptionError1 import ExceptionError1
from tkinter import messagebox

class notLicenceException(ExceptionError1):
    def __init__(self,conductorNombre):
        super().__init__()
        messagebox.showerror("Error al contratar", "No se puede contratar a " + conductorNombre + " ya que tiene no tiene la licencia activa.")
