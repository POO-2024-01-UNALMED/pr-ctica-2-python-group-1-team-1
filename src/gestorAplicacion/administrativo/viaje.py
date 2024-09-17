import math
import random
"""# SOLUCIÓN IMPORTACIONES --------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath("src"))
#--------------------------------------------------------------------------------------"""


class Viaje:
    _totalViajes = 1 # Atributo de clase
    # Constructor
    def __init__(self, terminal, horaSalida, fechaSalida, vehiculo, conductor, llegada, salida):
        from src.gestorAplicacion.administrativo.terminal import Terminal
        from src.gestorAplicacion.tiempo.tiempo import Tiempo

        self._terminal = terminal
        self._id = Viaje._totalViajes
        self._horaSalida = horaSalida
        self._fechaSalida = fechaSalida
        self._vehiculo = vehiculo
        self._conductor = conductor
        self._llegada = llegada
        self._salida = salida
        self._estado = False # Estado por defecto (False); Significa: Sin salir
        self._pasajeros = []
        self._transportadora = conductor.getTransportadora() # Verificar con el Vehiculo o el Destino
        self._dia = Tiempo.dia
        self._distancia = self.calcularDistancia()  
        self._duracion = self.calcularDuracion()
        self._fechaLlegada = "" # Lo calcula el metodo inferior
        self._horaLlegada = self.calcularHoraLlegada()
        self._tarifa = self.calcularTarifa()
        self._asientosDisponibles = None # Replantear la forma de calcularlos
        Terminal.getViajes().append(self)
        self._conductor.getTransportadora().getViajesAsignados().append(self)
        self._conductor.getHorario().append(self)
        #self.asignarPasajerosAViaje(Terminal.getPasajeros())
        Viaje._totalViajes += 1
    
    # Metodos necesarios para inicializar
    """
    Calcula la distancia euclidiana entre dos puntos en un espacio n-dimensional.

    Returns:
        float: Distancia euclidiana entre los dos puntos.
    """
    def calcularDistancia(self):
        # Coordenadas de Salida (INICIO)
        x1 = self._salida.getEjeX()
        y1 = self._salida.getEjeY()
        # Coordenadas de Llegada (FIN)
        x2 = self._llegada.getEjeX()
        y2 = self._llegada.getEjeY()
        # Calcular la distancia
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return distancia

    def asignarPasajerosAViaje(self, pasajeros):
        """
        Agerega pasajeros al viaje aleatoriamente seleccionandolos de una lista de pasajeros
        recurrentes
        """
        dineroTotal = 0
        cantidadPasajeros = (self.getVehiculo().getTipo().getCapacidad() // 2) + 1
        
        for _ in range(cantidadPasajeros): # VERIFICAR LA LISTA DE PASAJEROS
            if not pasajeros:
                break
            
            pasajero = random.choice(pasajeros)
            self.getPasajeros().append(pasajero)
            pasajeros.remove(pasajero) # ELIMINARLO DE LA LISTA PARA NO REPETIR
            
            dineroTotal += self.getTarifa() * pasajero.getTipo().getDescuento()
        
        transportadora = self.getVehiculo().getTransportadora()
        transportadora.setDinero(transportadora.getDinero() + dineroTotal)

    """
    Calcula la duración estimada de un viaje en horas.
    Returns:
        float: Duración estimada del viaje en horas.
    """
    def calcularDuracion(self):
        distancia = self._distancia
        velocidad = self._vehiculo.getVelocidadPromedio()
        tiempo = (distancia / velocidad)

        if (self._conductor.getExperiencia() > 0.5):
            factorReduccion = 0.9
            tiempo *= factorReduccion
        
        return tiempo
    
    """
    Calcula la hora estimada de llegada de un viaje.
    Returns:
        salida: Hora estimada de llegada.
    """
    def calcularHoraLlegada(self):
        # Tiempo en horas y minutos
        tiempoHorasDuracion = self._duracion
        horaSalida = self._horaSalida
        
        # Dividir la hora de salida en horas y minutos
        partes = horaSalida.split(":")
        horasSalida = int(partes[0])
        minutosSalida = int(partes[1])
        
        # Dividir la fecha en día, mes y año
        fechaPartes = self._fechaSalida.split("/")
        dia = int(fechaPartes[0])
        mes = int(fechaPartes[1])
        año = int(fechaPartes[2])
        
        # Convertir la duración en horas enteras y minutos
        horasEnterasDuracion = int(tiempoHorasDuracion)
        minutosDuracion = int((tiempoHorasDuracion - horasEnterasDuracion) * 60)
        
        # Calcular el total de horas y minutos
        totalHoras = horasSalida + horasEnterasDuracion
        totalMinutos = minutosSalida + minutosDuracion
        
        # Manejar el exceso de minutos y horas
        totalHoras += totalMinutos // 60  # Sumar las horas extra de los minutos
        totalMinutos %= 60  # Mantener solo los minutos restantes

        # Ajustar el día si supera 24 horas
        dia += totalHoras // 24
        totalHoras %= 24

        # Ajustar el mes si supera 30 días
        mes += dia // 30
        dia %= 30

        # Ajustar el año si supera 12 meses
        año += mes // 12
        mes %= 12
        
        # Modificar la fecha de llegada
        fechaLlegada = f"{dia}/{mes}/{año}"
        self.setFechaLlegada(fechaLlegada)

        salida = f"{totalHoras}:{totalMinutos:02d}"
        
        return salida
    
    """
    Método para obtener la tarifa del viaje.
    Returns:
        total, dependiendo las condiciones establecidas: duración y tipo de vehiculo.
    """
    def calcularTarifa(self):
        from src.gestorAplicacion.administrativo.vehiculo import Vehiculo
        from src.gestorAplicacion.constantes.tipoVehiculo import TipoVehiculo
        from src.gestorAplicacion.administrativo.transportadora import Transportadora

        costoPorMinuto = 0
        total = 0
        
        # Establecer el costo por minuto según el tipo de vehículo
        tipoVehiculo = self._vehiculo.getTipo().name
        
        if tipoVehiculo == "TAXI":
            costoPorMinuto = 200
        elif tipoVehiculo == "VANS":
            costoPorMinuto = 170
        elif tipoVehiculo == "ESCALERA":
            costoPorMinuto = 66
        elif tipoVehiculo == "BUS":
            costoPorMinuto = 88
        else:
            return -1  # Valor de retorno inválido
        
        # Calcular la tarifa total
        estrellas = self._vehiculo.getTransportadora().getEstrellas()
        total = estrellas * 0.0005 * self._distancia # Considera la distancia
        
        total *= costoPorMinuto * (self._duracion * 60)
        
        return total
    
    """
    Valida el estado del viaje actual. Si el viaje no está en la lista de viajes en curso,
    lo añade a dicha lista, marca el viaje como activo, actualiza el estado del vehículo asociado,
    y lo elimina de la lista de todos los viajes. Retorna un mensaje indicando si el viaje está 
    ahora en curso o si ya estaba en curso.

    Returns:
        str: Mensaje indicando el estado del viaje.
    """
    def validacion(self):
        from src.gestorAplicacion.administrativo.terminal import Terminal
        from src.gestorAplicacion.administrativo.viaje import Viaje
        from src.gestorAplicacion.administrativo.vehiculo import Vehiculo
        from src.uiMain.principal import listViajes, listReservas, removeViaje, removeReserva
        
        viajes = Terminal.getViajesEnCurso()
        disponibles = listViajes()
        reservas = listReservas()

        if (self in viajes):
            return "El viaje ya esta en curso"
        else:
            viajes.append(self)
            self.setEstado(True)
            #self.getVehiculo().viaje(int(self.getDistancia())) #TODO : RECORDAR ARREGLAR ESTE ERROR
            removeViaje(self)
            if (self in reservas):
                removeReserva(self)
            return "El viaje está en Curso"
        

    """
    Maneja la programación automática del viaje, gestionando la continuidad del viaje o su cancelación. 
    Si el viaje está en curso, lo mueve al historial, lo elimina de la lista de viajes en curso y crea 
    un nuevo viaje con la fecha ajustada. Si el viaje no está en curso (lo que indica que fue cancelado 
    antes de salir), lo elimina de la lista de todos los viajes y también crea un nuevo viaje con la 
    fecha ajustada.
    """
    def programacionAutomatica(self):
        from src.gestorAplicacion.administrativo.terminal import Terminal
        from src.gestorAplicacion.usuarios.conductor import Conductor
        from src.gestorAplicacion.administrativo.viaje import Viaje
        from src.uiMain.principal import listViajesCurso, listViajesHistorial

        viaje = Terminal.getViajesEnCurso()
        self.getConductor().getHorario().remove(self)
        self.setEstado
        if (self in viaje):
            Terminal.getHistorial().append(self)
            viaje.remove(self)
        else:
            Terminal.getViajes().remove(self)

    def ajusteFecha(self, dias):
        """
        Ajusta la fecha de llegada sumando una cantidad de días.

        Args:
            dias (int): Número de días a sumar a la fecha de llegada.

        Returns:
            str: La nueva fecha en formato "dd/mm/yyyy".
        """
        fechaPartes = self.getFechaLlegada().split("/") # SEPARAR LA FECHA EN PARTES NUMÉRICAS
        dia = int(fechaPartes[0])
        mes = int(fechaPartes[1])
        año = int(fechaPartes[2])

        dia += dias
        if (dia > 30):
            dia = dia-30
            mes += 1
            if (mes > 12):
                mes = 1
                año +=1
        
        fechaLlegada = f"{dia}/{mes}/{año}"
        return fechaLlegada

    """ Genera un informe del estado actual del viaje, con detalles que varían dependiendo de si el viaje está en curso 
    o si aún no ha salido.
    Returns: 
        Una cadena de texto que describe el estado del viaje. Si el viaje está en curso, incluye detalles como
        la ubicación actual, pasajeros en curso. Si el viaje aún no ha salido, 
        muestra la información relevante comno los asientos disponibles.
    """
    def estado(self):
        enCurso = self.estado
        estado = ""
        
        if enCurso:
            estado = (
                "Estado del Viaje: En curso\n"
                "Detalles del Viaje:\n"
                f"Salida: {self._salida.name()}\n"
                f"Llegada: {self._llegada.name()}\n"
                f"Ubicación Actual: {self.ubicacion()}\n" 
                f"Fecha de salida: {self._fechaSalida}\n"
                f"Hora de salida: {self._horaSalida}\n"
                f"Vehículo: {self._vehiculo.getModelo()}\n"
                f"Placa: {self._vehiculo.getPlaca()}\n"
                f"Conductor: {self._conductor.getNombre()}\n"
                f"Experiencia: {self._conductor.getExperiencia()}\n"
                f"Pasajeros en Curso: {self._vehiculo.getCapacidad() - self.verificarAsientos()}\n"
            )
        else:
            estado = (
                "Estado del Viaje: Sin Salir\n"
                "Detalles del Viaje:\n"
                f"Salida: {self._salida.name()}\n"
                f"Llegada: {self._llegada.name()}\n"
                f"Fecha de Salida: {self._fechaSalida}\n"
                f"Hora de Salida: {self._horaSalida}\n"
                f"Vehículo: {self._vehiculo.getModelo()}\n"
                f"Placa: {self._vehiculo.getPlaca()}\n"
                f"Conductor: {self._conductor.getNombre()}\n"
                f"Experiencia: {self._conductor.getExperiencia()}\n"
                f"Asientos disponibles: {self.getAsientosDisponibles()}\n"
            )
        
        return estado
    
    def ubicacion(): # Implementación en evaluación. jajaja
        pass

    """
    Verifica el número de asientos disponibles en el vehículo asociado a este viaje.
    Este método calcula la cantidad de asientos disponibles restando el número de pasajeros actuales
    de la capacidad total del vehículo asignado a este viaje.
    Returns:
        total, El número de asientos disponibles en el vehículo. Un valor positivo indica la cantidad de asientos libres,
        mientras que un valor de cero o negativo podría indicar que no hay asientos disponibles o que hay más pasajeros
        de los que puede acomodar el vehículo.
    """
    def verificarAsientos(self):
        from src.gestorAplicacion.administrativo.vehiculo import Vehiculo
        from src.gestorAplicacion.constantes.tipoVehiculo import TipoVehiculo

        capacidadVehiculo = self._vehiculo.getTipo().getCapacidad()
        asientosOcupados = len(self._pasajeros)
        total = capacidadVehiculo - asientosOcupados
        return total
    
    def isequals():
        pass

    def detallesViaje(self):
        """Metodo para mostrar los detalles del viaje de manera superficial"""
        return "Fecha del viaje: " + str(self.getFecha()) + " Destino: " + str(self.getLlegada) + " ID: " + str(self.getId())

    # Métodos Get y Set
    # Establece o modifica la Terminal del viaje.
    def setTerminal(self, terminal):
        self._terminal = terminal

    # Obtiene la Terminal del viaje.
    def getTerminal(self):
        return self._terminal

    # Establece o modifica el identificador del viaje.
    def setId(self, id):
        self._id = id

    # Obtiene el identificador del viaje.
    def getId(self):
        return self._id

    # Establece o modifica la tarifa del viaje.
    def setTarifa(self, tarifa):
        self._tarifa = tarifa

    # Obtiene la tarifa del viaje.
    def getTarifa(self):
        return self._tarifa

    # Establece o modifica la duración del viaje en minutos.
    def setDuracion(self, duracion):
        self._duracion = duracion

    # Obtiene la duración del viaje en minutos.
    def getDuracion(self):
        return self._duracion

    # Establece o modifica el número total de viajes realizados.
    def setTotalViajes(self, totalViajes):
        Viaje._totalViajes = totalViajes

    # Obtiene el número total de viajes realizados.
    def getTotalViajes(self):
        return Viaje._totalViajes

    # Establece o modifica la hora de inicio del viaje.
    def setHora(self, hora):
        self._horaSalida = hora

    # Obtiene la hora de inicio del viaje.
    def getHora(self):
        return self._horaSalida

    # Establece o modifica la hora de llegada del viaje.
    def setHoraLlegada(self, horaLlegada):
        self._horaLlegada = horaLlegada

    # Obtiene la hora de llegada del viaje.
    def getHoraLlegada(self):
        return self._horaLlegada

    # Establece o modifica la fecha de inicio del viaje.
    def setFecha(self, fecha):
        self._fechaSalida = fecha

    # Obtiene la fecha de inicio del viaje.
    def getFecha(self):
        return self._fechaSalida

    # Establece o modifica la fecha de llegada del viaje.
    def setFechaLlegada(self, fechaLlegada):
        self._fechaLlegada = fechaLlegada

    # Obtiene la fecha de llegada del viaje.
    def getFechaLlegada(self):
        return self._fechaLlegada

    # Establece o modifica la lista de pasajeros del viaje.
    def setPasajeros(self, pasajeros):
        self._pasajeros = pasajeros

    # Obtiene la lista de pasajeros del viaje.
    def getPasajeros(self):
        return self._pasajeros

    # Establece o modifica el vehículo utilizado en el viaje.
    def setVehiculo(self, vehiculo):
        self._vehiculo = vehiculo

    # Obtiene el vehículo utilizado en el viaje.
    def getVehiculo(self):
        return self._vehiculo

    # Establece o modifica el conductor del vehículo en el viaje.
    def setConductor(self, conductor):
        self._conductor = conductor

    # Obtiene el conductor del vehículo en el viaje.
    def getConductor(self):
        return self._conductor

    # Obtiene el destino final del viaje.
    def getLlegada(self):
        return self._llegada

    # Establece o modifica la llegada del viaje.
    def setLlegada(self, llegada):
        self._llegada = llegada

    # Establece o modifica el dia de salida del viaje.
    def setDia(self, dia):
        self._dia = dia

    # Obtiene el día en que se realiza el viaje.
    def getDia(self):
        return self._dia

    # Establece o modifica el destino de salida del viaje.
    def setSalida(self, salida):
        self._salida = salida

    # Obtiene el destino actual del viaje.
    def getSalida(self):
        return self._salida

    # Establece o modifica el estado utilizado en el viaje.
    def setEstado(self, estado):
        self._estado = estado

    # Obtiene el estado del viaje. (false "Estacionado" y True "Viaje en curso")
    def getEstado(self):
        return self._estado

    # Establece o modifica la distancia del viaje.
    def setDistancia(self, distancia):
        self._distancia = distancia

    # Obtiene la distancia en Km del viaje.
    def getDistancia(self):
        return self._distancia

    # Obtiene el número de asientos disponibles en el viaje.
    def getAsientosDisponibles(self):
        return self._asientosDisponibles

    # Establece o modifica el número de asientos disponibles en el viaje.
    def setAsientosDisponibles(self, asientosDisponibles):
        self._asientosDisponibles = asientosDisponibles

    # Establece o modifica la transportadora asociada al viaje.
    def setTransportadora(self, transportadora):
        self._transportadora = transportadora

    # Obtiene la transportadora asociada al viaje.
    def getTransportadora(self):
        return self._transportadora