import tkinter as tk
from tkinter import messagebox
import principal

colors = principal.colors

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

    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado, parent, enviado):
        super().__init__(parent, bg=colors["background"], padx=10, pady=10)
        self.parent = parent
        self.criterios = criterios
        self.enviado = enviado
        self.valores = valores
        self.habilitado = habilitado
        self.datos = {}
        self.formularioDatos = {}

        # CREACIÓN LABELS TITULOS
        label_titulo_criterio = tk.Label(self, text=tituloCriterios, font=("Century", 17, "bold"), bg = colors["amarillo"], relief="ridge", bd= 3)
        label_titulo_valores = tk.Label(self, text=tituloValores, font=("Century", 17, "bold"), bg = colors["amarillo"], relief="ridge", bd= 3)

        # UBICACIÓN DE LOS TITULOS
        label_titulo_criterio.grid(row=0, column=0, padx=5, pady=5)
        label_titulo_valores.grid(row=0, column=1, padx=5, pady=5)

        # CREAR LA ENTRADA ENTRY PARA CADA CRITERIO
        for index, criterio in enumerate(criterios):
            elementoCriterio = tk.Label(self, text=criterio, bg = colors["background"], font=("Century", 14, "bold"), fg = colors["text"])
            elementoCriterio.grid(row=index+1, column=0, padx=5, pady=5)

            elementoInput = tk.Entry(self, font=("Century", 12)) # SE UTILIZA Entry
            elementoInput.grid(row=index+1, column=1, padx=5, pady=5)

            if valores is not None and index < len(valores):
                elementoInput.insert(0, valores[index])

            if habilitado is not None and index < len(habilitado) and not habilitado[index]:
                elementoInput.configure(state=tk.DISABLED)
            
            self.datos[criterio] = {
                "elementos": (elementoCriterio, elementoInput),
                "value": None
                }
            

        
        # BOTONES PARA ENVIAR O LIMPIAR
        botonEnviar = tk.Button(self, text="Enviar", font=("Century", 12), bg=colors["azul"], fg=colors["text"], relief="ridge", bd= 3, command=lambda: self.guardarDatos())
        botonEnviar.grid(row=len(criterios)+1, column=1, padx=5, pady=5)

        botonLimpiar = tk.Button(self, text="Limpiar", font=("Century", 12), bg=colors["naranja"], fg=colors["text"], relief="ridge", bd= 3, command=self.limpiarCasillas)
        botonLimpiar.grid(row=len(criterios)+1, column=0, padx=5, pady=5)
        

    # MÉTODOS DE LA CLASE
    def getValue(self, criterio):
        return self.datos[criterio]["value"]
    
    def guardarDatos(self):
        camposVacios = []

        for criterio in self.criterios:
            value = self.datos[criterio]["elementos"][1].get()
            self.datos[criterio]["value"] = value
            self.formularioDatos[criterio] = value

            if (value == ""): # VERIFICAR SI HAY CAMPOS VACIOS 
                camposVacios.append(criterio) # ALMACENA PARA INFORMAR CUAL CRITERIO FALTA
        
        if (camposVacios):
            alertWarn("Entradas Vacias", f"Error, por favor completa todos los espacios. Faltan:{', '.join(camposVacios)}")
            return False
        
        if self.enviado:
            self.enviado(self.formularioDatos)
        return True
    
    def limpiarCasillas(self):
        for criterio in self.criterios:
            self.datos[criterio]["elementos"][1].delete(0,"end")

# EJEMPLO DE USO --- CORRER ESTA CLASE PARA VER EL EJEMPLO

def main():
    root = tk.Tk()
    root.title("FieldFrame Example")

    # Define some example criteria and initial values
    criterios = ["Nombre", "Edad", "Email", "Destino", "Vehiculo"]
    valores_iniciales = ["Juan Pérez", "30", "juan.perez@example.com"]
    habilitado = [True, True, False]  # Email field is disabled

    # Create the FieldFrame widget
    field_frame = FieldFrame(
        parent=root,
        tituloCriterios="Criterio",
        criterios=criterios,
        tituloValores="Valor",
        valores=valores_iniciales,
        habilitado=habilitado,
        enviado=on_submit
    )

    field_frame.grid(row=0, column=0, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()