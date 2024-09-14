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
    """
    Crea una tabla que muestra una lista de objetos con atributos definidos por el usuario.
    
    @param tituloCriterios: Lista de títulos para cada columna (Nombres de los atributos).
    @param atributos: Lista de atributos de los objetos que se mostrarán (Nombre del apuntador a este atributo).
    @param habilitado: Lista booleana que indica si un campo es editable.
    @param parent: Frame padre donde se colocará la tabla.
    @param lista: Lista de objetos cuyos atributos serán mostrados en la tabla.
    """
    # INICIALIZADOR DE LA TABLA QUE MOSTRARA LA LISTA DE INSTANCIA DE UNA CLASE X

    def __init__(self, tituloCriterios, atributos, parent, lista, habilitado=None):

        super().__init__(parent, bg=colors["background"], padx=10, pady=10)
        self.parent = parent
        self.atributos = atributos
        self.lista = lista
        self.habilitado = habilitado
        self.datos = {}
        
        # CREAR LOS TITULOS DE LA COLUMNA BASADO EN LA LISTA DE CRITERIOS
        for col, titulo in enumerate(tituloCriterios):
            label_titulo = tk.Label(self, text=titulo, font=("Century", 17, "bold"), bg=colors["amarillo"], relief="ridge", bd=3)
            label_titulo.grid(row=0, column=col, padx=5, pady=5)

        # CREAR LA FILA SEGUN EL INDICE
        for i, obj in enumerate(self.lista):
            index_label = tk.Label(self, text=str(i+1), bg=colors["background"], font=("Century", 14, "bold"), fg=colors["text"])
            index_label.grid(row=i+1, column=0, padx=5, pady=5)

            # CREAR LA CELDA SEGÚN EL ATRIBUTO Y LA LISTA HABILITADO PARA SABER SI LA CASILLA ES EDITABLE 
            for j, atributo in enumerate(self.atributos):
                valor = getattr(obj, atributo, "")
                if self.habilitado[j]:
                    entry = tk.Entry(self, font=("Century", 12))
                    entry.insert(0, valor) # VALOR INICIAL
                    entry.grid(row=i+1, column=j+1, padx=5, pady=5)
                    self.datos[(i, j)] = entry
                else:
                    label = tk.Label(self, text=valor, font=("Century", 12), bg=colors["background"], fg=colors["text"])
                    label.grid(row=i+1, column=j+1, padx=5, pady=5)

        # CREAR UN COMBOBOX PARA SELECCIONAR UN INDICE
        self.combobox = ttk.Combobox(self, values=[f"Opción {i+1}, {lista[i].nombre}" for i in range(len(lista))], font=("Century", 12), state="readonly")
        self.combobox.grid(row=len(lista)+1, column=1, padx=10, pady=5)

        # CREAR UN BOTON PARA CONFIRMAR LA SELECCIÓN
        botonSeleccionar = tk.Button(self, text="Seleccionar", font=("Century", 12), bg=colors["azul"], fg=colors["text"], relief="ridge", bd=3, command=self.seleccionarIndice)
        botonSeleccionar.grid(row=len(lista)+1, column=2, padx=5, pady=5, sticky="nsew")

    def seleccionarIndice(self):
        """
        Muestra el índice seleccionado en el Combobox.
        """
        seleccion = self.combobox.get()
        if seleccion:
            indice_seleccionado = seleccion.split()[-1]
            print(f"Índice seleccionado: {indice_seleccionado}")
        else:
            print("Ningún índice seleccionado")

    def obtenerDatos(self): # SIRVE PARA CAPTURAR LOS DATOS DE MANERA GLOBAL
        """
        Retorna un diccionario con los valores actualizados de las celdas editables.
        """
        datos_actualizados = {}
        for (i, j), entry in self.datos.items():
            datos_actualizados[(i, j)] = entry.get()
        return datos_actualizados

# EJEMPLO DE USO

# Definir una clase de ejemplo para los objetos
class Persona:
    def __init__(self, nombre, edad, genero, colegio, pandemia):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.colegio = colegio
        self.pandemia = pandemia

# Crear una lista de objetos
personas = [
    Persona("Whyliam", 30, "Femenino", "STO", "IO"),
    Persona("Zantiago", 24, "Masculino", "STP", "FDP"),
    Persona("Juzman", 28, "Masculino", "SPM", "POO")
]

if __name__ == "__main__":
    root = tk.Tk()

    # Lista de títulos para las columnas
    titulos_columnas = ["ID", "Nombre", "Edad", "Género", "Colegio", "Pandemia"]

    # Instanciar TablaFrame con los atributos que queremos mostrar
    tablaFrame = TablaFrame(
        tituloCriterios=titulos_columnas,  # Títulos de las columnas
        atributos=["nombre", "edad", "genero", "colegio", "pandemia"],  # Atributos a mostrar
        parent=root,
        lista=personas,
        habilitado=[False, False, False, False, False]  # Ningún campo editable en este caso
    )

    tablaFrame.pack(padx=10, pady=10)

    root.mainloop()