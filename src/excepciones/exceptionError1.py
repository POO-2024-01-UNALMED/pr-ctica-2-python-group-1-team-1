from src.excepciones.errorAplicacion import ErrorAplicacion
from tkinter import messagebox

class ExceptionError1(ErrorAplicacion):
    
    def __init__(self,mensaje):
        msg= "Error de verificacion de atributos: " + mensaje
        super().__init__(msg)
        

    def mensaje(self):
        
        print("prueba")

if __name__ == "__main__":
    
    try:
        raise ExceptionError1()
    
    except ExceptionError1 as f:
        
        f.mensaje()