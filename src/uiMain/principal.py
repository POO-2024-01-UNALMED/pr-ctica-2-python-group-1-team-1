import tkinter as tk
from tkinter import messagebox


# PALETA DE COLORES
colors = {
        "background": "#0c1424",
        "text": "#f5f5f5",
        "naranja": "#ff350a",
        "amarillo": "#ffbf00",
        "grisClaro": "#d1d1d1",
        "grisOscuro": "#4a5568",
        "azul" : "#2d9bfb",
        "accent": "#2e3b49"
}

def interfazPrincipal(ventanaInicio):
    """
    Genera la interfaz de usuario para el menú principal.
    """
    ventanaInicio.withdraw()

    ventanaPrincipal = tk.Toplevel(ventanaInicio)
    ventanaPrincipal.title("Sistema Inteligente de Administración y Seguimiento de la Terminal")
    ventanaPrincipal.iconbitmap("src/imagenes/logo.ico")
    ventanaPrincipal.geometry("1400x800") # RESOLUCIÓN POR DEFECTO

    # CREACIÓN DE LA BARRA DE MENU
    menuBar = tk.Menu(ventanaPrincipal)
    ventanaPrincipal.config(menu=menuBar)

    menuArchivo = tk.Menu(menuBar, tearoff=False,bg="white")
    menuBar.add_cascade(menu=menuArchivo, label="Archivo")
    menuArchivo.add_command(label="Aplicacion", command= mensajeEmergente)
    menuArchivo.add_command(label="Salir", command= lambda: salir(ventanaPrincipal, ventanaInicio))

    menuConsultas = tk.Menu(menuBar, tearoff=False,bg="white")
    menuBar.add_cascade(menu=menuConsultas, label="Procesos y Consultas")
    menuConsultas.add_command(label="Venta de Viajes")
    menuConsultas.add_command(label="Facturacion y Finanzas")
    menuConsultas.add_command(label="Conductores y Vehiculos")
    menuConsultas.add_command(label="Talleres y Mecanicos")
    menuConsultas.add_command(label="Programación de Viajes")

    menuAyuda = tk.Menu(menuBar, tearoff=False,bg= "white")
    menuBar.add_cascade(menu=menuAyuda, label="Ayuda")
    menuAyuda.add_command(label="Acerca de", command=mensajeAcerdade)

def mensajeEmergente():
    messagebox.showinfo("Información básica", "Nuestra aplicación permite la gestion de una Terminal de Transporte...")

def mensajeAcerdade():
    messagebox.showinfo("Quienes somos", " Santiago Ochoa Cardona \n Johan Ramirez Marin \n Jaime Luis Osorio Gomez \n Juan Camilo Marin Valencia \n Jonathan David Osorio Restrepo")

def salir(ventanaPrincipal, ventanaInicio):
    ventanaPrincipal.destroy()
    ventanaInicio.deiconify()
