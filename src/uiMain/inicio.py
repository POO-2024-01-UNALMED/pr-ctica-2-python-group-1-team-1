import os
import sys
import tkinter as tk
import principal as main

# SOLUCIÓN IMPORTACIONES --------------------------------------------------------------
import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))
#--------------------------------------------------------------------------------------"""

"""current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '..'))"""

#print(os.path.join(os.path.abspath("src"), ".."))


from src.gestorAplicacion.tiempo.tiempo import Tiempo
from src.gestorAplicacion.administrativo.terminal import Terminal

from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador


# PALETA DE COLORES
colors = main.colors

# FUNCIÓN PARA MOSTRAR LA DESCRIPCION DEL PROYECTO
def mostrarDescripcion():
    label_frame_top.config(text= "Terminal Creations es una plataforma integral de administración y seguimineto,\n que optimiza las operaciones de terminales. Permite administrar transportadoras, \nprogramar viajes, controlar tarifas y gestionar facturación desde un sistema \ncentralizado. Con monitoreo en tiempo real y generación de informes personalizados, \nfacilita la toma de decisiones y mejora la eficiencia operativa, maximizando la productividad \ny controlando todas las operaciones en un solo lugar.", font = "Century", )

# FUNCIÓN PARA SALIR DE LA APLICACIÓN Y APAGAR EL TIEMPO
if __name__ == "__main__":
    Serializador.crearObjetos()
    #Deserializador.deserializarListas()

tiempo = Tiempo.tiempos[0] # 

def salir():
    global tiempo
    if tiempo:
        tiempo.detener()
    Serializador.serializarListas()
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
root.configure(bd = 2, bg= colors["background"])
root.config(menu= menu_bar)

menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label = "Inicio", menu = menu_opciones)
menu_opciones.add_command(label= "Descripcion", background = colors["text"] ,command= mostrarDescripcion)
menu_opciones.add_separator()
menu_opciones.add_command(label= "Salir", background = colors["text"], command=salir)

# IMAGENES
# VARIABLES PARA CAMBIAR LAS DESCRIPCIONES DE LAS HOJAS DE VIDA E IMAGENES.
valores = ["Hoja Vida 1 = Santiago", "Hoja Vida 2 = Jaime", "Hoja Vida 3 = Juan Camilo", "Hoja Vida 4 = Jhonatan", "Hoja Vida 5 = Johan"]
imagenes = ["src/imagenes/developers/foto1.png", "src/imagenes/developers/foto2.png", "src/imagenes/developers/foto3.png", "src/imagenes/developers/foto4.png", "src/imagenes/developers/foto1.png"]
photoImagenes = [tk.PhotoImage(file = imagen) for imagen in imagenes] # GUARDAR LAS IMAGENES COMO OBJETOS DE PhotoImage

indice_valor = 0 # Todo se indexa desde 0
indice_mouse = 0

def cambiarDescripcionImagen():
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
frame_left = tk.Frame(root, bd = 2, relief="sunken")
frame_right = tk.Frame(root, bd = 2, relief="sunken")

#EMPAQUETAR LOS FRAME PRINCIPALES P1,P2 EN LA VENTANA
frame_left.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = "e")
frame_right.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = "w")

# CREACIÓN DE P3 y P4
frame_left_top = tk.Frame(frame_left, bg = colors["background"], bd = 7)
frame_left_bottom = tk.Frame(frame_left, bg = colors["background"], bd = 1)

# DEBO DAR LA UBICACIÓN DEL FRAME P3 y P4
frame_left_top.place(relx=0, rely=0, relwidth=1, relheight=0.2)
frame_left_bottom.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
#frame_left_bottom.bind("<Enter>", lambda event: cambiarImagen()) # PERMITE CAMBIAR LA IMAGEN CUANDO EL MOUSE ENTRA Y SALE DEL FRAME

# CREACIÓN DE P5 Y P6
frame_right_top = tk.Frame(frame_right, bg = colors["background"],bd = 2)
frame_right_bottom = tk.Frame(frame_right, bg = colors["background"], bd = 5)

# UBICACIÓN
frame_right_top.place(relx=0, rely=0, relwidth=1, relheight=0.3)
frame_right_bottom.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

# PARA DESCRIPCION, en los frame se pueden meter etiquetas ls cuales tienen texto. 
label_frame_top = tk.Label(frame_left_top, bd = 5, bg= colors["accent"], relief="groove", text="Bienvenido a Terminal Creations, sistema inteligente \n donde podras llevar el control de tu terminal a un solo clic...\nEn esta ventana puedes ver la informacion de los desarrolladores e \n ingresar al sistema dando click en la imagen inferior.", fg = colors["text"], font= ("Century", 15))
label_frame_top.pack(expand=True, fill="both", padx=2, pady=2)

# BOTON PARA CAMBIAR LAS HOJAS DE VIDA
boton_right_top = tk.Button(frame_right_top,bd = 15, bg= colors["amarillo"], text = "Hojas de Vida de los Desarrolladores", fg = "black" ,font= ("Century", 24),activebackground = colors["azul"], command=cambiarDescripcionImagen)
boton_right_top.pack(expand=True, fill="both", padx=20, pady=20)

# BOTONES ASOCIADO AL INGRESO AL SISTEMA
boton_left_bottom = tk.Button(frame_left_bottom, bg = "black", text = "Administrar Terminal", fg = "lightblue" ,font = ("Century", 15), relief = "groove")
#boton_left_bottom.pack(side = "bottom", pady = 5)
boton_left_bottom.bind("<Button-1>", lambda e : main.interfazPrincipal(root)) # PASA A GENERAR LA NUEVA VENTANA DEL SISTEMA

# BOTONES ASOCIADO AL INGRESO AL CAMBIO DE IMAGEN
boton_left_top = tk.Button(frame_left_bottom, image = photoInicio[0], bd = 5, bg= colors["amarillo"], relief="ridge",command = lambda: main.interfazPrincipal(root))
boton_left_top.pack(side = "top", pady = 20, padx = 20)
boton_left_top.bind("<Leave>", lambda event: cambiarImagen())

# EL FRAME INFERIOR DERECHO (P6), DIVIDIRLO EN 4, 2FIL, 2COL
frame_right_bottom.grid_rowconfigure(0, weight=1)
frame_right_bottom.grid_rowconfigure(1, weight=1)
frame_right_bottom.grid_columnconfigure(0, weight=1)
frame_right_bottom.grid_columnconfigure(1, weight=1)

# CREAR LOS SUB-FRAME DE P6
frame_rb_tl = tk.Frame(frame_right_bottom, bd = 5, bg= colors["azul"], relief="ridge")
frame_rb_tr = tk.Frame(frame_right_bottom, bd = 5, bg= colors["azul"], relief="ridge")
frame_rb_bl = tk.Frame(frame_right_bottom, bd = 5, bg= colors["azul"], relief="ridge")
frame_rb_br = tk.Frame(frame_right_bottom, bd = 5, bg= colors["azul"], relief="ridge")

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

root.protocol("WM_DELETE_WINDOW", salir)

root.mainloop()