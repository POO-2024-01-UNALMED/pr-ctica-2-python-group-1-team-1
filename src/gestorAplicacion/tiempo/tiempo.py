# Importaciones para el Tiempo
import threading
import time

# SOLUCIÓN IMPORTACIONES --------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#--------------------------------------------------------------------------------------

from gestorAplicacion.constantes.dia import Dia
from gestorAplicacion.administrativo.terminal import Terminal
#from gestorAplicacion.administrativo.viaje import Viaje


class Tiempo:
    # Atributos de Clase
    # Salida - - Formatos
    salidaFecha = ""
    salidaHora = ""
    dia = ""
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
        self.Dia = Dia.LUN.name
        # Controladores
        self.intervalo = intervalo_ms / 1000  # Convertir milisegundos a segundos
        self.ejecutando = True  # Para controlar si el contador está activo - - Sirve para evitar que se la ejecución de dos o más Hilos.
        self.timer = None  # Almacenar el objeto timer
        self.ejecutarPeriodicamente()  # Iniciar la ejecución periódica
        print("Iniciado tiempo...")
        Tiempo.tiempos.append(self)# Añadir a la lista de Tiempos (Serializar)
    
    # Método donde se asignan las tareas.
    def tareas(self):
        # MÉTODOS NECESARIOS PARA CALCULAR EL TIEMPO
        self.calcularHora() # Calcula la hora
        self.calcularDia() # Calcula el dia de la Semana
        self.calcularSalidaHora() # Define el formato de salida de la hora sirve para hacer validaciones.
        self.calcularSalidaFecha() # Define el formato de salida de la fecha sirve para hacer validaciones.
        self.modificarDia()
        #print(self.mostrarTiempo()) # Pruebas 
        
        # MÉTODOS PARA ADMINISTRAR LOS VIAJES
        self.comprobarViajes()
        self.comprobarViajesEnCurso()

        # MÉTODOS PARA ADMINISTRAR EL TALLER

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
    def modificarDia(self):
        Tiempo.dia = self.Dia

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

        diasSemana = list(Dia)  # Determinar el día de la semana
        indiceDia = (diasDesdeBase + baseDia-1) % 7
        self.Dia = diasSemana[indiceDia].name

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
    
    def comprobarViajes(self):
        """
        Revisa todos los viajes programados en la terminal y valida aquellos que coincidan con la fecha y hora actuales.
        La lógica es la siguiente:
    	 * 1. Se obtiene la lista de viajes desde la terminal.
    	 * 2. Si la lista de viajes no es nula, se itera sobre cada viaje.
    	 * 3. Para cada viaje, se compara la fecha y la hora del viaje con la fecha y hora actuales.
    	 * 4. Si el viaje coincide con la fecha y hora actuales, se llama al método `validacion()` del viaje.
        """
        viajesOriginal = Terminal.getViajes()
        viajes = viajesOriginal.copy()
        if (viajes is not None):
            for i in range(len(viajes)):
                viaje = viajes[i]
                if (viaje.getFecha() == Tiempo.salidaFecha):
                    if not (viaje.getPasajeros()):
                        viaje.asignarPasajerosAViaje(Terminal.getPasajeros())
                    if (viaje.getHora() == Tiempo.salidaHora):
                        print(f"Salio: {viaje.getId()}")
                        print(f"Lista Pasajeros: {viaje.getPasajeros()}")
                        viaje.validacion()

    def comprobarViajesEnCurso(self):
        """
        Revisa todos los viajes en curso en la terminal y ejecuta la programación automática para aquellos que llegan a la hora actual.
        La lógica es la siguiente:
    	 * 1. Se obtiene la lista de viajes en curso desde la terminal.
    	 * 2. Si la lista de viajes en curso no es nula, se itera sobre cada viaje.
    	 * 3. Para cada viaje, se compara la fecha y la hora de llegada del viaje con la fecha y hora actuales.
    	 * 4. Si el viaje coincide con la fecha y hora actuales, se llama al método `programacionAutomatica()` del viaje.
    	 */
        """
        viajes = Terminal.getViajesEnCurso()
        if (viajes is not None):
            for i in range(len(viajes)):
                viaje = viajes[i]
                if (viaje.getFecha() == Tiempo.salidaFecha):
                    if (viaje.getHora() == Tiempo.salidaHora):
                        print(f"llego: {viaje.getId()}")
                        print(Terminal.getHistorial())
                        viaje.programacionAutomatica()

    def mecanicosDisponibles (self):

        for i in Mecanico.getMecanicos():

            if (len(i.getVehiculosReparando()) == 0):

                i.setEstado (True)
            
            else:

                i.setEstado (False)

    def verificarVehiculos ():

        for taller in Taller.getListaTalleres():

            copiaVehiculos = taller.getVehiculosEnReparacion()

            for vehiculo in copiaVehiculos:

                if (vehiculo.getFechaHoraReparacion() <= Tiempo.getFechaHora()):

                    vehiculo.getMecanicoAsociado().repararVehiculo(vehiculo)
                
                #elif ((vehiculo.getFechaHoraReparacion() - Tiempo.getFechaHora()) >= 1000):

                    #vehiculo.getMecanicoAsociado().repararVehiculo(vehiculo)
    
    def verificarVehiculosVenta ():

        for taller in Taller.getListaTalleres():

            vehiculosEnVenta = taller.getVehiculosEnVenta()

            for vehiculo in vehiculosEnVenta:

                if (vehiculo.getFechaHoraReparacion() <= Tiempo.getFechaHora()):

                    vehiculo.getTransportadora().getTaller().venderVehiculo(vehiculo)
                    vehiculo.setReparando(False)
                
                #elif ((vehiculo.getFechaHoraReparacion() - Tiempo.getFechaHora()) >= 1000):

                    #vehiculo.getTransportadora().getTaller().venderVehiculo(vehiculo)
                    #vehiculo.setReparando(False)
                

    

    @classmethod
    def getFechaHora(cls):

        return((525600 * cls.año) + (43800 * cls.meses) + (10950 * cls.semana) + (1440 + cls.dias) + (60 * cls.horas))
    
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

    # MÉTODO PARA SERIALIZAR EL TIEMPO SIN EL ATRIBUTO QUE CONTIENE AL HILO 
    def __getstate__(self):
        # EXCLUIR EL TIMER 
        state = self.__dict__.copy()
        state['timer'] = None  # DARLE UN VALOR NONE
        return state

    # MÉTODO PARA DESERIALIZAR EL HILO Y PONERLO EN MARCHA
    def __setstate__(self, state):
        self.__dict__.update(state)
        # REINICIAR
        self.ejecutando = True
        self.ejecutarPeriodicamente()
    

#PRUEBAS

#contador = Tiempo(intervalo_ms=1)  # Intervalo de 1000 ms (1 segundo)

#try:
#    while True:
#        pass  # Aquí puedes continuar con tu lógica principal del programa

#except KeyboardInterrupt:
#    # Manejo de interrupción del teclado para detener el temporizador
#    contador.detener()
#    print("Programa terminado por el usuario.")