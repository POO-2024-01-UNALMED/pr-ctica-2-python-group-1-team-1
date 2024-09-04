import tkinter as tk
from tkinter import messagebox

def mostrarDescripcion():
    label_frame_top.config(text= "Bienvenido al Sistema de Administración Inteligente de Terminales de Transporte.\n Donde los viajes que salen nunca terminan...", font = "Impact")

# Funcion para Salir de la aplicación
def salir():
    root.quit()

# CREAR OBJETO DE TIPO VENTANA
root = tk.Tk()

# MODIFICACIONES A LA VENTANA
root.title("Terminal Creations")
root.iconbitmap("src/imagenes/logo.ico")
root.geometry("1400x800") # RESOLUCIÓN POR DEFECTO

# INSTANCIAR UN OBJETO DE TIPO MENU
menu_bar = tk.Menu()

#ASOCIAR LA BARRA DE MENU CON LA VENTANA PRINCIPAL
root.config(menu= menu_bar)

menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label = "Opciones", menu = menu_opciones)
menu_opciones.add_command(label= "Descripcion", command= mostrarDescripcion)
menu_opciones.add_separator()
menu_opciones.add_command(label= "Salir", command=salir)

# IMAGENES
# VARIABLES PARA CAMBIAR LAS DESCRIPCIONES DE LAS HOJAS DE VIDA E IMAGENES.
valores = ["Hoja Vida 1 = Santiago", "Hoja Vida 2 = Jaime", "Hoja Vida 3 = Juan Camilo", "Hoja Vida 4 = Jhonatan", "Hoja Vida 5 = Johan"] # En nuestro caso serian los String
imagenes = ["src/imagenes/developers/foto1.png", "src/imagenes/developers/foto2.png", "src/imagenes/developers/foto3.png", "src/imagenes/developers/foto4.png", "src/imagenes/developers/foto1.png"]
photoImagenes = [tk.PhotoImage(file = imagen) for imagen in imagenes] # GUARDAR LAS IMAGENES COMO OBJETOS DE PhotoImage

indice_valor = 0 # Todo se indexa desde 0
indice_mouse = 0

def cambiar_valor_color():
    global indice_valor

    # VAMOS A CAMBIAR EL TEXTO (HOJA DE VIDA) FRAME SUPERIOR DERECHO
    boton_right_top.config(text = valores[indice_valor], font= ("Century", 15))

    # AUMENTAR EL SIGUIENTE VALOR DE LA LISTA
    indice_valor = (indice_valor + 1) % len(valores)

    # CAMBIAR LAS IMAGENES DE CADA SUB-FRAME DENTRO DE P6
    label_rb_tl.config(image = photoImagenes[indice_valor])
    label_rb_br.config(image = photoImagenes[(indice_valor+1) % len(photoImagenes)])
    label_rb_bl.config(image = photoImagenes[(indice_valor+2) % len(photoImagenes)])
    label_rb_tr.config(image = photoImagenes[(indice_valor+3) % len(photoImagenes)])

def cambiarImagen():
    """
        Cambia las imagenes del sistema al pasar el mouse
    """
    global indice_mouse
    boton_left_top.config(image = photoInicio[indice_mouse])
    indice_mouse = (indice_mouse + 1)% len(photoInicio)


# VARIABLES PARA CAMBIAR LAS IMAGENES DEL INICIO AL SISTEMA
imagenesInicio = ["src/imagenes/inicio/banner1.png","src/imagenes/inicio/banner2.png", "src/imagenes/inicio/banner3.png", "src/imagenes/inicio/banner4.png", "src/imagenes/inicio/banner5.png"]
photoInicio = [tk.PhotoImage(file = imagen) for imagen in imagenesInicio] # GUARDAR LAS IMAGENES COMO OBJETOS DE PhotoImage
# FALTA BUSCAR LA MANERA DE REDIMENSIONAR



# DISTRIBUCIÓN DE LA VENTANA EN LOS FRAME SOLICITADOS
# GENERACIÓN DE LOS CONTENEDORES PRINCIPALES
frame_left = tk.Frame(root, bg = "blue", bd = 0, relief="sunken")
frame_right = tk.Frame(root, bg = "blue", bd = 0, relief="sunken")

#EMPAQUETAR LOS FRAME PRINCIPALES P1,P2 EN LA VENTANA
#frame_left.pack(side = "left", expand = True, fill = "both", padx = 5, pady = 5) # FORMA DAVID
#frame_right.pack(side = "right", expand = True, fill = "both", padx = 5, pady = 5) # FORMA DAVID
frame_left.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = "e")
frame_right.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = "w")

# CREACIÓN DE P3 y P4
frame_left_top = tk.Frame(frame_left, bg = "#0c1424", bd = 2, relief = "solid")
frame_left_bottom = tk.Frame(frame_left, bg = "#0c1424", bd = 2, relief = "solid")

# DEBO DAR LA UBICACIÓN DEL FRAME P3 y P4
#frame_left_top.pack(side = "top", expand = True, fill = "both", padx= 5, pady = 5) # FORMA DAVID
#frame_left_bottom.pack(side = "bottom", expand = True, fill = "both", padx= 5, pady = 5) # FORMA DAVID
frame_left_top.place(relx=0, rely=0, relwidth=1, relheight=0.2)
frame_left_bottom.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
frame_left_bottom.bind("<Enter>", lambda event: cambiarImagen()) # PERMITE CAMBIAR LA IMAGEN CUANDO EL MOUSE ENTRA Y SALE DEL FRAME

# CREACIÓN DE P5 Y P6
frame_right_top = tk.Frame(frame_right, bg = "#0c1424", bd = 2, relief = "solid")
frame_right_bottom = tk.Frame(frame_right, bg = "#0c1424", bd = 2, relief = "solid")

# UBICACIÓN
#frame_right_top.pack(side = "top", expand = True, fill = "both", padx= 5, pady = 5)
#frame_right_bottom.pack(side = "bottom", expand = True, fill = "both", padx= 5, pady = 5)
frame_right_top.place(relx=0, rely=0, relwidth=1, relheight=0.3)
frame_right_bottom.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

# PARA DESCRIPCION, en los frame se pueden meter etiquetas ls cuales tienen texto. 
label_frame_top = tk.Label(frame_left_top, text="Bienvenido a Terminal Creations, donde podras llevar el control\n de tu terminal a un solo clic...", fg = "white", font= ("Century", 15), bg = "#0c1424")
label_frame_top.pack(expand=True, fill="both", padx=5, pady=5)

# BOTON PARA CAMBIAR LAS HOJAS DE VIDA
boton_right_top = tk.Button(frame_right_top, bg = "#0c1424", text = "Hojas de Vida de los Desarrolladores", fg = "white" ,font= ("Century", 24), relief = "solid", command=cambiar_valor_color)
boton_right_top.pack(expand=True, fill="both", padx=7, pady=7)

# BOTONES ASOCIADO AL INGRESO AL SISTEMA
boton_left_bottom = tk.Button(frame_left_bottom, bg = "black", text = "Administrar Terminal", fg = "lightblue" ,font = ("Century", 15), relief = "groove")
boton_left_bottom.pack(side = "bottom", pady = 5)
boton_left_bottom.bind("<Button-1>", lambda e : Main().interfazPrincipal()) # PASA A GENERAR LA NUEVA VENTANA DEL SISTEMA

# BOTONES ASOCIADO AL INGRESO AL CAMBIO DE IMAGEN
boton_left_top = tk.Button(frame_left_bottom, image = photoInicio[0])
boton_left_top.pack(side = "top", expand = True, pady = 5)
#boton_left_top.bind("<Enter>", lambda event: cambiarImagen()) # MEJOR LLAMARLO DESDE EL FRAME

# EL FRAME INFERIOR DERECHO (P6), DIVIDIRLO EN 4, 2FIL, 2COL
frame_right_bottom.grid_rowconfigure(0, weight=1)
frame_right_bottom.grid_rowconfigure(1, weight=1)
frame_right_bottom.grid_columnconfigure(0, weight=1)
frame_right_bottom.grid_columnconfigure(1, weight=1)

# CREAR LOS SUB-FRAME DE P6
frame_rb_tl = tk.Frame(frame_right_bottom, bg = "lightblue", bd = 1, relief="sunken")
frame_rb_tr = tk.Frame(frame_right_bottom, bg = "lightblue", bd = 1, relief="sunken")
frame_rb_bl = tk.Frame(frame_right_bottom, bg = "lightblue", bd = 1, relief="sunken")
frame_rb_br = tk.Frame(frame_right_bottom, bg = "lightblue", bd = 1, relief="sunken")

# UBICAR LOS SUB-FRAME
frame_rb_tl.grid(row = 0, column = 0, padx=15, pady=15,sticky="nsew")
frame_rb_tr.grid(row = 0, column = 1, padx=15, pady=15, sticky="nsew")
frame_rb_bl.grid(row = 1, column = 0, padx=15, pady=15, sticky="nsew")
frame_rb_br.grid(row = 1, column = 1, padx=15, pady=15, sticky="nsew")

# LABELS ASOCIADOS A LOS FRAME PARA AJUSTAR LAS IMAGENES DE LOS DESARROLLADORES
label_rb_tl = tk.Label(frame_rb_tl, width= 230, height=230,relief="solid", image = photoImagenes[0])
label_rb_tl.pack(expand=True, fill="both", padx=2, pady=2)

label_rb_tr = tk.Label(frame_rb_tr, width= 230, height=230,relief="solid", image = photoImagenes[1])
label_rb_tr.pack(expand=True, fill="both", padx=2, pady=2)

label_rb_bl = tk.Label(frame_rb_bl, width= 230, height=230,relief="solid", image = photoImagenes[2])
label_rb_bl.pack(expand=True, fill="both", padx=2, pady=2)

label_rb_br = tk.Label(frame_rb_br, width= 230, height=230,relief="solid", image = photoImagenes[3])
label_rb_br.pack(expand=True, fill="both", padx=2, pady=2)


class Main:
    """
    Clase que representa el menú principal de la aplicación.
    """
    def __init__(self):
        pass

    def interfazPrincipal(self):
        """
        Genera la interfaz de usuario para el menú principal.
        """
        # DESTRUIR LOS FRAME PRINCIPALES DEL INICIO
        frame_left.destroy()
        frame_right.destroy()

        frame_top = tk.Frame(root, bg = "red", bd = 0, relief="sunken")
        frame_bottom = tk.Frame(root, bg = "blue", bd = 0, relief="sunken")  

        frame_top.pack(side = "top", expand = True, fill = "both", padx = 5, pady = 5)
        frame_bottom.pack(side = "bottom", expand = True, fill = "both", padx = 5, pady = 5)

        # CREACIÓN DE LA BARRA DE MENU
        menuBar = tk.Menu(root)
        root.config(menu=menuBar)
        root.title("Sistema Inteligente de Administración y Seguimiento de la Terminal")

        menuArchivo = tk.Menu(menuBar, tearoff=False,bg="white")
        menuBar.add_cascade(menu=menuArchivo, label="Archivo")
        menuArchivo.add_command(label="Aplicacion")
        menuArchivo.add_command(label="Salir")

        menuConsultas = tk.Menu(menuBar, tearoff=False,bg="white")
        menuBar.add_cascade(menu=menuConsultas, label="Funcionalidades")
        menuConsultas.add_command(label="Venta de Viajes")
        menuConsultas.add_command(label="Facturacion y Finanzas")
        menuConsultas.add_command(label="Conductores y Vehiculos")
        menuConsultas.add_command(label="Talleres y Mecanicos")
        menuConsultas.add_command(label="Programación de Viajes")

        menuAyuda = tk.Menu(menuBar, tearoff=False,bg= "white")
        menuBar.add_cascade(menu=menuAyuda, label="Ayuda")
        menuAyuda.add_command(label="Acerca de:")

root.mainloop()