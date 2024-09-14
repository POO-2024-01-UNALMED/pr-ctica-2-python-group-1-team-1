from tkinter import messagebox

class ErrorAplicacion(Exception):
    
    def __init__(self, msg):
        
        self.msg = msg
        messagebox.showerror("Alerta!",f" Manejo de errores de la aplicacion: {msg}")
    