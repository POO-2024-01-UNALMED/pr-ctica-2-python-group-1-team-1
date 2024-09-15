import tkinter as tk
from tkinter import ttk # SOLO PARA UTILIZAR EL COMBOBOX
import principal

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
    def __init__(self, tituloCriterios, atributos, parent, lista, habilitado=None):
        super().__init__(parent, bg=colors["background"], padx=10, pady=10)
        self.parent = parent
        self.atributos = atributos
        self.lista = lista
        self.habilitado = habilitado
        self.datos = {}

        # Crear los títulos de columna basados en los criterios
        for col, titulo in enumerate(tituloCriterios):
            label_titulo = tk.Label(self, text=titulo, font=("Century", 17, "bold"), bg=colors["amarillo"], relief="ridge", bd=3)
            label_titulo.grid(row=0, column=col, padx=5, pady=5)

        # Crear las filas de datos
        for i, obj in enumerate(self.lista):
            index_label = tk.Label(self, text=str(i+1), bg=colors["background"], font=("Century", 14, "bold"), fg=colors["text"])
            index_label.grid(row=i+1, column=0, padx=5, pady=5)

            for j, atributo in enumerate(self.atributos):
                metodo_get = getattr(obj, f"get{atributo}", None)
                if metodo_get is not None:
                    valor = metodo_get()
                else:
                    valor = ""

                if self.habilitado[j]:
                    entry = tk.Entry(self, font=("Century", 12))
                    entry.insert(0, valor)  # Valor inicial
                    entry.grid(row=i+1, column=j+1, padx=5, pady=5)
                    self.datos[(i, j)] = entry
                else:
                    label = tk.Label(self, text=valor, font=("Century", 12), bg=colors["background"], fg=colors["text"])
                    label.grid(row=i+1, column=j+1, padx=5, pady=5)

        # Crear un combobox para seleccionar un índice
        self.combobox = ttk.Combobox(self, values=[f"Opción {i+1}" for i in range(len(lista))], font=("Century", 12), state="readonly")
        self.combobox.grid(row=len(lista)+1, column=1, padx=10, pady=5)

        # Crear un botón para confirmar la selección
        botonSeleccionar = tk.Button(self, text="Seleccionar", font=("Century", 12), bg=colors["azul"], fg=colors["text"], relief="ridge", bd=3, command=self.seleccionarIndice)
        botonSeleccionar.grid(row=len(lista)+1, column=2, padx=5, pady=5, sticky="nsew")

    def seleccionarIndice(self):
        seleccion = self.combobox.get()
        if seleccion:
            indice_seleccionado = seleccion.split()[-1]
            print(f"Índice seleccionado: {indice_seleccionado}")
        else:
            print("Ningún índice seleccionado")

    def obtenerDatos(self):
        datos_actualizados = {}
        for (i, j), entry in self.datos.items():
            datos_actualizados[(i, j)] = entry.get()
        return datos_actualizados
