import tkinter as tk
from tkinter import messagebox, ttk


def alertWarn(title, message):
    messagebox.showwarning(title, message)

def on_submit(formData):
    print("Form submitted with data:")
    for key, value in formData.items():
        print(f"{key}: {value}")

class FieldFrame(tk.Frame):
    """
    @arg tituloCriterios titulo para la columna "Criterio"
    @arg criterios array con los nombres de los criterios
    @arg tituloValores titulo para la columna "valor"
    @arg valores array con los valores iniciales; Si ‘None’, no hay valores iniciales
    @arg habilitado array con los campos no-editables por el usuario; Si ‘None’, todos son editables
    @arg parent contenedor principal donde se colocara el formulario
    @arg enviado es una funcion que se llamara cuando el formulario se envie
    """

    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado, parent, devolucionLlamado):
        import principal
        colors = principal.colors
        super().__init__(parent, bg=colors["background"], padx=10, pady=10)
        self.parent = parent
        self.criterios = criterios
        self.devolucionLlamado = devolucionLlamado
        self.valores = valores
        self.habilitado = habilitado
        self.datos = {}
        self.formularioDatos = {}

        # Configura la cuadrícula del formulario
        self.grid_rowconfigure(0, weight=1)  # Fila de títulos
        self.grid_rowconfigure(len(criterios)+1, weight=1)  # Fila de botones
        self.grid_columnconfigure(0, weight=1)  # Columna de criterios
        self.grid_columnconfigure(1, weight=1)  # Columna de valores

        # CREACIÓN LABELS TITULOS
        label_titulo_criterio = tk.Label(self, text=tituloCriterios, font=("Century", 17, "bold"), bg = colors["amarillo"], relief="ridge", bd= 3)
        label_titulo_valores = tk.Label(self, text=tituloValores, font=("Century", 17, "bold"), bg = colors["amarillo"], relief="ridge", bd= 3)

        # UBICACIÓN DE LOS TITULOS
        label_titulo_criterio.grid(row=0, column=0, padx=5, pady=5)
        label_titulo_valores.grid(row=0, column=1, padx=5, pady=5)

 # CREAR LA ENTRADA ENTRY O COMBOBOX PARA CADA CRITERIO
        for index, criterio in enumerate(criterios):
            elementoCriterio = tk.Label(self, text=criterio, bg = colors["background"], font=("Century", 14, "bold"), fg = colors["text"])
            elementoCriterio.grid(row=index+1, column=0, padx=5, pady=5)

            # Si el criterio es "Tipo de Programación", usar un Combobox
            if tituloCriterios == "Opciones":
                elementoInput = ttk.Combobox(self, font=("Century", 12), values=valores, state="readonly")
                elementoInput.current(0)  # Mostrar la primera opción por defecto
            else:
                # Para otros criterios, usar el Entry habitual
                elementoInput = tk.Entry(self, font=("Century", 12))

                if valores is not None and index < len(valores):
                    elementoInput.insert(0, valores[index])

                if habilitado is not None and index < len(habilitado) and not habilitado[index]:
                    elementoInput.configure(state=tk.DISABLED)

            elementoInput.grid(row=index+1, column=1, padx=5, pady=5)

            # ALMACENAR LOS DATOS Y SUS VALORES
            self.datos[criterio] = {
                "elementos": (elementoCriterio, elementoInput),
                "value": None
            }

        # BOTONES PARA ENVIAR O LIMPIAR
        botonEnviar = tk.Button(self, text="Enviar", font=("Century", 12), bg=colors["azul"], fg=colors["text"], relief="ridge", bd= 3, command=lambda: self.guardarDatos(devolucionLlamado))
        botonEnviar.grid(row=len(criterios)+1, column=1, padx=5, pady=5)

        if tituloCriterios != "Opciones":
            botonLimpiar = tk.Button(self, text="Limpiar", font=("Century", 12), bg=colors["naranja"], fg=colors["text"], relief="ridge", bd= 3, command=self.limpiarCasillas)
            botonLimpiar.grid(row=len(criterios)+1, column=0, padx=5, pady=5)
        

    # MÉTODOS DE LA CLASE

    def getValue(self, criterio):
        """
            Obtiene el valor de un criterio que se pasa como parametro. 
        """
        return self.datos[criterio]["value"]
    
    def guardarDatos(self, devolucionLlamado): # AGREGAR EL ERROR SUGERIDO
        camposVacios = []

        for criterio in self.criterios:
            value = self.datos[criterio]["elementos"][1].get()
            self.datos[criterio]["value"] = value
            self.formularioDatos[criterio] = value

            if (value == ""): # VERIFICAR SI HAY CAMPOS VACIOS 
                camposVacios.append(criterio) # ALMACENA PARA INFORMAR CUAL CRITERIO FALTA

            # Try
            if (devolucionLlamado != None):
                devolucionLlamado(self.formularioDatos)
        
        if (camposVacios):
            alertWarn("Entradas Vacias", f"Error, por favor completa todos los espacios. Faltan:{', '.join(camposVacios)}")
            return False
        
    
    def limpiarCasillas(self):
        """
            Limpia todos los datos del formulario
        """
        for criterio in self.criterios:
            self.datos[criterio]["elementos"][1].delete(0,"end")
