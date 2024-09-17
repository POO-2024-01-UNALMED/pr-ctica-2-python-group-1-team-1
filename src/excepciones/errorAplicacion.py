from tkinter import messagebox

class ErrorAplicacion(Exception):
    
    def __init__(self, msg=""):
        
        self.msg = msg
        messagebox.showerror("Manejo de errores","Manejo de errores de la Aplicación: " + msg)

    