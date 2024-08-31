import math
# Faltan las importaciones...

class Viaje:
    _totalViajes = 1 # Atributo de clase
    # Constructor
    def __init__(self, terminal, horaSalida, fechaSalida, vehiculo, conductor, llegada, salida):
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
        self._transportadora = None # Verificar con el Vehiculo o el Destino
        self._dia = None
        self._distancia = None # Tiempo.calcularDia(fecha)
        self._duracion = None # Viaje.calcularDistancia(salida, llegada)
        self._horaLlegada = None # calcularHoraLlegada()
        self._fechaLlegada = None # calcularFechaLlegada()
        self._tarifa = None # calcularTarifa ()
        self._asientosDisponibles = None # Replantear la forma de calcularlos
        # Añadirlo a la lista de la Terminal, Terminal.getViajes.append() 
        # Asignar a la Transportadora --- Intentar que sea desde la transportadora que se asigne al conductor y vehiculo.
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

    def asignarPasajerosAViaje():
        pass

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
        fechaPartes = self.fecha.split("/")
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
        costoPorMinuto = 0
        total = 0
        
        # Establecer el costo por minuto según el tipo de vehículo
        tipoVehiculo = self._vehiculo.getTipo()
        
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
    
    def validacion(self): # Implementación depende del tiempo
        pass

    def programacionAutomatica(self): # Implementación depende del tiempo
        pass

    def ajusteFecha(self): # Implementación depende del tiempo
        pass

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
        capacidadVehiculo = self._vehiculo.getTipo().getCapacidad()
        asientosOcupados = len(self._pasajeros)
        total = capacidadVehiculo - asientosOcupados
        return total
    
    def isequals():
        pass

    def detallesViaje(): # Depronto sirve el metodo estado - - - Hacen lo mismo. 
        pass

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