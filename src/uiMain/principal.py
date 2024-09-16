import tkinter as tk
from tkinter import messagebox
from FieldFrame import FieldFrame
from TablasFieldFrame import TablaFrame, TablaFrameDinamica, ResultadosOperacion

import sys
import os
sys.path.append(os.path.join(os.path.abspath("src"), ".."))

from src.gestorAplicacion.constantes.destino import Destino
from src.gestorAplicacion.constantes.tipoPasajero import TipoPasajero
from src.gestorAplicacion.constantes.tipoVehiculo import TipoVehiculo
from src.gestorAplicacion.administrativo.terminal import Terminal
from src.gestorAplicacion.tiempo.tiempo import Tiempo
from src.gestorAplicacion.administrativo.viaje import Viaje

def alertWarn(title, message):
    messagebox.showwarning(title, message)

def on_submit(formData):
    print("Form submitted with data:")
    for key, value in formData.items():
        print(f"{key}: {value}")

# CONSULTAR LAS LISTAS 
def listViajes():
    return Terminal.getViajes()

def listViajesCurso():
    return Terminal.getViajesEnCurso()

def listViajesHistorial():
    return Terminal.getHistorial()

def listReservas():
    return Terminal.getReservas()

# REMOVER ELEMEMNTOS DE ESTAS LISTAS

# Método para eliminar un viaje de la lista de viajes de la Terminal
def removeViaje(viaje):
    viajes = Terminal.getViajes()  # Obtener la lista de viajes
    if viaje in viajes:  # Verificar que el viaje esté en la lista
        viajes.remove(viaje)  # Eliminar el viaje
        Terminal.setViajes(viajes)  # Actualizar la lista en Terminal

# Método para eliminar un viaje en curso de la lista de viajes en curso de la Terminal
def removeViajeCurso(viaje):
    viajesCurso = Terminal.getViajesEnCurso()  # Obtener la lista de viajes en curso
    if viaje in viajesCurso:  # Verificar que el viaje esté en la lista
        viajesCurso.remove(viaje)  # Eliminar el viaje
        Terminal.setViajesEnCurso(viajesCurso)  # Actualizar la lista en Terminal

# Método para eliminar un viaje del historial de la Terminal
def removeViajeHistorial(viaje):
    historial = Terminal.getHistorial()  # Obtener el historial de viajes
    if viaje in historial:  # Verificar que el viaje esté en el historial
        historial.remove(viaje)  # Eliminar el viaje
        Terminal.setHistorial(historial)  # Actualizar el historial en Terminal

# Método para eliminar una reserva de la lista de reservas de la Terminal
def removeReserva(reserva):
    reservas = Terminal.getReservas()  # Obtener la lista de reservas
    if reserva in reservas:  # Verificar que la reserva esté en la lista
        reservas.remove(reserva)  # Eliminar la reserva
        Terminal.setReservas(reservas)  # Actualizar la lista en Terminal


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

tipoPasajero = None
tipoVehiculo = None
viajesDisponibles= []
viajeSeleccionado = None
cantidad = 0

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
    menuConsultas.add_command(label="Venta de Viajes", command= lambda: funcionalidad1())
    menuConsultas.add_command(label="Gestión de Conductores", command= lambda: funcionalidad2())
    menuConsultas.add_command(label="Facturacion y Finanzas", command= lambda: funcionalidad3())
    menuConsultas.add_command(label="Talleres y Mecanicos", command= lambda: funcionalidad4())
    menuConsultas.add_command(label="Programación de Viajes", command= lambda: funcionalidad5())

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
    label_top_center = tk.Label(frame_top, text="Hola Admin de Terminal Creations", font=("Segoe Script", 35, "bold"), fg=colors["amarillo"], bd=3, bg=colors["background"])
    label_top_left = tk.Label(frame_top, text="Descripción", font=("Segoe Script", 10, "bold"), fg=colors["text"], bd=3, bg=colors["background"])
    label_top_right = tk.Label(frame_top, text="TC", bd=3, font=("Segoe Script", 60, "bold"), fg=colors["text"], bg=colors["background"])

    # Posicionando los labels superiores con .place()
    label_top_right.place(relx=0.0, rely=0.5, relwidth=0.1, anchor='w')  # Ocupa 10% del ancho
    label_top_center.place(relx=0.1, rely=0.5, relwidth=0.7, anchor='w')  # Ocupa 70% del ancho
    label_top_left.place(relx=0.8, rely=0.5, relwidth=0.2, anchor='w')  # Ocupa 20% del ancho

    # DIVISIÓN FRAME INFERIOR EN DOS
    frame_bottom_left = tk.Frame(frame_bottom, bd=3, bg=colors["background"])
    frame_bottom_right = tk.Frame(frame_bottom, bd=3, bg=colors["background"])

    # UBICACIÓN DE LOS FRAME INFERIORES CON .place()
    frame_bottom_left.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.98)  # Izquierda
    frame_bottom_right.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.98)  # Derecha

    # AGREGAR LOS LABELS A CADA FRAME INFERIOR
    label_bottom_left_tp = tk.Label(frame_bottom_left, text="¿Cómo usar nuestro sistema?", font=("Small fonts", 20), fg=colors["text"], bd=3, bg=colors["naranja"])
    label_bottom_left_bt = tk.Label(frame_bottom_left, text="En nuestro sistema inteligente de podras administrar tu  terminal de\ntransportes dentro de las operaciones se encuentran la venta de viajes,\nfacturación y finanzas, gestión de conductores, talleres y vehiculos\npara la reparación de los mismos y programación y seguimientos de\nviajes. Tambien podrás consultar acerca de los desarrolladores en la\npestaña (Ayuda) del menu superior.", font=("Century", 13), fg=colors["text"], bd=3, bg=colors["background"])
    label_bottom_left_extra = tk.Label(frame_bottom_left, text="ESPACIO IMG", font=("Century", 11), fg=colors["text"], bd=3, bg=colors["background"], relief="solid")

    label_bottom_right_tp = tk.Label(frame_bottom_right, text="¿Qué puede hacer?", font=("Small fonts", 20), fg=colors["text"], bd=3, bg=colors["naranja"])
    label_bottom_right_bt = tk.Label(frame_bottom_right, text="Para utilizar tus diferentes funcionalidades de administración debes\nir a la barra superior de menús, en la pestaña (Procesos y consultas)\nse desplegarán todas la operaciones que puedes realizar al seleccionar\nalguna de estas opciones se mostrará la interfaz respectiva, donde se\ndara una breve descripción y los diferentes formularios necesarios\npara la ejecución de la misma.\n\nRecuerda que en la pestaña (Archivo) tienes las opciones de (Aplicación)\nla cual te dara información acerca del sistema, y (Salir) te regresará al\na la ventana de Inicio.", font=("Century", 13), fg=colors["text"], bd=3, bg=colors["background"])
    label_bottom_right_extra = tk.Label(frame_bottom_right, text="ESPACIO IMG", font=("Century", 11), fg=colors["text"], bd=3, bg=colors["background"], relief="solid")

    # UBICAR LOS LABELS INFERIORES EN CADA FRAME CON .place()
    label_bottom_left_tp.place(relx=0.5, rely=0.05, anchor="n")
    label_bottom_left_bt.place(relx=0.5, rely=0.2, anchor="n")
    label_bottom_left_extra.place(relx=0.5, rely=0.65, relwidth=0.9, relheight=0.3, anchor="n")

    label_bottom_right_tp.place(relx=0.5, rely=0.05, anchor="n")
    label_bottom_right_bt.place(relx=0.5, rely=0.2, anchor="n")
    label_bottom_right_extra.place(relx=0.5, rely=0.65, relwidth=0.9, relheight=0.3, anchor="n")

    ventanaPrincipal.protocol("WM_DELETE_WINDOW", lambda: salir(ventanaPrincipal, ventanaInicio))

    # FUNCIONALIDADES
    def funcionalidad1():
        from src.gestorAplicacion.administrativo.transportadora import Transportadora
        #VARIABLES PARA LA FUNCIONALIDAD
        #print(len(Terminal.getPasajeros()))
        #for viaje in Terminal.getViajes():
         #   print(len(viaje.getPasajeros()))

        lista = estructura_frames("Venta Viajes", "sasaasdada")
        frame_bottom = lista[0]
        label_top_center = lista[1]
        label_center_center = lista[2]

        label_top_center.configure(text="Venta de Viajes")

        def elegirDestino(): # 1
            def devolucionLlamado(formularioDatos):
                global destinoDeseado
                global viajesDisponibles

                # Suponiendo que 'formularioDatos' es un diccionario y contiene un único destino
                destino_nombre = list(formularioDatos.values())[0]
                
                destinoDeseado = Destino[destino_nombre]  # Convertir el nombre del destino a un Enum
                print(destinoDeseado)
                print(type(destinoDeseado))

                viajesDisponibles = Terminal.viajesDestino(destinoDeseado)
                for viaje in viajesDisponibles:
                    print(viaje.getVehiculo().getTipo().name)

                if len(viajesDisponibles) == 0:
                    messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponibles para este destino")
                    elegirDestino()
                  
                else:
                    print(f"viajesDisponibles{viajesDisponibles}")
                    elegirTipoPasajero()
                
                # Llamar al siguiente método
                
            criterios = ["Destinos"]
            destinos= [destino.name for destino in Destino]
            habilitado = [False, False, False]


            # Create the FieldFrame widget
            field_frame = FieldFrame(
                parent=frame_bottom,
                tituloCriterios="Opciones",
                criterios=criterios,
                tituloValores="Selección",
                valores=destinos,
                habilitado=habilitado,
                devolucionLlamado= devolucionLlamado
                )


            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)
        
        def elegirTipoPasajero(): #2

            def devolucionLlamado(formularioDatos):
                global tipoPasajero
                global viajesDisponibles
                tipoPasajero = list(formularioDatos.values())[0]
                tipoPasajero = TipoPasajero[tipoPasajero]

                if tipoPasajero == TipoPasajero.ESTUDIANTE:
                    viajesDisponibles = Terminal.viajesParaEstudiantes(viajesDisponibles)
                    if len(viajesDisponibles) != 0:
                        elegirTipoVehiculoEstudiante()

                                
                    elif len(viajesDisponibles)==0:

                        messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponibles para este tipo de pasajero")
                        elegirTipoPasajero()


                else:
                    separarPasajeros1()

            criterios = ["Tipos pasajero"]
            tiposPasajeros= [tipoPasajero.name for tipoPasajero in TipoPasajero]
            habilitado = [False, False, False]

                        # Create the FieldFrame widget
            field_frame = FieldFrame(
                parent=frame_bottom,
                tituloCriterios="Opciones",
                criterios=criterios,
                tituloValores="Selección",
                valores=tiposPasajeros,
                habilitado=habilitado,
                devolucionLlamado= devolucionLlamado
                )


            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

        def elegirTipoVehiculoEstudiante():#3.1
            def devolucionLlamado(formularioDatos):
                global viajesDisponibles
                global tipoVehiculo
                tipoVehiculo = formularioDatos
                print(tipoVehiculo)
                tipo = list(formularioDatos.values())[0]
                tipoVehiculo = TipoVehiculo[tipo]
                print(viajesDisponibles)
                viajesDisponibles2 = Terminal.viajesParaEstudiantes(viajesDisponibles,tipo)
                print(viajesDisponibles2)

                if len(viajesDisponibles2) == 0:
                    def mostrar():
                        for viaje in viajesDisponibles:
                            lista = []
                            if not viaje.getVehiculo().getTipo().name in lista:
                                lista.append(viaje.getVehiculo().getTipo().name)
                        return lista
                    messagebox.showinfo("Sin viajes disponibles", f"No hay viajes disponibles para este tipo de vehiculo {mostrar()}")
                    elegirTipoVehiculoEstudiante()
                else:
                    viajesDisponibles = viajesDisponibles2
                    elegirTranportadora()
                    print("si hay")

            criterios = ["Tipo vehiculo"]
            lista = []

            #Mostrar solo los que se pueden
            for viaje in viajesDisponibles:
                if not viaje.getVehiculo().getTipo().name in lista:
                    lista.append(viaje.getVehiculo().getTipo().name)

            tiposVehiculos= lista
            habilitado = [False, False, False]

            # Create the FieldFrame widget
            field_frame = FieldFrame(
                parent=frame_bottom,
                tituloCriterios="Opciones",
                criterios=criterios,
                tituloValores="Selección",
                valores=tiposVehiculos,
                habilitado=habilitado,
                devolucionLlamado= devolucionLlamado
                )


            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)
        
        def elegirModalidad():
            def devolucionLlamado(formularioDatos):
                global viajesDisponibles
                tipoPasajero = list(formularioDatos.values())[0]
                tipoPasajero = TipoPasajero[tipoPasajero]


            criterios = ["Modalidad"]
            tiposPasajeros= ["Mayor velocidad",
                             "Salida con mayor antelación",
                             "Más económico",
                             "Transportadora"]
            habilitado = [False, False, False]

            # Create the FieldFrame widget
            field_frame = FieldFrame(
                parent=frame_bottom,
                tituloCriterios="Opciones",
                criterios=criterios,
                tituloValores="Selección",
                valores=tiposPasajeros,
                habilitado=habilitado,
                devolucionLlamado= devolucionLlamado
                )


            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)
        
        def elegirTranportadora():#estudiante 4.0 

            """Elegir el primer viaje que encuentre de la transportadora"""
                    
            def devolucionLlamado(formularioDatos):
                global viajeSeleccionado
                global tipoPasajero
                global viajesDisponibles
                print(type(formularioDatos))
                indice = int(formularioDatos.split(" ")[-1])
                print(type(indice))
                transportadora = transportadoras[indice-1]
                print(transportadora.getNombre())
                
                #for viaje in transportadora.getViajesAsignados():
                for viaje in viajesDisponibles:
                    if viaje.getVehiculo().getTransportadora() == transportadora:
                        viajeSeleccionado = viaje
                        break

                print(viajeSeleccionado.getVehiculo().getTipo().name)
                    
            global transportadoras
            transportadoras =Terminal.transportadorasViaje(viajesDisponibles)

            frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
            frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

            # Create the FieldFrame widget
            field_frame = TablaFrame(["Opcion","Transportadora"],
                                     ["Nombre"],
                                     frame_bottom,
                                     transportadoras, 
                                     [False],
                                     devolucionLlamado=devolucionLlamado)

            # UBICACIÓN DEL FIELD FRAME

            # Si es necesario, asegúrate de configurar las filas y columnas para que se expandan
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)
                        

        def elegirCantidad():
            def devolucionLlamado(formularioDatos):
                global cantidad
                if isinstance(formularioDatos, dict):
            # Convierte los valores del diccionario en una lista
                    lista = list(formularioDatos.values())
                    print(f"Lista de valores: {lista}")
                    
                    if len(lista) > 2:
                        cantidad = lista[2]
                        if cantidad>15:
                                messagebox.showinfo("Sin viajes disponibles", "No se vende una cantidad superior a 15")
                        print(cantidad)
                        elegirModalidad()
                    else:
                        print("La lista no contiene suficientes elementos.")
                else:
                    print("formularioDatos no es un diccionario.")
                
            criterios = ["Destino", "Tipo pasajero", "cantidad"]
            habilitado = [False, False, True]

            field_frame = FieldFrame(
            parent=frame_bottom,
            tituloCriterios="Criterio",
            criterios=criterios,
            tituloValores="Valor",
            valores=[destinoDeseado.name, tipoPasajero.name],
            habilitado=habilitado,
            devolucionLlamado=devolucionLlamado  # Aquí se usa 'devolucionLlamado'
            )

            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)
        
        def verificarCantidad():
            global cantidad
            global viajesDisponibles
            global tipoPasajero

            if tipoPasajero == TipoPasajero.VIP:
                viajesDisponibles = Terminal.viajesParaVips(cantidad, viajesDisponibles)
                if len(viajesDisponibles) == 0:
                    messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponbles para esa cantidad de puestos")
                    elegirTipoPasajero()
                else:
                    elegirModalidad()
            
                if tipoPasajero == TipoPasajero.DISCAPACITADO or tipoPasajero == TipoPasajero.REGULAR:
                    viajesDisponibles = Terminal.viajesParaRegularesYDiscapacitados(cantidad, viajesDisponibles)
                    if len(viajesDisponibles) == 0:
                        messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponbles para esa cantidad de puestos")
                        elegirTipoPasajero()
                    else:
                        elegirModalidad()
        
        def separarPasajeros1():
            global viajesDisponibles
            global cantidad

            print("Tipo de Pasajero:", tipoPasajero)

            if tipoPasajero == TipoPasajero.VIP:
                viajesDisponibles = Terminal.viajesParaVips(cantidad, viajesDisponibles)
                if len(viajesDisponibles)==0:
                    messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponibles para este tipo de pasajero")
                    elegirTipoPasajero()
                else:
                    elegirCantidad()
            
            else:
                viajesDisponibles = Terminal.viajesParaRegularesYDiscapacitados(cantidad, viajesDisponibles)
                if len(viajesDisponibles)==0:
                    messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponibles para este tipo de pasajero")
                    elegirTipoPasajero()
                
                else:
                    elegirCantidad()

        elegirDestino()

    def funcionalidad2():
        from src.gestorAplicacion.administrativo.transportadora import Transportadora

        lista = estructura_frames("Gestion de conductores","Elija la transportadora a la cual le administrara los conductores")
        new_frame_bottom = lista[0]
        label_top_center = lista[1]
        label_center_center = lista[2]
        """frame_top.destroy()
        frame_bottom.destroy()

        new_frame_top = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
        new_frame_center = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
        new_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])

        new_frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        new_frame_center.place(relx=0, rely=0.15, relwidth=1, relheight=0.1)
        new_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

        label_top_center = tk.Label(new_frame_top, text="Gestion de conductores", font=("Segoe Script", 35, "bold"), fg=colors["amarillo"], bd=3, bg=colors["background"], relief="ridge")
        label_center_center = tk.Label(new_frame_center, text="Elija la transportadora a la cual le administrara los conductores", font=("Arial", 10, "bold"), fg=colors["text"], bd=3, bg=colors["background"])

        label_top_center.place(relx=0.5,rely=0.5, anchor="center")
        label_center_center.place(relx=0.5,rely=0.5, anchor="center")"""

        #print(Transportadora.getTransportadoras()[0].getNombre())

        def devolucion_transportadora(valor):
            true_value = int(valor.split(" ")[2])

            transportadora = Transportadora.getTransportadoras()[true_value-1]

            new_frame_bottom.destroy()

            label_center_center.config(text="Seleccione una opcion")
            new2_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
            new2_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

            criterios = ["Opciones de conductor"]
            valores_iniciales = ["Despedir conductor","Contratar conductor","Modificar conductor"]
            habilitado = [False, False, False]

            datos = {}

            def devolucion_llamado(formularioDatos):

                datos = formularioDatos
                print(formularioDatos)

                new2_frame_bottom.destroy()

                new3_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                new3_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                print(datos)

                def devolucion_contratar(valor):
                    true_value = int(valor.split(" ")[2])
                    
                    driver = transportadora.getConductoresRegistrados()[true_value-1]
                    label_center_center.config(text=transportadora.contratarConductor(driver))

                    #Mostrar que se contrato a un conductor



                def devolucion_despedir(valor):
                    true_value = int(valor.split(" ")[2])

                    driver = transportadora.getConductores()[true_value-1]
                    label_center_center.config(text=transportadora.despedirConductor(driver))

                    #Mostar que se despidio a un conductor


                def devolucion_modificar(valor):
                    true_value = int(valor.split(" ")[2])

                    conductor = transportadora.getConductores()[true_value-1]

                    new3_frame_bottom.destroy()

                    label_center_center.config(text="Seleccione que desea modificarle al conductor")

                    new4_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                    new4_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                    criterios = ["Modificaciones"]
                    valores_iniciales = ["Viaje","Vehiculo","Modificar conductor"]
                    habilitado = [False, False, False]

                    def devolucion_viaje(valor):
                        
                        new4_frame_bottom.destroy()

                        new5_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                        new5_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)    

                        if valor["Modificaciones"] == "Viaje":

                            if (len(conductor.getHorario()) == 0 ):
                                
                                criterios = ["Modificar viaje"]
                                valores_iniciales = ["Asignar viaje"]
                                habilitado = [False]

                                def devolucion_asignar_viaje(valor):
                                    
                                    new5_frame_bottom.destroy()

                                    new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                    new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)    

                                    viajes_disponibles_tabla = TablaFrame(["Opcion","Destino","Fecha","Hora llegada"], ["Llegada","Fecha","Hora"], new6_frame_bottom, transportadora.getViajesAsignados(), [False,False,False], devolucionLlamado=devolucion_modificar)
                                    viajes_disponibles_tabla.place(relx=0.5,rely=0.5,anchor="center")

                                
                                viajes_disponibles = FieldFrame(
                                parent=new5_frame_bottom,
                                tituloCriterios="Opciones",
                                criterios=criterios,
                                tituloValores="Seleccion",
                                valores=valores_iniciales,
                                habilitado=habilitado,
                                devolucionLlamado=devolucion_asignar_viaje
                                )                         

                                viajes_disponibles.place(relx=0.5,rely=0.5, anchor="center")   
                            else:
                                
                                criterios = ["Modificar viaje"]
                                valores_iniciales = ["Asignar viaje","Desvincular viaje"]
                                habilitado = [False,False]

                                

                                def devolucion_viaje_viaje(valor):
                                    from gestorAplicacion.tiempo.tiempo import Tiempo
                                    
                                    if valor["Modificar viaje"] == "Asignar viaje":
                                        new5_frame_bottom.destroy()

                                        new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                        new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                        #if transportadora.obtenerViajesDisponibles(Tiempo.Dia.getValue(), conductor.getTipoVehiculo(), conductor):

                                        def prueba(valor):
                                            pass
        

                                        viajes_disponibles_tabla_2 = TablaFrameDinamica(["Opcion","Destino","Fecha","Hora llegada"], ["Llegada","Fecha","Hora"], new6_frame_bottom, transportadora.mostrarViajesDisponibles(Tiempo.tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor), [False,False,False], devolucionLlamado=prueba )
                                        viajes_disponibles_tabla_2.place(relx=0.5,rely=0.5,anchor="center")

                                    if valor["Modificar viaje"] == "Desvincular viaje":
                                        new5_frame_bottom.destroy()

                                        new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                        new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                        def prueba(valor):
                                            pass                                        
        

                                        viajes_disponibles_tabla_2 = TablaFrameDinamica(["Opcion","Destino","Fecha","Hora llegada"], ["Llegada","Fecha","Hora"], new6_frame_bottom, conductor.getHorario(), [False,False,False], devolucionLlamado=prueba)
                                        viajes_disponibles_tabla_2.place(relx=0.5,rely=0.5,anchor="center")                                                                              


                                
                                viajes_disponibles = FieldFrame(
                                parent=new5_frame_bottom,
                                tituloCriterios="Opciones",
                                criterios=criterios,
                                tituloValores="Seleccion",
                                valores=valores_iniciales,
                                habilitado=habilitado,
                                devolucionLlamado=devolucion_viaje_viaje
                                ) 

                                viajes_disponibles.place(relx=0.5,rely=0.5, anchor="center")

                        if valor["Modificaciones"] == "Vehiculo":

                            if conductor.getVehiculo() != None:
                                    
                                criterios = ["Modificaciones"]
                                valores_iniciales = ["Desvincular vehiculo"]
                                habilitado = [False]

                                def devolucion_desvincular_vehiculo(valor):

                                    new5_frame_bottom.destroy()

                                    label_center_center.config(text="Seleccione el vehiculo que desea desvincular del conductor")

                                    new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                    new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                    def devolucion_desvincular_verificacion(valor):

                                        if conductor.getHorario() == 0:
                                            if len(conductor.getVehiculo().getConductores()) >= 2:
                                                pass
                                                #Desvincular vehiculo del conductor
                                            else:
                                                pass
                                            #No se puede porque no hay mas conductores asociados al vehiculo
                                        else:
                                            pass
                                            #No se puede porque el conductor tiene viajes programados

                                    tabla_vehiculo_asociado = TablaFrame(["Opcion","Placa","Modelo"], ["Placa","Modelo"], new6_frame_bottom, [conductor.getVehiculo()], [False,False], devolucionLlamado=devolucion_desvincular_verificacion)
                                    tabla_vehiculo_asociado.place(relx=0.5,rely=0.5,anchor="center")

                                    


                                opciones_de_modificar = FieldFrame(
                                parent=new5_frame_bottom,
                                tituloCriterios="Opciones",
                                criterios=criterios,
                                tituloValores="Seleccion",
                                valores=valores_iniciales,
                                habilitado=habilitado,
                                devolucionLlamado=devolucion_desvincular_vehiculo
                                )
                                    
                                opciones_de_modificar.place(relx=0.5,rely=0.5, anchor="center")

                            else:
                                criterios = ["Modificaciones"]
                                valores_iniciales = ["Vincular vehiculo"]
                                habilitado = [False]

                                def devolucion_vincular_vehiculo(valor):
                                    new5_frame_bottom.destroy()

                                    new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                    new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                    def  devolucion_vincular_vehiculo_verificacion(valor):
                                        true_value = int(valor.split(" ")[2])

                                        conductor.tomarVehiculo(transportadora.mostrarVehiculosDisponibles()[true_value-1])

                                        #Mostrar que se vinculo el vehiculo exitosamente al conductor

                                    if (len(transportadora.mostrarVehiculosDisponibles()) == 0):
                                        label_center_center.config(text="No hay vehiculos disponibles")
                                        #Por si no hay vehiculos disponibles para mostrar


                                    tabla_vehiculo_asociado = TablaFrame(["Opcion","Placa","Modelo"], ["Placa","Modelo"], new6_frame_bottom, transportadora.mostrarVehiculosDisponibles(), [False,False], devolucionLlamado=devolucion_vincular_vehiculo_verificacion)
                                    tabla_vehiculo_asociado.place(relx=0.5,rely=0.5,anchor="center")


                                opciones_de_modificar = FieldFrame(
                                parent=new5_frame_bottom,
                                tituloCriterios="Opciones",
                                criterios=criterios,
                                tituloValores="Seleccion",
                                valores=valores_iniciales,
                                habilitado=habilitado,
                                devolucionLlamado=devolucion_vincular_vehiculo
                                )

                                opciones_de_modificar.place(relx=0.5,rely=0.5, anchor="center")
                                


                    opciones_de_modificar = FieldFrame(
                        parent=new4_frame_bottom,
                        tituloCriterios="Opciones",
                        criterios=criterios,
                        tituloValores="Seleccion",
                        valores=valores_iniciales,
                        habilitado=habilitado,
                        devolucionLlamado=devolucion_viaje
                    )

                    opciones_de_modificar.place(relx=0.5,rely=0.5, anchor="center")
                    




                if datos["Opciones de conductor"] == "Despedir conductor":
                    label_center_center.config(text="Seleccione el conductor que desea despedir")

                    fire_tabla = TablaFrameDinamica(["Opcion","Nombre","Experiencia  "], ["getNombre","getExperiencia"], new3_frame_bottom, transportadora.getConductores(), [False,False], devolucionLlamado=devolucion_despedir)
                    fire_tabla.place(relx=0.5,rely=0.5,anchor="center")

                if datos["Opciones de conductor"] == "Contratar conductor":
                    label_center_center.config(text="Seleccione el conductor que desea contratar")

                    hire_tabla = TablaFrame(["Opcion","Nombre","Experiencia","Licencia"], ["Nombre","Experiencia","Licencia"], new3_frame_bottom, transportadora.getConductoresRegistrados(), [False,False,False], devolucionLlamado=devolucion_contratar)
                    hire_tabla.place(relx=0.5,rely=0.5,anchor="center")

                if datos["Opciones de conductor"] == "Modificar conductor":
                    label_center_center.config(text="Seleccione el conductor que desea modificar")
                    
                    modify_tabla = TablaFrameDinamica(["Opcion","Nombre","Experiencia  "], ["getNombre","getExperiencia"], new3_frame_bottom, transportadora.getConductores(), [False,False], devolucionLlamado=devolucion_modificar)
                    modify_tabla.place(relx=0.5,rely=0.5,anchor="center")

                





            tabla_second_window = FieldFrame(
                parent=new2_frame_bottom,
                tituloCriterios="Opciones",
                criterios=criterios,
                tituloValores="Seleccion",
                valores=valores_iniciales,
                habilitado=habilitado,
                devolucionLlamado=devolucion_llamado
            )

            tabla_second_window.place(relx=0.5,rely=0.5, anchor="center")

            


        tabla_frame = TablaFrame(["Opcion","Transportadora"], ["Nombre"], new_frame_bottom, Transportadora.getTransportadoras(), [False], devolucionLlamado=devolucion_transportadora)
        tabla_frame.place(relx=0.5, rely=0.5, anchor="center")
        



    

      
    


            

       
            

    def funcionalidad3():
        label_top_center.configure(text="Facturacion y Finanzas")
            

    def funcionalidad4():
        label_top_center.configure(text="Talleres y Mecanicos")
            

    def funcionalidad5():
        lista = estructura_frames("Gestion de conductores","Elija la transportadora a la cual le administrara los conductores")
        frame_bottom = lista[0]
        label_top_center = lista[1]
        label_center_center = lista[2]

        label_top_center.configure(text="Programación de Viajes")
        label_center_center.config(text = "Funcionalidad 5")

        def devolucionLlamado(formularioDatos):
            if (formularioDatos[criterios[0]] == "Programación de Viajes"):
                programacionViaje()
            elif (formularioDatos[criterios[0]] == "Administración de Reservas"):    
                administraciondeReservas()
            elif (formularioDatos[criterios[0]] ==  "Aministracion de Viajes"):
                administracionViaje()
            elif (formularioDatos[criterios[0]]== "Administración de Historial"):
                administracionHistorial()
            
        criterios = ["Tipos de acciones de Programación"]
        valores_iniciales = ["Programación de Viajes", "Administración de Reservas", "Aministracion de Viajes", "Administración de Historial"]
        habilitado = [False, False, False]


            # Create the FieldFrame widget
        field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

            # UBICACIÓN DEL FIELD FRAME
        field_frame.grid(row=0, column=0, sticky="nsew")
        frame_bottom.grid_rowconfigure(0, weight=1)
        frame_bottom.grid_columnconfigure(0, weight=1)
            

        def programacionViaje():
            label_top_center.configure(text="Programando un viaje...")

            # LISTA DE DESTINOS DEL ENUMERADO
            valores_iniciales = list(Destino)
            destinos = []
            for i in valores_iniciales:
                destinos.append(i.name)

            criterios = ["Destino"]
            habilitado = [False, False, False]

            def devolucionLlamado(formularioDatos): # TRANSPORTADORAS POR DESTINO
                global destinoSelect
                destinoNombre = formularioDatos[criterios[0]]
                listaTransportadoras = None

                for i in valores_iniciales:
                    if (i.name == destinoNombre):
                        listaTransportadoras = Terminal.transportadorasViajeDisponible(i)
                        destinoSelect = i
                
                # PASAR A LA SEGUNDA VENTANA
                seleccionTransportadora(listaTransportadoras)
                
            def seleccionTransportadora(transportadoras):
                label_top_center.configure(text="Seleccionando Transportadora...")

                # LISTA DE TRANSPORTADORAS POR NOMBRE
                nombresTransportadoras = []
                for i in transportadoras:
                    nombresTransportadoras.append(i.getNombre())
                
                criterios = ["Transportadora"]
                habilitado = [False, False, False]

                def devolucionLlamado(formularioDatosTransportadora):
                    transportadoraNombre = formularioDatosTransportadora[criterios[0]]
                    global transportadoraSelect
                    for i in transportadoras:
                        if (i.getNombre() == transportadoraNombre):
                            transportadoraSelect = i
                    
                    # PASAR A SELECCIONAR LA FECHA  Y HORA
                    seleccionFecha()

                    print(transportadoraNombre)
                
                field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=nombresTransportadoras, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

                # UBICACIÓN DEL FIELD FRAME
                field_frame.grid(row=0, column=0, sticky="nsew")
                frame_bottom.grid_rowconfigure(0, weight=1)
                frame_bottom.grid_columnconfigure(0, weight=1)

                def seleccionFecha():
                    label_top_center.configure(text="Seleccionando Fecha del Viaje...")
                    fechaActual = Tiempo.salidaFecha
                    fechasDisponibles = Terminal.fechasDisponibles(fechaActual)

                    criterios = ["Fechas Disponibles"]

                    def devolucionLlamado(formularioDatosFechas):
                        global fechaSelect
                        fechaSelect = formularioDatosFechas[criterios[0]]
                    
                        print(fechaSelect)

                        # PASAR A SELECCIONAR LA HORA
                        seleccionHora(fechaSelect)
                    
                    field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=fechasDisponibles, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

                    # UBICACIÓN DEL FIELD FRAME
                    field_frame.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                    def seleccionHora(fechaSeleccionada):
                        label_top_center.configure(text="Seleccionando Hora del Viaje...")
                        horasDisponibles = Terminal.horasDisponibles(fechaSeleccionada)
                        criterios = ["Horas Disponibles"]

                        def devolucionLlamado(formularioDatosHoras):
                            global horaSelect
                            horaSelect = formularioDatosHoras[criterios[0]]

                            print(horaSelect)

                            # PASAR A SELECCIONAR EL TIPO DE VEHICULO
                            seleccionTipoVehiculo()
                        
                        field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=horasDisponibles, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

                        # UBICACIÓN DEL FIELD FRAME
                        field_frame.grid(row=0, column=0, sticky="nsew")
                        frame_bottom.grid_rowconfigure(0, weight=1)
                        frame_bottom.grid_columnconfigure(0, weight=1)
                        
                        def seleccionTipoVehiculo():
                            tiposDisponibles = transportadoraSelect.tiposVehiculosDisponible()
                            tiposPorNombre = []
                            for i in tiposDisponibles:
                                tiposPorNombre.append(i.name)
                            criterios = ["Tipo de Vehiculo"]

                            def devolucionLlamado(formularioDatosTipoVehiculo):
                                label_top_center.configure(text="Seleccionando tipo de Vehiculo...")
                                global tipoVehiculoSelect
                                seleccionNombre = formularioDatosTipoVehiculo[criterios[0]]  # Try, si las listas son vacias
                                for i in tiposDisponibles:
                                    if (i.name == seleccionNombre):
                                        tipoVehiculoSelect = i

                                # PASAR A SELECCIONAR EL CONDUCTOR
                                seleccionConductor()

                                print(tiposPorNombre)

                            field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=tiposPorNombre, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

                            # UBICACIÓN DEL FIELD FRAME
                            field_frame.grid(row=0, column=0, sticky="nsew")
                            frame_bottom.grid_rowconfigure(0, weight=1)
                            frame_bottom.grid_columnconfigure(0, weight=1)

                            def seleccionConductor():
                                label_top_center.configure(text="Tipo de selección del conductor...")
                                def devolucionLlamado(formularioDatos):
                                    if (formularioDatos[criterios[0]] == "Selección Manual"):
                                        seleccionManual()
                                    elif (formularioDatos[criterios[0]] == "Selección Semi-Automática"):    
                                        seleccionAutomática()
                                    
                                criterios = ["Modo de Selección"]
                                valores_iniciales = ["Selección Manual", "Selección Semi-Automática"]
                                habilitado = [False, False]


                                    # Create the FieldFrame widget
                                field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                                    # UBICACIÓN DEL FIELD FRAME
                                field_frame.grid(row=0, column=0, sticky="nsew")
                                frame_bottom.grid_rowconfigure(0, weight=1)
                                frame_bottom.grid_columnconfigure(0, weight=1)

                                def seleccionManual():
                                    conductores = transportadoraSelect.conductoresDisponibles(fechaSelect, tipoVehiculoSelect)
                                    conductoresNombre = []

                                    if (conductoresNombre):
                                        for i in conductores:
                                            conductoresNombre.append(i.getNombre())
                                        criterios = ["Conductores Disponibles"]

                                        def devolucionLlamado(formularioDatosConductores):

                                            global conductorSelect
                                            conductorSelect = formularioDatosConductores
                                        
                                        field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=conductoresNombre, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                                        # UBICACIÓN DEL FIELD FRAME
                                        field_frame.grid(row=0, column=0, sticky="nsew")
                                        frame_bottom.grid_rowconfigure(0, weight=1)
                                        frame_bottom.grid_columnconfigure(0, weight=1)

                                    else:
                                        print ("No hay conductores disponibles...") # Buen lugar para las excepciones --- Solucionar errores
                                        seleccionTipoVehiculo()
                                        
                                    print(conductores)

                                def seleccionAutomática():
                                    global viaje
                                    viaje = Terminal.programarViaje(destinoSelect, tipoVehiculoSelect, fechaSelect, horaSelect, Destino.MEDELLIN)

                                    if (isinstance(viaje, Viaje)):
                                        print("Programación exitosa")
                                        # AGREGAR PANTALLA DE RESULTADOS
                                    else:
                                        print("Programación en proceso")
                                        # AGREGAR PANTALLA DE RESULTADOS
            
            field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=destinos, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

        def administraciondeReservas():
            label_top_center.configure(text="Administrando Reservas...")
            reservas = Terminal.getReservas()
            
            def devolucionLlamado(formularioReservas):
                partes = formularioReservas.split(":")
                indiceSeleccionado = int(partes[1].strip())
                global viajeSelect
                viajeSelect = reservas[indiceSeleccionado-1]
                print(f"indiceSeleccionado: {indiceSeleccionado} Viaje: {viajeSelect.getId()}")

                # CREAR UN NUEVO FORMULARIO.
                seleccionAdministrarReserva()

            def seleccionAdministrarReserva():
                def devolucionLlamado(formularioDatosAdministrar):
                    if (formularioDatosAdministrar[criterios[0]] == "Ver detalles Reserva"):
                        verDetallesReserva()
                    elif (formularioDatosAdministrar[criterios[0]] == "Cancelar Reserva"):    
                        cancelarReserva()

                def verDetallesReserva():
                    print("ver Detalles Reserva")
                    label_top_center.configure(text=f"Detalles del Viaje con ID = {viajeSelect.getId()}")

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Administrar otra Reserva", "Terminar Proceso"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles de la reserva", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= administraciondeReservas, metodo2= funcionalidad5)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def cancelarReserva():
                    print("Cancelar Viajes")
                    label_top_center.configure(text=f"Cancelar el Viaje con ID = {viajeSelect.getId()}")

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Regresar", "Cancelar"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles de la reserva", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= administraciondeReservas, metodo2= cancelar)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def cancelar():
                    try:
                        a = Terminal.cancelarViajeAbsoluto(viajeSelect)
                            
                        if a == "El viaje no tenía pasajeros":
                                
                                # Ventana emergente confirmando que no había pasajeros
                                messagebox.showinfo("Información", "Reserva Cancelada")
                                funcionalidad5()
                            
                        elif a == "Viaje cancelado":
                            # Ventana emergente confirmando que el viaje fue cancelado
                            messagebox.showinfo("Confirmación", "La reserva ha sido cancelado exitosamente.")
                            funcionalidad5()
                        else:
                            # Ventana emergente para mostrar un mensaje de error
                            messagebox.showerror("Error", "No se pudo cancelar la Reserva. Por favor, intente nuevamente.")
                            cancelarReserva()
                        
                    except Exception as e:
                        # Manejo de excepciones y ventana emergente para errores
                        messagebox.showerror("Error", f"Ocurrió un error: {e}")
                        cancelarReserva()

                criterios = [f"Administrar Reserva con ID : {viajeSelect.getId()}"]
                valores_iniciales = ["Ver detalles Reserva", "Cancelar Reserva"]
                habilitado = [False, False]

                # Create the FieldFrame widget
                field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                # Agregar el nuevo frame debajo de la tabla
                field_frame.grid(row=0, column=0, sticky="nsew")
                frame_bottom.grid_rowconfigure(0, weight=1)
                frame_bottom.grid_columnconfigure(0, weight=1)
            
            titulo_criterios = ["Opción", "Id", "Llegada", "Fecha", "Hora", "Transportadora", "Vehiculo"]
            atributos  = ["getId", "getLlegada", "getFecha", "getHora", "getTransportadora.getNombre", "getVehiculo.getTipo"]
            habilitado = [False, False, False, False, False, False, False]

            tabla = TablaFrameDinamica(tituloCriterios= titulo_criterios, atributos = atributos, parent = frame_bottom, lista = reservas, habilitado=habilitado, devolucionLlamado = devolucionLlamado)
            # Ubica la tabla en el centro del frame
            # UBICACIÓN DEL FIELD FRAME
            tabla.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)


        def administracionViaje():
            label_top_center.configure(text="Administrando Viajes...")
            viajes = Terminal.getViajes()
            
            def devolucionLlamado(formularioViajes):
                partes = formularioViajes.split(":")
                indiceSeleccionado = int(partes[1].strip())
                global viajeSelect
                viajeSelect = viajes[indiceSeleccionado-1]
                print(f"indiceSeleccionado: {indiceSeleccionado} Viaje: {viajeSelect.getId()}")

                # CREAR UN NUEVO FORMULARIO.
                seleccionAdministrarViaje()


            titulo_criterios = ["Opción", "Id", "Llegada", "Fecha", "Hora", "Transportadora", "Vehiculo"]
            atributos  = ["getId", "getLlegada", "getFecha", "getHora", "getTransportadora.getNombre", "getVehiculo.getTipo"]
            habilitado = [False, False, False, False, False, False, False]

            tabla = TablaFrameDinamica(tituloCriterios= titulo_criterios, atributos = atributos, parent = frame_bottom, lista = viajes, habilitado=habilitado, devolucionLlamado = devolucionLlamado)
            # UBICACIÓN DE LA TABLA
            tabla.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

            def seleccionAdministrarViaje():
                def devolucionLlamado(formularioDatosAdministrar):
                    if (formularioDatosAdministrar[criterios[0]] == "Ver detalles"):
                        verDetalles()
                    elif (formularioDatosAdministrar[criterios[0]] == "Cancelar"):    
                        cancelarViaje()

                def verDetalles():
                    print("ver Detalles")
                    label_top_center.configure(text=f"Detalles del Viaje con ID = {viajeSelect.getId()}")
                    def devolucionLlamado():
                        pass

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Administrar Otro Viaje", "Terminar Proceso"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos= nombreMetodos, metodo1=administracionViaje , metodo2 = funcionalidad5)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)
                    

                def cancelarViaje():
                    print("Cancelar Viajes")

                    label_top_center.configure(text=f"Cancelar el Viaje con ID = {viajeSelect.getId()}")

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Regresar", "Cancelar"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos= nombreMetodos, metodo1=administracionViaje , metodo2 = cancelar)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def cancelar():
                    try:
                        a = Terminal.cancelarViajeAbsoluto(viajeSelect)
                                
                        if a == "El viaje no tenía pasajeros":
                                    
                                # Ventana emergente confirmando que no había pasajeros
                                messagebox.showinfo("Información", "El viaje no tenía pasajeros.")
                                funcionalidad5()
                                
                        elif a == "Viaje cancelado":
                            # Ventana emergente confirmando que el viaje fue cancelado
                            messagebox.showinfo("Confirmación", "El viaje ha sido cancelado exitosamente.")
                            funcionalidad5()
                        else:
                            # Ventana emergente para mostrar un mensaje de error
                            messagebox.showerror("Error", "No se pudo cancelar el viaje. Por favor, intente nuevamente.")
                            cancelarViaje()
                            
                    except Exception as e:
                        # Manejo de excepciones y ventana emergente para errores
                        messagebox.showerror("Error", f"Ocurrió un error: {e}")
                        cancelarViaje()

                criterios = [f"Administrar viaje con ID : {viajeSelect.getId()}"]
                valores_iniciales = ["Ver detalles", "Cancelar"]
                habilitado = [False, False]

                
                field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                field_frame.grid(row=0, column=0, sticky="nsew")
                frame_bottom.grid_rowconfigure(0, weight=1)
                frame_bottom.grid_columnconfigure(0, weight=1)

        def administracionHistorial():
            label_top_center.configure(text="Administrando Historial...")
            viajesHistorial = Tiempo.listahistorial()
            
            def devolucionLlamado(formularioViajes):
                partes = formularioViajes.split(":")
                indiceSeleccionado = int(partes[1].strip())
                global viajeSelect
                viajeSelect = viajesHistorial[indiceSeleccionado-1]
                print(f"indiceSeleccionado: {indiceSeleccionado} Viaje: {viajeSelect.getId()}")

                # CREAR UN NUEVO FORMULARIO.
                seleccionAdministrarViaje()


            titulo_criterios = ["Opción", "Id", "Llegada", "Fecha", "Hora", "Transportadora", "Vehiculo"]
            atributos  = ["getId", "getLlegada", "getFecha", "getHora", "getTransportadora.getNombre", "getVehiculo.getTipo"]
            habilitado = [False, False, False, False, False, False, False]

            tabla = TablaFrameDinamica(tituloCriterios= titulo_criterios, atributos = atributos, parent = frame_bottom, lista = viajesHistorial, habilitado=habilitado, devolucionLlamado = devolucionLlamado)
            # UBICACIÓN DE LA TABLA
            tabla.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

            def seleccionAdministrarViaje():
                global fieldFrameInferior
                def devolucionLlamado(formularioDatosAdministrar):
                    if (formularioDatosAdministrar[criterios[0]] == "Reprogramar"):
                        reprogramar()
                    elif (formularioDatosAdministrar[criterios[0]] == "Ver más información"):    
                        verInformación()
                    elif (formularioDatosAdministrar[criterios[0]] == "Ver pasajeros"):
                        verPasajeros()

                criterios = [f"Administrar viaje con ID : {viajeSelect.getId()}"]
                valores_iniciales = ["Reprogramar", "Ver más información", "Ver pasajeros"]
                habilitado = [False, False, False]

                field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                field_frame.grid(row=0, column=0, sticky="nsew")
                frame_bottom.grid_rowconfigure(0, weight=1)
                frame_bottom.grid_columnconfigure(0, weight=1)
                    

                def verPasajeros():
                    label_top_center.configure(text=f"Pasajeros del Viaje con ID = {viajeSelect.getId()}")
                    def devoluciónLlamado():
                        pass

                    
                    

                def verInformación():
                    label_top_center.configure(text=f"Detalles del Viaje con ID = {viajeSelect.getId()}")

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Administrar Otro Viaje", "Terminar Proceso"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos= nombreMetodos, metodo1=administracionHistorial , metodo2 = funcionalidad5)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def reprogramar():
                    label_top_center.configure(text=f"Reprogramación del Viaje con ID = {viajeSelect.getId()}")
                    def devolucionLlamado():
                        pass # ResultFrame

                criterios = [f"Administrar viaje con ID : {viajeSelect.getId()}"]
                valores_iniciales = ["Reprogramar", "Ver más información", "Ver pasajeros"]
                habilitado = [False, False]

                # Create the FieldFrame widget
                fieldFrameInferior = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                field_frame.grid(row=0, column=0, sticky="nsew")
                frame_bottom.grid_rowconfigure(0, weight=1)
                frame_bottom.grid_columnconfigure(0, weight=1)
    
    
    def estructura_frames(titulo,descripcion):
        frame_top.destroy()
        frame_bottom.destroy()

        new_frame_top = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
        new_frame_center = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
        new_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])

        new_frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        new_frame_center.place(relx=0, rely=0.15, relwidth=1, relheight=0.1)
        new_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

        label_top_center = tk.Label(new_frame_top, text=titulo, font=("Segoe Script", 35, "bold"), fg=colors["amarillo"], bd=3, bg=colors["background"], relief="ridge")
        label_center_center = tk.Label(new_frame_center, text=descripcion, font=("Arial", 10, "bold"), fg=colors["text"], bd=3, bg=colors["background"])

        label_top_center.place(relx=0.5,rely=0.5, anchor="center")
        label_center_center.place(relx=0.5,rely=0.5, anchor="center")

        return [new_frame_bottom,label_top_center,label_center_center] #Retorna el frame de abajo, con el cual se haran los respectivos procesos y consultas
        #lista[0] es el frame de abajo
        #lista[1] es el titulo grande de arriba
        #lista[2] es la descripcion
    
# MÉTODOS PARA EL MENÚ 

def mensajeEmergente():
    messagebox.showinfo("Información básica", "Nuestra aplicación permite la gestion de una Terminal de Transporte...")

def mensajeAcerdade():
    messagebox.showinfo("Quienes somos", " Santiago Ochoa Cardona \n Johan Ramirez Marin \n Jaime Luis Osorio Gomez \n Juan Camilo Marin Valencia \n Jonathan David Osorio Restrepo")

def salir(ventanaPrincipal, ventanaInicio):
    ventanaPrincipal.destroy()
    ventanaInicio.deiconify()

