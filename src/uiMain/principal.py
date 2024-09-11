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

    # CREACIÓN DE LA PANTALLA DE INICIO (PRESENTACIÓN DEL SISTEMA)
    frame_top = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
    frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])

    # UBICACIÓN DE LOS FRAME PRINCIPALES
    frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    frame_bottom.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

    # AGREGAR LOS LABELS SUPERIORES
    label_top_left = tk.Label(frame_top, text="Hola Admin de Terminal Creations", font=("Segoe Script",40, "bold"), fg=colors["amarillo"], bd = 3, bg= colors["background"])
    label_top_right = tk.Label(frame_top, text = "TC", bd = 3, font=("Segoe Script", 60, "bold"), fg = colors["text"], bg = colors["background"])

    label_top_right.pack(side="left",padx=5, pady=5, expand=True, fill="y")
    label_top_left.pack(side="right", padx= 5, pady= 5, fill="both", expand=True)

    # DIVISIÓN FRAME INFERIOR EN DOS
    frame_bottom_left = tk.Frame(frame_bottom, bd = 3, bg=colors["background"])
    frame_bottom_right = tk.Frame(frame_bottom, bd = 3, bg=colors["background"])

    # UBICACIÓN DE LOS FRAME INFERIORES
    frame_bottom_left.pack(side="left", expand= True, fill="both" ,padx= 10, pady= 10)
    frame_bottom_right.pack(side="right", expand= True, fill="both", padx= 10, pady= 10)

    # AGREGAR LOS LABELS A CADA FRAME INFERIOR
    label_bottom_left_tp = tk.Label(frame_bottom_left, text="¿Cómo usar nuestro sistema?", font=("Small fonts",20), fg = colors["text"], bd =3, background=colors["naranja"])
    label_bottom_left_bt = tk.Label(frame_bottom_left, text="En nuestro sistema inteligente de podras administrar tu  terminal de\ntransportes dentro de las operaciones se encuentran la venta de viajes,\nfacturación y finanzas, gestión de conductores, talleres y vehiculos\npara la reparación de los mismos y programación y seguimientos de\nviajes. Tambien podrás consultar acerca de los desarrolladores en la\npestaña (Ayuda) del menu superior.", font=("Century",13), fg = colors["text"], bd =3, bg= colors["background"])

    label_bottom_right_tp = tk.Label(frame_bottom_right, text="¿Qué puede hacer?", font=("Small fonts",20), fg = colors["text"], bd =3, background=colors["naranja"])
    label_bottom_right_bt = tk.Label(frame_bottom_right, text="Para utilizar tus diferentes funcionalidades de administración debes\nir a la barra superior de menús, en la pestaña (Procesos y consultas)\nse desplegarán todas la operaciones que puedes realizar al seleccionar\nalguna de estas opciones se mostrará la interfaz respectiva, donde se\ndara una breve descripción y los diferentes formularios necesarios\npara la ejecución de la misma.\n\nRecuerda que en la pestaña (Archivo) tienes las opciones de (Aplicación)\nla cual te dara información acerca del sistema, y (Salir) te regresará al\na la ventana de Inicio.", font=("Century",13), fg = colors["text"], bd =3, bg= colors["background"])

    label_bottom_left_extra = tk.Label(frame_bottom_left, text="ESPACIO IMG", font=("Century", 11), fg=colors["text"], bd=3, bg=colors["background"], relief="solid")
    label_bottom_right_extra = tk.Label(frame_bottom_right, text="ESPACIO IMG", font=("Century", 11), fg=colors["text"], bd=3, bg=colors["background"], relief="solid")

    # UBICACIÓN LABEL INFERIOR IZQUIERDO
    label_bottom_left_tp.pack(side="top", padx=5, pady=10)
    label_bottom_left_bt.pack(side="top", padx=15, pady=15)
    label_bottom_left_extra.pack(side="top", padx=5, pady=10, expand=True, fill="both")

    # UBICACIÓN LABEL INFERIOR DERECHO 
    label_bottom_right_tp.pack(side="top", padx=5, pady=10)
    label_bottom_right_bt.pack(side="top", padx=15, pady=15)
    label_bottom_right_extra.pack(side="top", padx=5, pady=10, expand=True, fill="both")

def mensajeEmergente():
    messagebox.showinfo("Información básica", "Nuestra aplicación permite la gestion de una Terminal de Transporte...")

def mensajeAcerdade():
    messagebox.showinfo("Quienes somos", " Santiago Ochoa Cardona \n Johan Ramirez Marin \n Jaime Luis Osorio Gomez \n Juan Camilo Marin Valencia \n Jonathan David Osorio Restrepo")

def salir(ventanaPrincipal, ventanaInicio):
    ventanaPrincipal.destroy()
    ventanaInicio.deiconify()
