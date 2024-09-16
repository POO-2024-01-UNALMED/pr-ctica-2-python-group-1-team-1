import tkinter as tk
from tkinter import ttk, Canvas, Scrollbar# SOLO PARA UTILIZAR EL COMBOBOX
from enum import Enum

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

class TablaFrame(tk.Frame):
    def __init__(self, tituloCriterios, atributos, parent, lista, habilitado=None, devolucionLlamado=None):
        super().__init__(parent, bg=colors["background"], padx=10, pady=10)
        self.parent = parent
        self.atributos = atributos
        self.lista = lista
        self.habilitado = habilitado
        self.datos = {}
        self.devolucionLlamado = devolucionLlamado  # Callback

        # TITULOS DE LAS COLUMNAS CON BASE EN EL RANGO DE LA LISTA DE CRITERIOS
        for col, titulo in enumerate(tituloCriterios):
            label_titulo = tk.Label(self, text=titulo, font=("Century", 17, "bold"), bg=colors["amarillo"], relief="ridge", bd=3)
            label_titulo.grid(row=0, column=col, padx=5, pady=5)

        # FILAS QUE ALMACENARAN CADA DATO
        for i, obj in enumerate(self.lista):
            index_label = tk.Label(self, text=str(i+1), bg=colors["background"], font=("Century", 14, "bold"), fg=colors["text"])
            index_label.grid(row=i+1, column=0, padx=5, pady=5)

            for j, atributo in enumerate(self.atributos):
                metodo_get = getattr(obj, f"get{atributo}", None)
                print(metodo_get)
                if metodo_get is not None:
                    valor = metodo_get()
                else:
                    valor = "noReconoce"

                if self.habilitado[j]:
                    entry = tk.Entry(self, font=("Century", 12))
                    entry.insert(0, valor)  # DEFAULT
                    entry.grid(row=i+1, column=j+1, padx=5, pady=5)
                    self.datos[(i, j)] = entry
                else:
                    label = tk.Label(self, text=valor, font=("Century", 12), bg=colors["background"], fg=colors["text"])
                    label.grid(row=i+1, column=j+1, padx=5, pady=5)

        # COMBOBOX PARA SELECCIONAR EL INDICE
        self.combobox = ttk.Combobox(self, values=[f"Opción {i+1}" for i in range(len(lista))], font=("Century", 12), state="readonly")
        self.combobox.grid(row=len(lista)+1, column=1, padx=10, pady=5)

        # BOTÓN PARA CONFIRMAR LA SELECCIÓN
        botonSeleccionar = tk.Button(self, text="Seleccionar", font=("Century", 12), bg=colors["azul"], fg=colors["text"], relief="ridge", bd=3, command=self.seleccionarIndice)
        botonSeleccionar.grid(row=len(lista)+1, column=2, padx=5, pady=5, sticky="nsew")

    def seleccionarIndice(self):
        seleccion = self.combobox.get()
        if seleccion:
            indice_seleccionado = seleccion.split()[-1]
            print(f"Índice seleccionado: {indice_seleccionado}")

            # INVOCAR LA DEVOLUCIÓN DE LLAMADO
            if self.devolucionLlamado is not None:
                self.devolucionLlamado(f"Índice seleccionado: {indice_seleccionado}")
        else:
            print("Ningún índice seleccionado")

    def obtenerDatos(self): # EN CASO DE QUERER TODOS LOS DATOS
        datos_actualizados = {}
        for (i, j), entry in self.datos.items():
            datos_actualizados[(i, j)] = entry.get()
        
        
        if self.devolucionLlamado is not None:
            self.devolucionLlamado(datos_actualizados)

        return datos_actualizados

class TablaFrameDinamica(tk.Frame):
    def __init__(self, tituloCriterios, atributos, parent, lista, habilitado=None, devolucionLlamado=None):
        super().__init__(parent, bg=colors["background"], padx=10, pady=10)
        self.parent = parent
        self.atributos = atributos
        self.lista = lista
        self.habilitado = habilitado
        self.datos = {}
        self.devolucionLlamado = devolucionLlamado  # Callback

        # Crear un Canvas y un Scrollbar
        self.canvas = Canvas(self, bg=colors["background"])
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)


        # Crear un frame dentro del Canvas para contener la tabla
        self.frame = tk.Frame(self.canvas, bg=colors["background"], bd = 7)

        # TITULOS DE LAS COLUMNAS CON BASE EN EL RANGO DE LA LISTA DE CRITERIOS
        for col, titulo in enumerate(tituloCriterios):
            label_titulo = tk.Label(self.frame, text=titulo, font=("Century", 17, "bold"), bg=colors["amarillo"], relief="ridge", bd=3)
            label_titulo.grid(row=0, column=col, padx=5, pady=5)

        # FILAS QUE ALMACENARAN CADA DATO
        for i, obj in enumerate(self.lista):
            index_label = tk.Label(self.frame, text=str(i+1), bg=colors["background"], font=("Century", 14, "bold"), fg=colors["text"])
            index_label.grid(row=i+1, column=0, padx=5, pady=5)

            for j, atributo in enumerate(self.atributos):
                valor = self.obtener_valor_encadenado(obj, atributo)
                
                if valor == "noReconoce":
                    valor = ""

                if self.habilitado[j]:
                    entry = tk.Entry(self.frame, font=("Century", 12))
                    entry.insert(0, valor)  # DEFAULT
                    entry.grid(row=i+1, column=j+1, padx=5, pady=5)
                    self.datos[(i, j)] = entry
                else:
                    label = tk.Label(self.frame, text=valor, font=("Century", 12), bg=colors["background"], fg=colors["text"])
                    label.grid(row=i+1, column=j+1, padx=5, pady=5)

        # Agregar el frame al Canvas y el Canvas al self
        self.canvas.create_window(0, 0, window=self.frame, anchor='nw')
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Configurar el peso de las columnas para que se ajusten al tamaño de la ventana
        self.grid_columnconfigure(0, weight=1)

        # COMBOBOX PARA SELECCIONAR EL INDICE
        self.combobox = ttk.Combobox(self, values=[f"Opción {i+1}" for i in range(len(lista))], font=("Century", 12), state="readonly")
        self.combobox.grid(row=len(lista)+1, column=0, padx=10, pady=5)

        # BOTÓN PARA CONFIRMAR LA SELECCIÓN
        botonSeleccionar = tk.Button(self, text="Seleccionar", font=("Century", 12), bg=colors["azul"], fg=colors["text"], relief="ridge", bd=3, command=self.seleccionarIndice)
        botonSeleccionar.grid(row=len(lista)+1, column=1, padx=5, pady=5, sticky="nsew")

    def obtener_valor_encadenado(self, obj, atributo_encadenado):
        """
        Permite obtener el valor de un atributo encadenado (ej. 'getTransportadora.getNombre').
        Si el valor es un enumerado, se devuelve su nombre en lugar de la representación completa.
        """
        try:
            metodos = atributo_encadenado.split('.')
            valor = obj
            for metodo in metodos:
                if valor is not None:
                    valor = getattr(valor, metodo, None)
                    if callable(valor):
                        valor = valor()

                    # Verifica si el valor es un Enum y devuelve solo su nombre
                    if isinstance(valor, Enum):
                        return valor.name
                    elif valor is None:
                        return "noReconoce"
                else:
                    return "noReconoce"

            return valor
        except Exception as e:
            print(f"Error al obtener valor encadenado: {e}")
            return "noReconoce"

    def seleccionarIndice(self):
        seleccion = self.combobox.get()
        if seleccion:
            indice_seleccionado = seleccion.split()[-1]

            # INVOCAR LA DEVOLUCIÓN DE LLAMADO
            if self.devolucionLlamado is not None:
                self.devolucionLlamado(f"Índice seleccionado: {indice_seleccionado}")
        else:
            print("Ningún índice seleccionado")

    def obtenerDatos(self):  # EN CASO DE QUERER TODOS LOS DATOS
        datos_actualizados = {}
        for (i, j), entry in self.datos.items():
            datos_actualizados[(i, j)] = entry.get()

        if self.devolucionLlamado is not None:
            self.devolucionLlamado(datos_actualizados)

        return datos_actualizados
    
class ResultadosOperacion(tk.Frame):
    """
    Clase que representa un marco de resultados en la interfaz de usuario a partir de un objeto.

    Atributos:
        parent (tkinter.Tk): La ventana principal de la aplicación.
        nextFreeRow (int): La próxima fila libre en el marco.
        marco (tkinter.Frame): El marco que contiene los elementos de la interfaz de usuario.
    """

    def __init__(self, tituloResultados, objeto, criterios, valores, parent, nombreMetodos,metodo1, metodo2):
        """
        Inicializa un objeto de la clase ObjectResultFrame.

        Args:
            tituloResultados (str): El título de los resultados.
            objeto (object): El objeto del cual se van a mostrar los datos.
            criterios (list): Lista de nombres de los atributos del objeto a mostrar.
            valores (list): Lista de métodos (rutas) para obtener los valores del objeto.
            parent (tkinter.Tk): La ventana principal de la aplicación.
            colors (dict): Diccionario con los colores a utilizar en la interfaz.
        """
        super().__init__(parent)  # Llamada al constructor de tk.Frame
        self.parent = parent
        
        # Crea el marco donde van a estar los elementos
        marco = tk.Frame(parent, bg=colors["background"], relief="flat")
        marco.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        # Agregar el título de los resultados
        elementoTituloResultados = tk.Label(marco, text=tituloResultados, font=("Century", 15), bg=colors["amarillo"])
        elementoTituloResultados.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)

        index = 0
        # Por cada criterio, ejecutar el método correspondiente y mostrar el valor
        for index, (criterio, valor_ruta) in enumerate(zip(criterios, valores)):
            # Ejecutar el método correspondiente para obtener el valor
            valor = self.obtener_valor_encadenado(objeto, valor_ruta)

            # Crea la etiqueta para el criterio
            elementoKey = tk.Label(marco, text=criterio, font=("Century", 13), bg=colors["azul"])
            elementoKey.grid(row=index+1, column=0, padx=5, pady=5)
            marco.grid_rowconfigure(index+1, weight=1)
            marco.grid_columnconfigure(0, weight=1)

            # Crea la etiqueta para el valor
            elementoValue = tk.Label(marco, text=valor, font=("Century", 13), bg=colors["background"], fg=colors["text"])
            elementoValue.grid(row=index+1, column=1, padx=5, pady=5)
            marco.grid_rowconfigure(index+1, weight=1)
            marco.grid_columnconfigure(1, weight=1)
        
        self.nextFreeRow = index + 2
        # Agregar los botones para ejecutar los métodos
        boton1 = tk.Button(marco, text=nombreMetodos[0], command=metodo1, bg=colors["naranja"])
        boton1.grid(row=self.nextFreeRow, column=0, padx=5, pady=10, sticky="ew")
        
        boton2 = tk.Button(marco, text=nombreMetodos[1], command=metodo2, bg=colors["azul"])
        boton2.grid(row=self.nextFreeRow, column=1, padx=5, pady=10, sticky="ew")

        self.marco = marco
    
    def delete(self):
        """
        Destruye el marco de resultados.
        """
        self.marco.destroy()

    def obtener_valor_encadenado(self, obj, atributo_encadenado):
        """
        Permite obtener el valor de un atributo encadenado (ej. 'getTransportadora.getNombre').
        Si el valor es un enumerado, se devuelve su nombre en lugar de la representación completa.

        Args:
            obj (object): El objeto inicial sobre el cual se realizará la búsqueda del atributo.
            atributo_encadenado (str): La cadena de atributos o métodos encadenados a evaluar.

        Returns:
            str: El valor del atributo, o 'noReconoce' si no se puede obtener.
        """
        try:
            metodos = atributo_encadenado.split('.')
            valor = obj
            for metodo in metodos:
                if valor is not None:
                    valor = getattr(valor, metodo, None)
                    if callable(valor):
                        valor = valor()

                    # Verifica si el valor es un Enum y devuelve solo su nombre
                    if isinstance(valor, Enum):
                        return valor.name
                    elif valor is None:
                        return "noReconoce"
                else:
                    return "noReconoce"

            return valor
        except Exception as e:
            print(f"Error al obtener valor encadenado: {e}")
            return "noReconoce"
