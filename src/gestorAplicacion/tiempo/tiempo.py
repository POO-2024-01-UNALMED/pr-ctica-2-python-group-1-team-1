# Importaciones para el Tiempo
import threading
import time
# from gestorAplicacion.constantes.dia import Dia

class Tiempo:
    # Atributos de la clase
    minutos  = 0
    horas = 1
    dias = 1
    semana = 0
    meses = 1
    año = 2024
    Dia = None
    # Atributos de Salida - - Formatos
    salidaFecha = ""
    salidaHora = ""
    # Lista para la Serializacón
    tiempos = []

    # Inicializador
    def __init__(self, intervalo_ms=1000):
        self.intervalo = intervalo_ms / 1000  # Convertir milisegundos a segundos
        self.timer = None  # Almacenar el objeto timer
        self.ejecutando = False  # Para controlar si el contador está activo - - Sirve para evitar que se la ejecución de dos o más Hilos.
        Tiempo.tiempos.append(self)# Añadir a la lista de Tiempos
    
    
    def tareas(self): # Método donde se asignan las tareas.
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
            self.timer = threading.Timer(self.intervalo, self.tareas)
            self.timer.start()

    # Se implementa para evitar que se creen dos Hilos simultaneamente
    def iniciar(self):
        if not self.ejecutando:  # Solo iniciar si no está ya en ejecución
            self.ejecutando = True
            self.ejecutarPeriodicamente()  # Iniciar la ejecución periódica
            print("Iniciado tiempo...")

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
        Tiempo.minutos += 1
        #print(str(Tiempo.minutos) + " Min")
        if (Tiempo.minutos >= 60):
            Tiempo.horas += 1
            Tiempo.minutos = 0
            if (Tiempo.horas > 23):
                Tiempo.dias += 1
                Tiempo.horas = 0
            # Metodos funcionalidad de Gestion de Conductores
            if (Tiempo.dias % 7 == 0):
                Tiempo.semana += 1

            if (Tiempo.dias > 30):
                Tiempo.meses += 1
                Tiempo.dias = 1
                if (Tiempo.meses >= 12):
                    Tiempo.año += 1
                    Tiempo.meses  = 1

    @classmethod
    def calcularDia(cls):
        # Referencias
        baseDia = 1
        baseMes = 1
        baseAño = 2024

        # Dias transcurridos
        diasDesdeBase = 0

        # Conteo
        diasDesdeBase = 0  # Almacena el número de días totales desde la fecha base

        diasDesdeBase += (cls.año - baseAño) * 360  # Suponiendo 30 días por mes y 12 meses por año

        diasDesdeBase += (cls.meses - baseMes) * 30  # Añadir días por meses completos del año actual

        diasDesdeBase += (cls.dias - baseDia)  # Añadir días del mes actual

        #diasSemana = list(Dia)  # Determinar el día de la semana
        #indiceDia = (diasDesdeBase + baseDia.value - 1) % 7
        #Tiempo.Dia = diasSemana[indiceDia] 


    """
    Imprime la fecha y hora actual en un formato completo para propósitos de prueba.
	Este método muestra en la consola:
	    * La fecha en formato "día/mes/año"
	    * La hora en formato "hora:minutos"
	    * El día de la semana correspondiente
    """
    @classmethod
    def mostrarTiempo(cls):
        tiempo = f"Fecha: {cls.dias}/{cls.meses}/{cls.año} Hora: {cls.horas}:{cls.minutos} Hoy es: {cls.Dia}"
        return tiempo
    
    @classmethod
    def calcularSalidaHora(cls):
        cls.salidaHora = f"{cls.horas}:{cls.minutos}"

    @classmethod
    def calcularSalidaFecha(cls):
        cls.salidaFecha = f"{cls.dias}/{cls.meses}/{cls.año}"
    

#PRUEBAS

contador = Tiempo(intervalo_ms=1)  # Intervalo de 1000 ms (1 segundo)

# Iniciar el contador
contador.iniciar() # Se puede modificar para que inicie automaticamente cuando se instancia la clase Tiempo

# Dejar correr por 100 segundos antes de detenerlo (Pruebas)
time.sleep(100) # La idea es que se detenga unicamente cuando se termina el main.
contador.detener()