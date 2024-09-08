# Importaciones para el Tiempo
import threading
import time

# Importaciones para el tiempo
#from src.gestorAplicacion.constantes.dia import Dia

class Tiempo:
    # Atributos de Clase
    # Salida - - Formatos
    salidaFecha = ""
    salidaHora = ""
    # Lista para la Serializacón
    tiempos = []

    # Inicializador
    def __init__(self, intervalo_ms=1000):
        # Atributos de la Instancia
        # Contadores
        self.minutos  = 0
        self.horas = 1
        self.dias = 1
        self.semana = 0
        self.meses = 1
        self.año = 2024
        self.Dia = None
        # Controladores
        self.intervalo = intervalo_ms / 1000  # Convertir milisegundos a segundos
        self.ejecutando = True  # Para controlar si el contador está activo - - Sirve para evitar que se la ejecución de dos o más Hilos.
        self.timer = None  # Almacenar el objeto timer
        self.ejecutarPeriodicamente()  # Iniciar la ejecución periódica
        print("Iniciado tiempo...")
        Tiempo.tiempos.append(self)# Añadir a la lista de Tiempos (Serializar)
    
    # Método donde se asignan las tareas.
    def tareas(self):
        self.calcularHora() # Calcula la hora
        self.calcularSalidaHora() # Define el formato de salida de la hora sirve para hacer validaciones.
        self.calcularSalidaFecha() # Define el formato de salida de la fecha sirve para hacer validaciones.
        #print(Tiempo.mostrarTiempo())
        print(f"{self.salidaFecha} ---- {self.salidaHora} --- {self.Dia}")
        # Llamar métodos creados
        # Necesario para reiniciar
        self.ejecutarPeriodicamente() # Reiniciar el temporizador
    
    # Metodo que realiza las tareas y define el intervalo de tiempo para las iteraciones. 
    def ejecutarPeriodicamente(self):
        if self.ejecutando:  # Verificar si el temporizador debe seguir ejecutándose
            self.timer = threading.Timer(self.intervalo, self.tareas) # Hilo no DEMONIO
            #self.timer = threading.Thread(target=self.tareas, daemon=True) # Hilo DEMONIO
            self.timer.start()

    # Se implementa para evitar que se creen dos Hilos simultaneamente
    def detener(self):
        if self.timer is not None:
            self.timer.cancel()  # Detener el temporizador
        self.ejecutando = False
        print("Tiempo detenido.")

    
    # Métodos Repetitivos
    """
        Actualiza la hora, los minutos, los días, los meses y los años de acuerdo con el paso del tiempo.
        Este método incrementa los minutos y realiza ajustes para las horas, días, meses y años con el paso del tiempo durante la ejecucion.
    """
    def calcularHora(self):
        self.minutos += 1
        #print(str(Tiempo.minutos) + " Min")
        if (self.minutos >= 60):
            self.horas += 1
            self.minutos = 0
            if (self.horas > 23):
                self.dias += 1
                self.horas = 0
            # Metodos funcionalidad de Gestion de Conductores
            if (self.dias % 7 == 0):
                self.semana += 1

            if (self.dias > 30):
                self.meses += 1
                self.dias = 1
                if (self.meses >= 12):
                    self.año += 1
                    self.meses  = 1

    def calcularDia(self):
        # Referencias
        baseDia = 1
        baseMes = 1
        baseAño = 2024

        # Dias transcurridos
        diasDesdeBase = 0

        # Conteo
        diasDesdeBase = 0  # Almacena el número de días totales desde la fecha base

        diasDesdeBase += (self.año - baseAño) * 360  # Suponiendo 30 días por mes y 12 meses por año

        diasDesdeBase += (self.meses - baseMes) * 30  # Añadir días por meses completos del año actual

        diasDesdeBase += (self.dias - baseDia)  # Añadir días del mes actual

        #diasSemana = list(Dia)  # Determinar el día de la semana
        #indiceDia = (diasDesdeBase + baseDia - 1) % 7
        #Tiempo.Dia = diasSemana[indiceDia] 

    def mostrarTiempo(self):
        """
        Imprime la fecha y hora actual en un formato completo para propósitos de prueba.
        
        Returns: (String) 
            * La fecha en formato "día/mes/año"
            * La hora en formato "hora:minutos"
            * El día de la semana correspondiente
        """
        tiempo = f"Fecha: {self.dias}/{self.meses}/{self.año} Hora: {self.horas}:{self.minutos} Hoy es: {self.Dia}"
        return tiempo
    
    def calcularSalidaHora(self):
        Tiempo.salidaHora = f"{self.horas}:{self.minutos}"

    def calcularSalidaFecha(self):
        Tiempo.salidaFecha = f"{self.dias}/{self.meses}/{self.año}"

    @staticmethod
    def getTiempos():
        return Tiempo.tiempos  # Retorna la lista tiempos

    @staticmethod
    def setTiempos(nuevos_tiempos):
        Tiempo.tiempos = nuevos_tiempos  # Setea la lista tiempos con nuevos datos
    

#PRUEBAS

#contador = Tiempo(intervalo_ms=1)  # Intervalo de 1000 ms (1 segundo)

#try:
#    while True:
#        pass  # Aquí puedes continuar con tu lógica principal del programa

#except KeyboardInterrupt:
#    # Manejo de interrupción del teclado para detener el temporizador
#    contador.detener()
#    print("Programa terminado por el usuario.")