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
from src.excepciones.notEnoughExperienceException import NotEnoughExperienceException
from src.excepciones.notLicenceException import notLicenceException

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
    label_bottom_left_extra = tk.Label(frame_bottom_left, text="💸", font=("Century", 180), fg=colors["text"], bd=0, bg=colors["background"])

    label_bottom_right_tp = tk.Label(frame_bottom_right, text="¿Qué puede hacer?", font=("Small fonts", 20), fg=colors["text"], bd=3, bg=colors["naranja"])
    label_bottom_right_bt = tk.Label(frame_bottom_right, text="Para utilizar tus diferentes funcionalidades de administración debes\nir a la barra superior de menús, en la pestaña (Procesos y consultas)\nse desplegarán todas la operaciones que puedes realizar al seleccionar\nalguna de estas opciones se mostrará la interfaz respectiva, donde se\ndara una breve descripción y los diferentes formularios necesarios\npara la ejecución de la misma.\n\nRecuerda que en la pestaña (Archivo) tienes las opciones de (Aplicación)\nla cual te dara información acerca del sistema, y (Salir) te regresará al\na la ventana de Inicio.", font=("Century", 13), fg=colors["text"], bd=3, bg=colors["background"])
    label_bottom_right_extra = tk.Label(frame_bottom_right, text="🚌", font=("Century", 130), fg=colors["text"], bd=0, bg=colors["background"])

    # UBICAR LOS LABELS INFERIORES EN CADA FRAME CON .place()
    label_bottom_left_tp.place(relx=0.5, rely=0.05, anchor="n")
    label_bottom_left_bt.place(relx=0.5, rely=0.2, anchor="n")
    label_bottom_left_extra.place(relx=0.5, rely=0.45, relwidth=0.9, relheight=0.5, anchor="n")

    label_bottom_right_tp.place(relx=0.5, rely=0.05, anchor="n")
    label_bottom_right_bt.place(relx=0.5, rely=0.2, anchor="n")
    label_bottom_right_extra.place(relx=0.5, rely=0.65, relwidth=0.9, relheight=0.3, anchor="n")

    ventanaPrincipal.protocol("WM_DELETE_WINDOW", lambda: salir(ventanaPrincipal, ventanaInicio))

    # FUNCIONALIDADES
    def funcionalidad1():
        from src.gestorAplicacion.administrativo.transportadora import Transportadora
        from src.gestorAplicacion.usuarios.pasajero import Pasajero
        from src.excepciones.noViajesErrorDestino import NoViajesErrorDestino
        from src.excepciones.noViajesErrorTipoPasajero import NoViajesErrorTipoPasajero
        from src.excepciones.noViajesErrorModalidad import NoViajesErrorModalidad
        #VARIABLES PARA LA FUNCIONALIDAD
        #print(len(Terminal.getPasajeros()))
        #for viaje in Terminal.getViajes():
        #   print(len(viaje.getPasajeros()))

        lista = estructura_frames("Venta Viajes", "Esta página está destinada al administrador para gestionar la oferta de viajes.\n" + 
                                "Permite definir detalles clave como el destino, el tipo de pasajero, la modalidad de viaje,\n" + 
                                "el tipo de vehículo y la transportadora. Facilita una administración eficiente, asegurando\n" +
                                "que las opciones de viaje se ajusten adecuadamente a las necesidades del usuario. 🚍")
        frame_bottom = lista[0]
        label_top_center = lista[1]
        label_center_center = lista[2]
        label_top_center.configure(text="🚎Venta de Viajes🚌")

        def elegirDestino(): # 1
            def devolucionLlamado(formularioDatos):
                global destinoDeseado
                global viajesDisponibles

                try:
                    # Suponiendo que 'formularioDatos' es un diccionario y contiene un único destino
                    destino_nombre = list(formularioDatos.values())[0]
                    
                    # Convertir el nombre del destino a un Enum
                    destinoDeseado = Destino[destino_nombre] 
                    viajesDisponibles = Terminal.viajesDestino(destinoDeseado)

                    for viaje in viajesDisponibles:
                        print(viaje.getVehiculo().getTipo().name)

                    if len(viajesDisponibles) == 0:
                        raise NoViajesErrorDestino(destinoDeseado)
                    
                    else:
                        elegirTipoPasajero()

                except NoViajesErrorDestino:
                    pass
                
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
                valores=destinos[1:],
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
                global cantidad
                tipoPasajero = list(formularioDatos.values())[0]
                tipoPasajero = TipoPasajero[tipoPasajero]

                if tipoPasajero == TipoPasajero.ESTUDIANTE:
                    try:
                        viajesDisponibles2 = Terminal.viajesParaEstudiantes(viajesDisponibles)
                        if len(viajesDisponibles2) != 0:
                            viajesDisponibles = viajesDisponibles2
                            cantidad = 1
                            elegirTipoVehiculoEstudiante()
                                    
                        elif len(viajesDisponibles2)==0:

                            raise NoViajesErrorTipoPasajero(tipoPasajero)
                    
                    except NoViajesErrorTipoPasajero:
                        pass

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
                tipo = list(formularioDatos.values())[0]
                tipoVehiculo = TipoVehiculo[tipo]
                viajesDisponibles2 = Terminal.viajesParaEstudiantes(viajesDisponibles,tipo)

                if len(viajesDisponibles2) == 0:

                    elegirTipoVehiculoEstudiante()
                else:
                    viajesDisponibles = viajesDisponibles2
                    elegirTransportadora()

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
        
        def elegirTransportadora():#estudiante 4.0 

            """Elegir el primer viaje que encuentre de la transportadora"""
                    
            def devolucionLlamado(formularioDatos):

                global viajeSeleccionado
                global tipoPasajero
                global viajesDisponibles
                indice = int(formularioDatos.split(" ")[-1])
                transportadora = transportadoras[indice-1]
                
                #for viaje in transportadora.getViajesAsignados():
                for viaje in viajesDisponibles:
                    if viaje.getVehiculo().getTransportadora() == transportadora:
                        viajeSeleccionado = viaje
                        break

                mostrarInformacionViaje()
                    
            global transportadoras

            transportadoras =Terminal.transportadorasViaje(viajesDisponibles)

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
                        
        
        def elegirModalidad():

            def devolucionLlamado(formularioDatos):
                global viajesDisponibles
                global viajeSeleccionado
                print(formularioDatos)

                 
                if formularioDatos['Modalidad'] == "Mayor velocidad":
                    try:
                        viajeSeleccionado = Terminal.masRapido(viajesDisponibles)
                        if not viajeSeleccionado:
                             
                            raise NoViajesErrorModalidad(modalidad[0])
                        else:
                            mostrarInformacionViaje()
                    except NoViajesErrorModalidad:
                        pass           

                elif formularioDatos['Modalidad'] == "Más económico":
                    try:
                        viajeSeleccionado = Terminal.masEconomico(viajesDisponibles)
                        if not viajeSeleccionado:
                            raise NoViajesErrorModalidad(modalidad[1])
                        else:
                            mostrarInformacionViaje()

                    except NoViajesErrorModalidad:
                        pass 
                
                elif formularioDatos['Modalidad'] == "Transportadora":
                    elegirTransportadora()

                elif formularioDatos['Modalidad'] == "Salida con mayor antelación":
                    viajeSeleccionado = Terminal.obtenerViajeMasProximo(viajesDisponibles)
                    try:
                        if not viajeSeleccionado:
                            raise NoViajesErrorModalidad(modalidad[3])
                        else:
                            mostrarInformacionViaje()
                    except NoViajesErrorModalidad:
                        pass
                        
                    
            criterios = ["Modalidad"]
            modalidad= ["Mayor velocidad",
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
                valores=modalidad,
                habilitado=habilitado,
                devolucionLlamado= devolucionLlamado
                )


            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

        def elegirCantidad():
            global tipoPasajero
            def devolucionLlamado(formularioDatos):
                global cantidad
                global viajesDisponibles
                #on_submit(formularioDatos)
                #if formilario["cantidad"]==None:
                #   print()
                if isinstance(formularioDatos, dict):
                # Convierte los valores del diccionario en una lista
                    lista = sacarValores(formularioDatos)
                    print(lista)
                    
                    if len(lista) > 2:
                        cantidad = int(lista[2])
                        if cantidad > 15:
                                messagebox.showinfo("Sin viajes disponibles", "No se vende una cantidad superior a 15")
                                elegirCantidad()
                        else:

                            if tipoPasajero == TipoPasajero.DISCAPACITADO or tipoPasajero == TipoPasajero.REGULAR:
                                viajesDisponibles2 = Terminal.viajesParaRegularesYDiscapacitados(cantidad, viajesDisponibles)
                                if len(viajesDisponibles2) == 0:

                                    mayorCantidad = 0
                                    
                                    for viaje in viajesDisponibles:
                                        asientos = viaje.verificarAsientos()
                                        if asientos > mayorCantidad:
                                            mayorCantidad = asientos

                                    messagebox.showinfo("Sin viajes disponibles", f"Insuficiencia de cupos, máximo de cupos en este caso {mayorCantidad}")
                                    elegirTipoPasajero()

                                else:
                                    viajesDisponibles = viajesDisponibles2

                                    elegirModalidad()

                            elif tipoPasajero == TipoPasajero.VIP:
                                viajesDisponibles2 = Terminal.viajesParaVips(cantidad, viajesDisponibles)
                                if len(viajesDisponibles2) == 0:

                                    mayorCantidad = 0
                                    
                                    for viaje in viajesDisponibles:
                                        asientos = viaje.verificarAsientos()
                                        if asientos > mayorCantidad:
                                            mayorCantidad = asientos

                                    if mayorCantidad > 0: 
                                        messagebox.showinfo("Sin viajes disponibles", f"Insuficiencia de cupos, máximo de cupos en este caso {mayorCantidad}")
                                        elegirTipoPasajero()
                                else:
                                    viajesDisponibles = viajesDisponibles2

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
            devolucionLlamado= devolucionLlamado  # Aquí se usa 'devolucionLlamado'
            )
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

        def sacarValores(dic):
            lista = list(dic.values())
            return lista
        
        def separarPasajeros1():
            global viajesDisponibles

            if tipoPasajero == TipoPasajero.VIP:
                viajesDisponibles2 = Terminal.viajesParaVips(viajesDisponibles)

                if len(viajesDisponibles2)==0:
                    messagebox.showinfo("Sin viajes disponibles", "No hay viajes disponibles para este tipo de pasajero")
                    elegirTipoPasajero()
                else:
                    viajesDisponibles = viajesDisponibles2
                    elegirCantidad()
            
            else:
                elegirCantidad()
        
        def mostrarInformacionViaje():
            global viajeSeleccionado

            def metodo1():
                elegirTipoPasajero()
            def metodo2():
                pedirInformacion()

            atributos = ["ID","Hora salida","Fecha salida","Tipo vehiculo","Transportadora", "Tarifa"]
            rutas = ["getId","getHora", "getFecha", "getVehiculo.getTipo","getVehiculo.getTransportadora.getNombre", "getTarifa" ]

            label_top_center.configure(text=f"Detalles del Viaje con ID = {viajeSeleccionado.getId()}")

            nombreMetodos = ["Cambiar tipo pasajero", "Solicitar información"]

            resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje", objeto=viajeSeleccionado, criterios=atributos, valores=rutas, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= metodo1, metodo2= metodo2)

            resultadosOperacion.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)
        
        def pedirInformacion():
            global cantidad
            print(cantidad)

            valorAPagar = cantidad*(viajeSeleccionado.getTarifa())

            def devolucionLlamado(formularioDatos):
                global tipoPasajero
                global tipoVehiculo
                global viajesDisponibles
                global viajeSeleccionado

                if isinstance(formularioDatos, dict):
                    lista = list(formularioDatos.values())
                    if len(lista) >= 7:
                        nombre = str(lista[0])
                        tipo = TipoPasajero[lista[1]]
                        id = int(lista[2])
                        edad = int(lista[3])
                        cantidad = float(lista[4])  # Corrección aquí
                        valorAPagar = float(lista[5])
                        valorPagado = float(lista[6])


                        # Solo crea el pasajero si todas las variables están inicializadas
                        if nombre and tipo and id and edad:
                            pasajero = Pasajero(tipo, id, edad, nombre)
                            print(pasajero)
                            print(f"Pasajero creado: Nombre: {nombre}, Tipo: {tipo}, ID: {id}, Edad: {edad}")
                            compararValores(valorAPagar, valorPagado, pasajero)

                        else:
                            print("Datos incompletos para crear el pasajero.")
                    else:
                        print("Datos insuficientes en el formulario.")
                else:
                    print("El formulario no es un diccionario.")

                                
            criterios = ["Nombre", "Tipo pasajero", "Id", "Edad", "Cantidad", "Valor a pagar", "Valor pagado"]
            habilitado = [True, False, True, True, False, False, True]

            field_frame = FieldFrame(
            parent=frame_bottom,
            tituloCriterios="Criterio",
            criterios=criterios,
            tituloValores="Información",
            valores=["", tipoPasajero.name, "","", cantidad, valorAPagar, ""],
            habilitado=habilitado,
            devolucionLlamado=devolucionLlamado  # Aquí se usa 'devolucionLlamado'
            )

            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

        def compararValores(cantidadEsperada, cantidadDada, pasajero):
            if cantidadDada >= cantidadEsperada:
                pasajero.setDinero(cantidadEsperada)
                print(pasajero.getDinero())
                pasajero.setViaje(viajeSeleccionado)
                print(pasajero.getViaje())
                messagebox.showinfo("Buen viaje", "Venta realizada con éxito. Regresando")
                funcionalidad1()
            else:
                messagebox.showinfo("Dinero insuficiente", "Cantidad de dinero insuficiente. Regresando")
                elegirDestino()
        
        elegirDestino()


    def funcionalidad2():
        from src.gestorAplicacion.administrativo.transportadora import Transportadora

        lista = estructura_frames("Elegir transportadora","Esta funcionalidad permite gestionar la administración de los conductores asignados a las transportadoras. A través de esta función,\n se pueden realizar acciones como despedir, contratar y modificar conductores. Facilita la asignación y desvinculación de viajes y vehículos a los conductores,\n según su disponibilidad.También permite modificar aspectos específicos del conductor, como sus viajes programados o el vehículo asociado, \nseleccionando la transportadora correspondiente para una gestión organizada del personal.")
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

            label_top_center.config(text="Seleccione una opcion")
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

                    label_top_center.config(text="Contratando...")

                    try:
                        if driver.getExperiencia() >= 5:
                            if driver.getLicencia() == "Activa":
                                new7_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                new7_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)


                                transportadora.contratarConductor(driver)
                                mostrar = ["ID", "Nombre","Edad","Experiencia","Transportadora"] # ASIENTOS -- P1
                                valores = ["getId", "getNombre", "getEdad", "getExperiencia", "getTransportadora.getNombre"]
                                nombreMetodos = ["Salir de la aplicacion", "Gestionar conductores"]


                                resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del conductor contratado", objeto=driver, criterios=mostrar, valores=valores, parent= new7_frame_bottom, nombreMetodos=nombreMetodos, metodo1= lambda:salir(ventanaPrincipal, ventanaInicio), metodo2= funcionalidad2)
                                resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                new7_frame_bottom.grid_rowconfigure(0, weight=1)
                                new7_frame_bottom.grid_columnconfigure(0, weight=1)
                                messagebox.showinfo("Contratacion exitosa","Se contrato al conductor " + driver.getNombre() + " exitosamente.")
                            else:
                                raise notLicenceException(driver.getNombre())
                        else:
                            raise NotEnoughExperienceException(driver.getNombre())
                    except notLicenceException:
                        pass
                    except NotEnoughExperienceException:
                        pass
                        
                    

                    #Mostrar que se contrato a un conductor



                def devolucion_despedir(valor):
                    true_value = int(valor.split(" ")[2])
                    driver = transportadora.getConductores()[true_value-1]
                    label_top_center.config(text="Despidiendo...")

                    if len(driver.getHorario()) == 0:
                        if len(driver.getVehiculo().getConductores()) >= 2:


                            new7_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                            new7_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                            mostrar = ["ID", "Nombre","Edad","Experiencia","Transportadora"] # ASIENTOS -- P1
                            valores = ["getId", "getNombre", "getEdad", "getExperiencia", "getTransportadora.getNombre"]
                            nombreMetodos = ["Salir de la aplicacion", "Gestionar conductores"]
                            transportadora.despedirConductor(driver)


                            resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del conductor despedido", objeto=driver, criterios=mostrar, valores=valores, parent= new7_frame_bottom, nombreMetodos=nombreMetodos, metodo1= lambda:salir(ventanaPrincipal, ventanaInicio), metodo2= funcionalidad2)
                            resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                            new7_frame_bottom.grid_rowconfigure(0, weight=1)
                            new7_frame_bottom.grid_columnconfigure(0, weight=1)
                            messagebox.showinfo("Despido exitoso","Se despidio al conductor " + driver.getNombre() + " exitosamente.")
                        else:
                            messagebox.showerror("No se puede despedir","No se puede despedir el conductor " + driver.getNombre() + " porque el vehiculo al que esta asociado no tiene mas conductores vinculados")


                    else:
                        messagebox.showerror("No se puede despedir","No se puede despedir el conductor " + driver.getNombre() + " porque tiene viajes programados")
                    #Mostar que se despidio a un conductor


                def devolucion_modificar(valor):
                    true_value = int(valor.split(" ")[2])

                    conductor = transportadora.getConductores()[true_value-1]

                    new3_frame_bottom.destroy()

                    label_top_center.config(text="Modificar conductor")

                    new4_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                    new4_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                    criterios = ["Modificaciones"]
                    valores_iniciales = ["Viaje","Vehiculo"]
                    habilitado = [False, False]

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
                                    


                                    if conductor.getVehiculo() is not None:

                                        if len(transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor)) != 0:
                                            new5_frame_bottom.destroy()
                                            new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                            new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                            def devolucion_tomar_viaje(a):
                                                true_value = int(a.split(" ")[2])
                                                retorno =  transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor)[true_value-1]
                                                new7_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                                new7_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                                label_top_center.config(text="Reasignacion viaje")

                                                mostrar = ["ID", "Conductor","Placa vehiculo", "Destino","Fecha"] # ASIENTOS -- P1
                                                valores = ["getId", "getConductor.getNombre", "getVehiculo.getPlaca", "getLlegada.getName","getFecha"]
                                                nombreMetodos = ["Salir de la aplicacion", "Gestionar conductores"]


                                                resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje reasignado", objeto=retorno, criterios=mostrar, valores=valores, parent= new7_frame_bottom, nombreMetodos=nombreMetodos, metodo1= lambda:salir(ventanaPrincipal, ventanaInicio), metodo2= funcionalidad2)
                                                resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                                new7_frame_bottom.grid_rowconfigure(0, weight=1)
                                                new7_frame_bottom.grid_columnconfigure(0, weight=1)
                                                messagebox.showinfo("Asignacion exitosa","Se ha reasignado el viaje al conductor " + conductor.getNombre())



                                            viajes_disponibles_tabla = TablaFrame(["Opcion","Destino","Fecha","Hora llegada"], ["Llegada","Fecha","Hora"], new6_frame_bottom, transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor), [False,False,False], devolucionLlamado=devolucion_tomar_viaje)
                                            viajes_disponibles_tabla.place(relx=0.5,rely=0.5,anchor="center")
                                        else:
                                            messagebox.showerror("No es posible","No se le puede asignar viajes al conductor " + conductor.getNombre() + " porque no hay viajes disponibles.")
                                            funcionalidad2()
                                    else:
                                        messagebox.showerror("No es posible","No se le puede asignar viajes al conductor" + conductor.getNombre() + " porque no tiene vehiculo asociado.")
                                        funcionalidad2()
                                
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

                                    
                                    if valor["Modificar viaje"] == "Asignar viaje":
                                        """new5_frame_bottom.destroy()

                                        new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                        new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                        #if transportadora.obtenerViajesDisponibles(Tiempo.Dia.getValue(), conductor.getTipoVehiculo(), conductor):

                                        def prueba(valor):
                                            pass
                                        if len(transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor)) != 0:
        

                                            viajes_disponibles_tabla_2 = TablaFrameDinamica(["Opcion","Destino","Fecha","Hora llegada"], ["getLlegada","getFecha","getHora"], new6_frame_bottom, transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor), [False,False,False], devolucionLlamado=prueba )
                                            viajes_disponibles_tabla_2.place(relx=0.5,rely=0.5,anchor="center")
                                        
                                        else:
                                            messagebox.showerror("No es posible","No se le puede asignar viajes al conductor " + conductor.getNombre() + " porque no hay viajes disponibles.")"""
                                        if conductor.getVehiculo() is not None:

                                            if len(transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor)) != 0:
                                                new5_frame_bottom.destroy()
                                                new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                                new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                                def devolucion_tomar_viaje(a):
                                                    true_value = int(a.split(" ")[2])
                                                    retorno =  transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor)[true_value-1]
                                                    new7_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                                    new7_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                                    label_top_center.config(text="Reasignacion viaje")

                                                    mostrar = ["ID", "Conductor","Placa vehiculo", "Destino","Fecha"] # ASIENTOS -- P1
                                                    valores = ["getId", "getConductor.getNombre", "getVehiculo.getPlaca", "getLlegada.getName","getFecha"]
                                                    nombreMetodos = ["Salir de la aplicacion", "Gestionar conductores"]


                                                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje reasignado", objeto=retorno, criterios=mostrar, valores=valores, parent= new7_frame_bottom, nombreMetodos=nombreMetodos, metodo1= lambda:salir(ventanaPrincipal, ventanaInicio), metodo2= funcionalidad2)
                                                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                                    new7_frame_bottom.grid_rowconfigure(0, weight=1)
                                                    new7_frame_bottom.grid_columnconfigure(0, weight=1)
                                                    messagebox.showinfo("Reasignacion exitosa","Se ha reasignado el viaje al conductor " + conductor.getNombre())


                                                viajes_disponibles_tabla = TablaFrame(["Opcion","Destino","Fecha","Hora llegada"], ["Llegada","Fecha","Hora"], new6_frame_bottom, transportadora.mostrarViajesDisponibles(Tiempo.getTiempos()[0].tener_dia().getValue(), conductor.getVehiculo().getTipo(), conductor), [False,False,False], devolucionLlamado=devolucion_tomar_viaje)
                                                viajes_disponibles_tabla.place(relx=0.5,rely=0.5,anchor="center")
                                            else:
                                                messagebox.showerror("No es posible","No se le puede asignar viajes al conductor " + conductor.getNombre() + " porque no hay viajes disponibles.")
                                                funcionalidad2()
                                            
                                        else:
                                            messagebox.showerror("No es posible","No se le puede asignar viajes al conductor" + conductor.getNombre() + " porque no tiene vehiculo asociado.")
                                            funcionalidad2()


                                    if valor["Modificar viaje"] == "Desvincular viaje":
                                        new5_frame_bottom.destroy()

                                        new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                        new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                        def devolucion_desvincular_vincular(valor):
                                            value = int(valor.split(" ")[2])  
                                            trip = conductor.getHorario()[value-1]      
                                            
                                            new6_frame_bottom.destroy()
                                            
                                            new7_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                            new7_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)  

                                            if len(transportadora.conductoresDisponiblesViaje(trip)) != 0:

                                                def devolucion_desvincular_paso_final(lom):
                                                    other_value = int(lom.split(" ")[2]) 

                                                    other_conductor = transportadora.conductoresDisponiblesViaje(trip)[other_value-1]
                                                    new7_frame_bottom.destroy()

                                                    conductor.desvincularYVincular(other_conductor,trip)
                                                    
                                                    mostrar = ["ID", "Conductor","Placa vehiculo", "Destino","Fecha"] # ASIENTOS -- P1
                                                    valores = ["getId", "getConductor.getNombre", "getVehiculo.getPlaca", "getLlegada.getName","getFecha"]
                                                    nombreMetodos = ["Salir de la aplicacion", "Gestionar conductores"]

                                                    label_top_center.config(text="Desvinculacion viaje")

                                                    new8_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                                    new8_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)  

                                                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje reasignado", objeto=trip, criterios=mostrar, valores=valores, parent= new8_frame_bottom, nombreMetodos=nombreMetodos, metodo1= lambda:salir(ventanaPrincipal, ventanaInicio), metodo2= funcionalidad2)
                                                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                                    new8_frame_bottom.grid_rowconfigure(0, weight=1)
                                                    new8_frame_bottom.grid_columnconfigure(0, weight=1)
                                                    messagebox.showinfo("Reasignacion correcta","Se le ha asignado el viaje a " + other_conductor.getNombre())


                                                tabla_vehiculo_asociado = TablaFrame(["Opcion","Nombre","Id","Experiencia"], ["Nombre","Id","Experiencia"], new7_frame_bottom, transportadora.conductoresDisponiblesViaje(trip), [False,False,False], devolucionLlamado=devolucion_desvincular_paso_final)
                                                tabla_vehiculo_asociado.place(relx=0.5,rely=0.5,anchor="center") 
                                            else:
                                                messagebox.showerror("No es posible","No se puede desvincular el viaje al conductor " + conductor.getNombre() + " porque no hay conductores disponibles que puedan tomar el viaje")
                                                funcionalidad2()
                                            


        

                                        viajes_disponibles_tabla_2 = TablaFrameDinamica(["Opcion","Destino","Fecha"], ["getLlegada","getFecha"], new6_frame_bottom, conductor.getHorario(), [False,False,False], devolucionLlamado=devolucion_desvincular_vincular)
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

                                    label_top_center.config(text="Vehiculo a desvincular...")

                                    new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                    new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                    def devolucion_desvincular_verificacion(valor):

                                        if len(conductor.getHorario()) == 0:
                                            if len(conductor.getVehiculo().getConductores()) >= 2:
                                                
                                                vehicle = conductor.getVehiculo()
                                                new7_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                                new7_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                                mostrar = ["Precio", "Placa","Transportadora"] # ASIENTOS -- P1
                                                valores = ["getPrecio", "getPlaca", "getTransportadora.getNombre"]
                                                nombreMetodos = ["Salir de la aplicacion", "Gestionar conductores"]

                                                label_top_center.config(text="Desvinculacion vehiculo")

                                                resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del vehiculo desvinculado", objeto=vehicle, criterios=mostrar, valores=valores, parent= new7_frame_bottom, nombreMetodos=nombreMetodos, metodo1= lambda:salir(ventanaPrincipal, ventanaInicio), metodo2= funcionalidad2)
                                                resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                                new7_frame_bottom.grid_rowconfigure(0, weight=1)
                                                new7_frame_bottom.grid_columnconfigure(0, weight=1)   

                                                messagebox.showinfo("Desvinculacion exitosa","Se le ha desvinculado el vehiculo a " + conductor.getNombre())                                                 
                                            else:
                                                messagebox.showerror("No es posible","No se puede desvincular el vehiculo a " + conductor.getNombre() + " porque no hay mas conductores aociados al vehiculo.")
                                                funcionalidad2()
                                            #No se puede porque no hay mas conductores asociados al vehiculo
                                            
                                        else:
                                            pass
                                            print(conductor.getHorario())
                                            messagebox.showerror("No es posible","No se puede desvincular el vehiculo a " + conductor.getNombre() + " porque tiene viajes programados.")
                                            #No se puede porque el conductor tiene viajes programados
                                            funcionalidad2()

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

                                    if (len(transportadora.mostrarVehiculosDisponibles())) != 0:
                                        new5_frame_bottom.destroy()

                                        new6_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                        new6_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                        def  devolucion_vincular_vehiculo_verificacion(valor):
                                            true_value = int(valor.split(" ")[2])

                                            vehicle = transportadora.mostrarVehiculosDisponibles()[true_value-1]
                                            new7_frame_bottom = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                                            new7_frame_bottom.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

                                            conductor.tomarVehiculo(transportadora.mostrarVehiculosDisponibles()[true_value-1])

                                            mostrar = ["Precio", "Placa","Transportadora"] # ASIENTOS -- P1
                                            valores = ["getPrecio", "getPlaca", "getTransportadora.getNombre"]
                                            nombreMetodos = ["Salir de la aplicacion", "Gestionar conductores"]

                                            label_top_center.config(text="Vinculacion vehiculo")

                                            resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del vehiculo vinculado", objeto=vehicle, criterios=mostrar, valores=valores, parent= new7_frame_bottom, nombreMetodos=nombreMetodos, metodo1= lambda:salir(ventanaPrincipal, ventanaInicio), metodo2= funcionalidad2)
                                            resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                            new7_frame_bottom.grid_rowconfigure(0, weight=1)
                                            new7_frame_bottom.grid_columnconfigure(0, weight=1)   
                                            messagebox.showinfo("Vinculacion exitosa","Se ha vinculado el vehiculo al conductor " + conductor.getNombre())





                                        tabla_vehiculo_asociado = TablaFrame(["Opcion","Placa","Modelo"], ["Placa","Modelo"], new6_frame_bottom, transportadora.mostrarVehiculosDisponibles(), [False,False], devolucionLlamado=devolucion_vincular_vehiculo_verificacion)
                                        tabla_vehiculo_asociado.place(relx=0.5,rely=0.5,anchor="center")
                                    else:
                                        messagebox.showerror("No es posible","No hay vehiculos disponibles que el conductor pueda tomar.")
                                        funcionalidad2()


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
                    label_top_center.config(text="Despidiendo...")

                    fire_tabla = TablaFrameDinamica(["Opcion","Nombre","Experiencia  "], ["getNombre","getExperiencia"], new3_frame_bottom, transportadora.getConductores(), [False,False], devolucionLlamado=devolucion_despedir)
                    fire_tabla.place(relx=0.5,rely=0.5,anchor="center")

                if datos["Opciones de conductor"] == "Contratar conductor":
                    label_top_center.config(text="Contratando...")

                    hire_tabla = TablaFrame(["Opcion","Nombre","Experiencia","Licencia"], ["Nombre","Experiencia","Licencia"], new3_frame_bottom, transportadora.getConductoresRegistrados(), [False,False,False], devolucionLlamado=devolucion_contratar)
                    hire_tabla.place(relx=0.5,rely=0.5,anchor="center")

                if datos["Opciones de conductor"] == "Modificar conductor":
                    label_top_center.config(text="Modificando...")
                    
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
        
        lista = estructura_frames("Gestion de conductores","Esta funcionalidad le permitirá ver las distintas estadísticas de la terminal, se podrá consultar las transportadoras que han pagado, \n se podrá ver el dinero que tienen las transportadoras, sus conductores principales, los viajes realizados, las tarifas de los respectivos viajes de cada transportadora")
        frame_bottom = lista[0]
        label_top_center = lista[1]
        label_center_center = lista[2]

        label_top_center.configure(text="Facturación y finanzas", relief= "sunken")
        
        def devolucionLlamado(formularioDatos):
            
            if (formularioDatos[criterios[0]] == "1. Tarifas viajes"): 

                verTarifas() 
                
            elif (formularioDatos[criterios[0]] == "2. Transportadoras que han cancelado monto"):
                
                transportadorasQueHanCanceladoMonto()
            
            elif(formularioDatos[criterios[0]] == "3. Ver estadisticas generales"):
                
                estadisticasGenerales()

        criterios = ["Tipo de opciones en facturación y finanzas"] 
        valores_iniciales = ["1. Tarifas viajes", "2. Transportadoras que han cancelado monto", "3. Ver estadisticas generales"] 
        habilitado = [False, False, False] 
        
    # Create the FieldFrame widget
        field_frame = FieldFrame( parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado) 
        # UBICACIÓN DEL FIELD FRAME
        field_frame.grid(row=0, column=0, sticky="nsew")
        frame_bottom.grid_rowconfigure(0, weight=1)
        frame_bottom.grid_columnconfigure(0, weight=1)
        
        def verTarifas():
            
            label_top_center.configure(text="Tarifas viajes")
            
            criterios = ["Transportadoras"]
            valores_iniciales = [t.getNombre() for t in Terminal.getTransportadoras()]
            valores = Terminal.getTransportadoras()
            habilitado = [False, False, False, False, False, False]
            
            def devolucionLlamado(formularioDatos):
                
                for i in range(0, len(valores_iniciales)):
                    
                    if (formularioDatos[criterios[0]] == valores_iniciales[i]):
                        
                        transport = valores[i]
                        mostrarTarifasViajes(transport)
                        
            field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

            def mostrarTarifasViajes(trans):
                
                label_top_center.configure(text=f"Mostrando tarifas de {trans.getNombre()}", font=(("Segoe Script", 25, "bold")))

                def devolucionLlamado(selection):
                    
                    for i in range(0, len(trans.getViajesAsignados())):
                        
                        if (tabla_tarifas.combobox.get() == f"Opción {i+1}"):
                        
                            label = tk.Label(field_frame, text=f"El viaje tiene {len(trans.getViajesAsignados()[i].getPasajeros())}, pasajeros", font= (("Segoe Script", 15, "bold")), background="Red")

                            
                    label.grid(row=3, column=0)
                        #if selection[criterios[0]] == i:
                            
                        # label = tk.Label(tabla_tarifas, text = "hi")
                            #label.grid(row=1, column=1)
                            
                    
                        
                #if (len(trans.getViajesAsignados()) != 0):
                #frame_bottom_new = tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                #frame_bottom_new.grid_rowconfigure(0, weight=1)
                #frame_bottom_new.grid_columnconfigure(0, weight=1)
                #frame_bottom_new.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
                tabla_tarifas = TablaFrame(["No.","Salida","Llegada","Tarifa"], ["Salida","Llegada","Tarifa"], field_frame, trans.getViajesAsignados(), [False,False,False], devolucionLlamado=devolucionLlamado)
                tabla_tarifas.grid(row=0, column=0, sticky="ns")

                #else:
                    
                    #print("Mistake")

            
        def estadisticasGenerales():
            
            label_top_center.configure(text="Estadisticas generales")
            
            criterios = ["Transportadoras"]
            valores_iniciales = ["Viajes realizados por transportadora", "Ver estadísticas"]
            habilitado = [False, False]
            
            def devolucionLlamado(formularioDatos):
                
                if(formularioDatos[criterios[0]] == "Viajes realizados por transportadora"):
                    
                    mostrarViajesRealizados()
                
                if(formularioDatos[criterios[0]] == "Ver estadísticas"):
                    
                    verEstadisticasTransportadoras()
                    
            field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado = devolucionLlamado)

            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)
            
            def mostrarViajesRealizados():
                
                
                def devolucionLlamado(select):
            
                    for i in range(0, len(Terminal.getTransportadoras())):
                        
                        if (tabla_viajes.combobox.get() == f"Opción {i+1}"):
                            
                            label = tk.Label(field_frame, text=f"La transportadora tiene como conductor principal a {Terminal.getTransportadoras()[i].getConductores()[i].getNombre()}", font= (("Segoe Script", 15, "bold")), background="Red")
                            
                            label.grid(row=3, column=0)
                            
                #frame_bottom= tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                #frame_bottom.grid_rowconfigure(0, weight=1)
                #frame_bottom.grid_columnconfigure(0, weight=1)
                #frame_bottom.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
                tabla_viajes = TablaFrame(["No.", "Transportadora"," No. Viajes Realizados"], ["Nombre","CantViajesAsignados"], field_frame, Terminal.getTransportadoras(), [False,False,False,False,False,False], devolucionLlamado=devolucionLlamado)
                tabla_viajes.grid(row=0, column=0, sticky="ns")
            
            def verEstadisticasTransportadoras():
                
                def devolucionLlamado(select):
            
                    for i in range(0, len(Terminal.getTransportadoras())):
                        
                        if (tabla_viajes.combobox.get() == f"Opción {i+1}"):
                            
                            label = tk.Label(field_frame, text=f"La transportadora tiene una cantidad de estrellas de {Terminal.getTransportadoras()[i].getEstrellas()}", font= (("Segoe Script", 15, "bold")), background="Red")
                            
                            label.grid(row=3, column=0)
                            
                #frame_bottom= tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                #frame_bottom.grid_rowconfigure(0, weight=1)
                #frame_bottom.grid_columnconfigure(0, weight=1)
                #frame_bottom.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
                tabla_viajes = TablaFrame(["No.","Nombre", "Dinero", "Estrellas"], ["Nombre","Dinero","Estrellas"], field_frame, Terminal.getTransportadoras(), [False,False,False], devolucionLlamado=devolucionLlamado)
                tabla_viajes.grid(row=0, column=0, sticky="ns")
            
                
            
            
            
            
            
            
            
            
        
        def transportadorasQueHanCanceladoMonto():
            
            def devolucionLlamado(select):
            
                    for i in range(0, len(Terminal.getTransportadoras())):
                        
                        if (tabla_viajes.combobox.get() == f"Opción {i+1}"):
                            
                            label = tk.Label(field_frame, text=f"Si ve un 0(False), significa que no ha pagado, y 1 (True) es por que pagó", font= (("Segoe Script", 15, "bold")), background="Red")
                            
                            label.grid(row=3, column=0)
                            
                #frame_bottom= tk.Frame(ventanaPrincipal, bd = 3, bg = colors["background"])
                #frame_bottom.grid_rowconfigure(0, weight=1)
                #frame_bottom.grid_columnconfigure(0, weight=1)
                #frame_bottom.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
            tabla_viajes = TablaFrame(["No.","Nombre", "Estado de pago"], ["Nombre","EstadoPago"], field_frame, Terminal.getTransportadoras(), [False,False], devolucionLlamado=devolucionLlamado)
            tabla_viajes.grid(row=0, column=0, sticky="ns")
                
            
            


            
            

            

    def funcionalidad4():
        label_top_center.configure(text="Talleres y Mecanicos")
            

    def funcionalidad5():
        lista = estructura_frames("Gestion de conductores","Elija la transportadora a la cual le administrara los conductores")
        frame_bottom = lista[0]
        label_top_center = lista[1]
        label_center_center = lista[2]

        label_top_center.configure(text="🚍  Programación de Viajes  🚍")
        label_center_center.config(text = "Esta funcionalidad permite al usuario gestionar todo lo relacionado con la programación de viajes, la administración de reservas, la \n gestión de viajes ya creados, y la consulta y manejo del historial de viajes pasados. A través de una interfaz intuitiva, el usuario \n puede seleccionar el tipo de acción que desea realizar desde una lista de opciones y, en función de la selección, se le redirige a la \n operación específica correspondiente.")

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
            label_top_center.configure(text="📅 Programando un viaje... 📅")

            # LISTA DE DESTINOS DEL ENUMERADO
            valores_iniciales = list(Destino)
            valores_iniciales.remove(valores_iniciales[0])
            global ubicacionActual
            ubicacionActual = valores_iniciales[0]
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
                label_top_center.configure(text="🏢 Seleccionando Transportadora... 🏢")

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
                    label_top_center.configure(text="📅 Seleccionando Fecha del Viaje... 📅")
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
                        label_top_center.configure(text="⏰ Seleccionando Hora del Viaje... ⏰")
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
                            label_top_center.configure(text="🚍 Seleccionando Tipo Vehiculo... 🚍")
                            tiposDisponibles = transportadoraSelect.tiposVehiculosDisponible()
                            tiposPorNombre = []
                            for i in tiposDisponibles:
                                tiposPorNombre.append(i.name)
                            criterios = ["Tipo de Vehiculo"]

                            def devolucionLlamado(formularioDatosTipoVehiculo):
                                label_top_center.configure(text="🚗 Seleccionando tipo de Vehiculo... 🚗")
                                global tipoVehiculoSelect
                                seleccionNombre = formularioDatosTipoVehiculo[criterios[0]]  # Try, si las listas son vacias
                                for i in tiposDisponibles:
                                    if (i.name == seleccionNombre):
                                        tipoVehiculoSelect = i

                                # PASAR A SELECCIONAR EL CONDUCTOR
                                seleccionConductor()

                            field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=tiposPorNombre, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

                            # UBICACIÓN DEL FIELD FRAME
                            field_frame.grid(row=0, column=0, sticky="nsew")
                            frame_bottom.grid_rowconfigure(0, weight=1)
                            frame_bottom.grid_columnconfigure(0, weight=1)

                            def seleccionConductor():
                                label_top_center.configure(text="🤹 Tipo de selección del conductor... 🤹")
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
                                    try:

                                        if (conductores):
                                            for i in conductores:
                                                conductoresNombre.append(i.getNombre())
                                            criterios = ["Conductores Disponibles"]

                                            def devolucionLlamado(formularioDatosConductores):
                                                conductorNombre = formularioDatosConductores[criterios[0]]
                                                global conductorSelect
                                                for i in conductores:
                                                    if (conductorNombre == i.getNombre()):
                                                        conductorSelect = i

                                                        viaje = Terminal.programarViajeV(destinoSelect, tipoVehiculoSelect, fechaSelect, horaSelect, ubicacionActual) # LOGICA DE PROGRAMACIÓN DE VIAJE
                                                        if isinstance(viaje, Viaje):
                                                            mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                                                            valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                                                            nombreMetodos = ["Programar otro Viaje", "Terminar Proceso"]

                                                            resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del Viaje", objeto=viaje, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= programacionViaje, metodo2= funcionalidad5)

                                                            resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                                            frame_bottom.grid_rowconfigure(0, weight=1)
                                                            frame_bottom.grid_columnconfigure(0, weight=1)
                                                        else:
                                                            messagebox.showerror("Estado", "Programación en proceso")
                                                            funcionalidad5()

                                            field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=conductoresNombre, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                                            # UBICACIÓN DEL FIELD FRAME
                                            field_frame.grid(row=0, column=0, sticky="nsew")
                                            frame_bottom.grid_rowconfigure(0, weight=1)
                                            frame_bottom.grid_columnconfigure(0, weight=1)

                                        else:
                                            raise ValueError ("No hay conductores disponibles para esta fecha y tipo de vehículo.")
                                            seleccionTipoVehiculo()

                                    except Exception as a: # PARA SABER EL TIPO DE ERROR
                                        messagebox.showerror("Error", f"No hay conductores disponibles: {str(a)}")

                                def seleccionAutomática():
                                    global viaje
                                    viaje = Terminal.programarViajeV(destinoSelect, tipoVehiculoSelect, fechaSelect, horaSelect, Destino.MEDELLIN)

                                    if isinstance(viaje, Viaje):
                                        mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                                        valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                                        nombreMetodos = ["Programar otro Viaje", "Terminar Proceso"]

                                        resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del Viaje", objeto=viaje, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= programacionViaje, metodo2= funcionalidad5)

                                        resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                        frame_bottom.grid_rowconfigure(0, weight=1)
                                        frame_bottom.grid_columnconfigure(0, weight=1)
                                    else:
                                        messagebox.showerror("Estado", "Programación en proceso")
                                        funcionalidad5()
            
            field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=destinos, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

            # UBICACIÓN DEL FIELD FRAME
            field_frame.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)

        def administraciondeReservas():
            label_top_center.configure(text="📅 Administrando Reservas... 📅")
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
                    label_top_center.configure(text=f"🗈 Detalles del Viaje con ID = {viajeSelect.getId()}")

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Administrar otra Reserva", "Terminar Proceso"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles de la reserva", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= administraciondeReservas, metodo2= funcionalidad5)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def cancelarReserva():
                    print("Cancelar Viajes")
                    label_top_center.configure(text=f"🗈 Cancelar el Viaje con ID = {viajeSelect.getId()}")

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Regresar", "Cancelar"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles de la reserva", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= administraciondeReservas, metodo2= cancelar)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def cancelar():
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

                criterios = [f"Administrar Reserva con ID : {viajeSelect.getId()}"]
                valores_iniciales = ["Ver detalles Reserva", "Cancelar Reserva"]
                habilitado = [False, False]

                # Create the FieldFrame widget
                field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=valores_iniciales, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                # Agregar el nuevo frame debajo de la tabla
                field_frame.grid(row=0, column=0, sticky="nsew")
                frame_bottom.grid_rowconfigure(0, weight=1)
                frame_bottom.grid_columnconfigure(0, weight=1)
            
            titulo_criterios = ["Opción", "Id", "Llegada", "Fecha", "Hora", "Transportadora", "Vehiculo", "Conductor", "Distancia (Km)", "#Asientos"]
            atributos  = ["getId", "getLlegada", "getFecha", "getHora", "getTransportadora.getNombre", "getVehiculo.getTipo", "getConductor.getNombre", "getDistancia", "getAsientosDisponibles"]
            habilitado = [False, False, False, False, False, False, False, False, False, False]

            tabla = TablaFrameDinamica(tituloCriterios= titulo_criterios, atributos = atributos, parent = frame_bottom, lista = reservas, habilitado=habilitado, devolucionLlamado = devolucionLlamado)
            # Ubica la tabla en el centro del frame
            # UBICACIÓN DEL FIELD FRAME
            tabla.grid(row=0, column=0, sticky="nsew")
            frame_bottom.grid_rowconfigure(0, weight=1)
            frame_bottom.grid_columnconfigure(0, weight=1)


        def administracionViaje():
            label_top_center.configure(text="🏢 Administrando Viajes... 🏢")
            viajes = Terminal.getViajes()
            
            def devolucionLlamado(formularioViajes):
                partes = formularioViajes.split(":")
                indiceSeleccionado = int(partes[1].strip())
                global viajeSelect
                viajeSelect = viajes[indiceSeleccionado-1]
                print(f"indiceSeleccionado: {indiceSeleccionado} Viaje: {viajeSelect.getId()}")

                # CREAR UN NUEVO FORMULARIO.
                seleccionAdministrarViaje()


            titulo_criterios = ["Opción", "Id", "Llegada", "Fecha", "Hora", "Transportadora", "Vehiculo", "Conductor", "Distancia (Km)", "#Asientos"]
            atributos  = ["getId", "getLlegada", "getFecha", "getHora", "getTransportadora.getNombre", "getVehiculo.getTipo", "getConductor.getNombre", "getDistancia", "getAsientosDisponibles"]
            habilitado = [False, False, False, False, False, False, False, False, False, False]

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
                    label_top_center.configure(text=f"🗈 Detalles del Viaje con ID = {viajeSelect.getId()}")
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

                    label_top_center.configure(text=f"🗈 Cancelar el Viaje con ID = {viajeSelect.getId()}")

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
            label_top_center.configure(text="🗈 Administrando Historial... 🗈")
            viajesHistorial = Terminal.getHistorial()
            
            def devolucionLlamado(formularioViajes):
                partes = formularioViajes.split(":")
                indiceSeleccionado = int(partes[1].strip())
                global viajeSelect
                viajeSelect = viajesHistorial[indiceSeleccionado-1]
                print(f"indiceSeleccionado: {indiceSeleccionado} Viaje: {viajeSelect.getId()}")

                # CREAR UN NUEVO FORMULARIO.
                seleccionAdministrarViaje()


            titulo_criterios = ["Opción", "Id", "Llegada", "Fecha", "Hora", "Transportadora", "Vehiculo", "Conductor", "Distancia (Km)", "#Asientos"]
            atributos  = ["getId", "getLlegada", "getFecha", "getHora", "getTransportadora.getNombre", "getVehiculo.getTipo", "getConductor.getNombre", "getDistancia", "getAsientosDisponibles"]
            habilitado = [False, False, False, False, False, False, False, False, False, False]

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
                    label_top_center.configure(text=f"👪 Pasajeros del Viaje con ID = {viajeSelect.getId()}")
                    
                    pasajeros = viajeSelect.getPasajeros()
                    
                    titulo_criterios = ["N°", "Id", "Nombre", "Edad", "Tipo"]
                    atributos  = ["getId", "getNombre", "getEdad", "getTipoPasajero"]
                    habilitado = [False, False, False, False, False]

                    tabla = TablaFrameDinamica(tituloCriterios= titulo_criterios, atributos = atributos, parent = frame_bottom, lista = pasajeros, habilitado=habilitado, devolucionLlamado = regresar)
                    # UBICACIÓN DE LA TABLA
                    tabla.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def regresar():
                    funcionalidad5()

                def verInformación():
                    label_top_center.configure(text=f"🗈 Detalles del Viaje con ID = {viajeSelect.getId()}")

                    mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                    valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                    nombreMetodos = ["Administrar Otro Viaje", "Terminar Proceso"]

                    resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del viaje", objeto=viajeSelect, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos= nombreMetodos, metodo1=administracionHistorial , metodo2 = funcionalidad5)

                    resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                    frame_bottom.grid_rowconfigure(0, weight=1)
                    frame_bottom.grid_columnconfigure(0, weight=1)

                def reprogramar():
                    label_top_center.configure(text=f"🗈 Reprogramación del Viaje con ID = {viajeSelect.getId()}")
                    
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
                        label_top_center.configure(text="⏰ Seleccionando Hora del Viaje... ⏰")
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
                            label_top_center.configure(text="🚍 Seleccionando Tipo Vehiculo... 🚍")
                            transportadoraSelect = viajeSelect.getConductor().getTransportadora()
                            tiposDisponibles = transportadoraSelect.tiposVehiculosDisponible()
                            tiposPorNombre = []
                            for i in tiposDisponibles:
                                tiposPorNombre.append(i.name)
                            criterios = ["Tipo de Vehiculo"]

                            def devolucionLlamado(formularioDatosTipoVehiculo):
                                label_top_center.configure(text="🚗 Seleccionando tipo de Vehiculo... 🚗")
                                global tipoVehiculoSelect
                                seleccionNombre = formularioDatosTipoVehiculo[criterios[0]]  # Try, si las listas son vacias
                                for i in tiposDisponibles:
                                    if (i.name == seleccionNombre):
                                        tipoVehiculoSelect = i

                                # PASAR A SELECCIONAR EL CONDUCTOR
                                seleccionConductor()

                            field_frame = FieldFrame(parent=frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=tiposPorNombre, habilitado=habilitado, devolucionLlamado=devolucionLlamado)

                            # UBICACIÓN DEL FIELD FRAME
                            field_frame.grid(row=0, column=0, sticky="nsew")
                            frame_bottom.grid_rowconfigure(0, weight=1)
                            frame_bottom.grid_columnconfigure(0, weight=1)

                            def seleccionConductor():
                                label_top_center.configure(text="🤹 Tipo de selección del conductor... 🤹")
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
                                    try:

                                        if (conductores):
                                            for i in conductores:
                                                conductoresNombre.append(i.getNombre())
                                            criterios = ["Conductores Disponibles"]

                                            def devolucionLlamado(formularioDatosConductores):
                                                conductorNombre = formularioDatosConductores[criterios[0]]
                                                global conductorSelect
                                                for i in conductores:
                                                    if (conductorNombre == i.getNombre()):
                                                        conductorSelect = i
                                                        destinoSelect = viajeSelect.getLlegada()
                                                        viaje = Terminal.programarViajeV(destinoSelect, tipoVehiculoSelect, fechaSelect, horaSelect, ubicacionActual) # LOGICA DE PROGRAMACIÓN DE VIAJE
                                                        if isinstance(viaje, Viaje):
                                                            mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                                                            valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                                                            nombreMetodos = ["Reprogramar otro Viaje", "Terminar Proceso"]

                                                            resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del Viaje", objeto=viaje, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= administracionHistorial, metodo2= funcionalidad5)

                                                            resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                                            frame_bottom.grid_rowconfigure(0, weight=1)
                                                            frame_bottom.grid_columnconfigure(0, weight=1)
                                                        else:
                                                            messagebox.showerror("Estado", "Programación en proceso")
                                                            funcionalidad5()

                                            field_frame = FieldFrame(parent = frame_bottom, tituloCriterios="Opciones", criterios=criterios, tituloValores="Selección", valores=conductoresNombre, habilitado=habilitado, devolucionLlamado= devolucionLlamado)

                                            # UBICACIÓN DEL FIELD FRAME
                                            field_frame.grid(row=0, column=0, sticky="nsew")
                                            frame_bottom.grid_rowconfigure(0, weight=1)
                                            frame_bottom.grid_columnconfigure(0, weight=1)

                                        else:
                                            raise ValueError ("No hay conductores disponibles para esta fecha y tipo de vehículo.")
                                            seleccionTipoVehiculo()

                                    except Exception as a: # PARA SABER EL TIPO DE ERROR
                                        messagebox.showerror("Error", f"No hay conductores disponibles: {str(a)}")

                                def seleccionAutomática():
                                    destinoSelect = viajeSelect.getLlegada()
                                    global viaje
                                    viaje = Terminal.programarViajeV(destinoSelect, tipoVehiculoSelect, fechaSelect, horaSelect, Destino.MEDELLIN)

                                    if isinstance(viaje, Viaje):
                                        mostrar = ["ID", "Llegada", "Fecha", "Hora", "Vehiculo", "Conductor"] # ASIENTOS -- P1
                                        valores = ["getId", "getLlegada", "getFecha", "getHora", "getVehiculo.getModelo", "getConductor.getNombre"]
                                        nombreMetodos = ["Programar otro Viaje", "Terminar Proceso"]

                                        resultadosOperacion = ResultadosOperacion(tituloResultados="Detalles del Viaje", objeto=viaje, criterios=mostrar, valores=valores, parent= frame_bottom, nombreMetodos=nombreMetodos, metodo1= programacionViaje, metodo2= funcionalidad5)

                                        resultadosOperacion.grid(row=0, column=0, sticky="nsew")
                                        frame_bottom.grid_rowconfigure(0, weight=1)
                                        frame_bottom.grid_columnconfigure(0, weight=1)
                                    else:
                                        messagebox.showerror("Estado", "Programación en proceso")
                                        funcionalidad5()
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
    messagebox.showinfo("Información básica", "Nuestra aplicación permite la gestion de una Terminal de Transporte, permitiendo funcionalidades que optimizan las tareas y procesos realizados. Ademas ofrece un interfaz muy intuitiva de facil comprensión. ")

def mensajeAcerdade():
    messagebox.showinfo("Quienes somos", "Estudiantes Universidad Nacional \n \nSantiago Ochoa Cardona -- sochoaca@unal.edu.co \n Johan Ramirez Marin -- joramirezma@unal.edu.co \n Jaime Luis Osorio Gomez -- jaosoriogo@unal.edu.co \n Juan Camilo Marin Valencia -- jumarinv@unal.edu.co \n Jonathan David Osorio Restrepo -- joosoriore@unal.edu.co")

def salir(ventanaPrincipal, ventanaInicio):
    ventanaPrincipal.destroy()
    ventanaInicio.deiconify()

