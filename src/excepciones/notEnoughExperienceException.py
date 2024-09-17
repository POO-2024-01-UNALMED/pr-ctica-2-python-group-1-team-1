from src.excepciones.exceptionError1 import exceptionError1
from tkinter import messagebox

class notEnoughExperienceException(exceptionError1):
    def __init__(self,conductorNombre):
        super().__init__("Error de contratacion")
        messagebox.showerror("Error al contratar", "No se puede contratar al conductor " + conductorNombre + " ya que tiene menos de 5 años de experiencia.")