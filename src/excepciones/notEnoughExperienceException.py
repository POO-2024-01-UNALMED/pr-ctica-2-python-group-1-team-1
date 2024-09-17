from src.excepciones.exceptionError1 import ExceptionError1
from tkinter import messagebox

class NotEnoughExperienceException(ExceptionError1):
    def __init__(self,conductorNombre):
        super().__init__()
        messagebox.showerror("Error al contratar", "No se puede contratar al conductor " + conductorNombre + " ya que tiene menos de 5 años de experiencia.")