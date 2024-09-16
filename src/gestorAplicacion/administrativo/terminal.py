# SOLUCIÓN IMPORTACIONES --------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath("src"))
#--------------------------------------------------------------------------------------

# Importaciones:
from multimethod import multimethod
from gestorAplicacion.constantes.tipoVehiculo import TipoVehiculo
from gestorAplicacion.constantes.destino import Destino
from gestorAplicacion.usuarios.conductor import Conductor
"""from gestorAplicacion.administrativo.transportadora import Transportadora
from gestorAplicacion.administrativo.vehiculo import Vehiculo
from gestorAplicacion.administrativo.viaje import Viaje
from gestorAplicacion.usuarios.conductor import Conductor"""

class Terminal:
    # Atributos de clase
    cantidadSedes = 0
    transportadoras  = []
    reservas = []
    viajes = []
    viajesEnCurso = []
    historial = []
    facturas = []
    pasajeros = []
    listaTerminales = [] # Para serializar
    
    # Inicializador
    def __init__(self, nombre, dinero, capacidadVehiculos, transportadoras, viajes, viajesEnCurso, destinos, comision, ubicacion, administrador):
        self._nombre = nombre
        self._dinero = dinero
        self._capacidadVehiculos = capacidadVehiculos
        Terminal.transportadoras = transportadoras
        Terminal.viajes = viajes
        Terminal.viajesEnCurso = viajesEnCurso
        Terminal._reservas = []
        Terminal._historial = []
        self._destinos = destinos # Propios de cada terminal
        self.vehiculosTerminal = [] # Propios de cada terminal
        self.COMISION = comision
        self._ubicacion = ubicacion
        self._administrador = administrador
        Terminal.cantidadSedes += 1

    # Sobrecarga de Inicializadores (Sin administrador)
    def __init__(self, nombre, dinero, capacidadVehiculos, transportadoras, viajes, viajesEnCurso, destinos, comision, ubicacion):
        self._nombre = nombre
        self._dinero = dinero
        self._capacidadVehiculos = capacidadVehiculos
        Terminal.transportadoras = transportadoras
        Terminal.viajes = viajes
        Terminal.viajesEnCurso = viajesEnCurso
        Terminal._reservas = []
        Terminal._historial = []
        self._destinos = destinos # Propios de cada terminal
        self.vehiculosTerminal = [] # Propios de cada terminal
        self.COMISION= comision
        self._ubicacion = ubicacion
        Terminal.cantidadSedes += 1

    def transportadorasViajeDisponible():
        pass

    def obtenerTransportadorasUnicas():
        pass

    @staticmethod
    def viajesDestino(destino):
        """Encontrar viajes disponibles con un destino en específico
        la idea es que solo en este se verifique si esta en la terminal 'getEstado()'"""
        from gestorAplicacion.administrativo.viaje import Viaje

        viajesDisponibles = []

        for viaje in Terminal.getViajes(): 
            if viaje.getLlegada()==destino and not viaje.getEstado():
                viajesDisponibles.append(viaje)     
            
        return viajesDisponibles
    
    @classmethod
    def transportadorasViajeDisponible(cls, destino):
        """Encuentra las transportadoras de la terminal que ofrecen un destino que se recibe como parametro.
        Returns:
            Lista de las transportadoras a dicho destino.         
        """
        from gestorAplicacion.administrativo.transportadora import Transportadora
        
        transportadorasPorDestino = []
        for transportadora in cls.getTransportadoras():
            if (destino in transportadora.getDestinos()):
                transportadorasPorDestino.append(transportadora)
        return transportadorasPorDestino
            
    def transportadorasViaje(viajes):
        """Encuentra las transportadoras de la lista de viajes sin repetir.
        Return:
            Lista de las transportadoras a dicho destino.         
        """
        from gestorAplicacion.administrativo.transportadora import Transportadora
        
        transportadoras = []
        for viaje in viajes:
            if (viaje.getVehiculo().getTransportadora() not in transportadoras):
                transportadoras.append(viaje.getVehiculo().getTransportadora())
        return transportadoras

    @staticmethod
    def viajesDisponibles(): # Para que se usa???
        nuevaLista = []
        return nuevaLista
    
    @staticmethod
    def masRapido(viajes):
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        viajeMasRapido = None

        for viaje in viajes:
            if viaje.getVehiculo().getTipo()==TipoVehiculo.VANS or viaje.getVehiculo().getTipo()==TipoVehiculo.TAXI:
                if viaje is None or viaje.getDuracion() < viajeMasRapido.getDuracion():
                    viajeMasRapido = viaje

        return viajeMasRapido
            
    def obtenerViajeMasProximo():
        pass

    @staticmethod
    def masEconomico(viajes):
        """Este método permite encontrar el viaje mas barato en una lista de viajes previamente seleccionados"""
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        viajeMasBarato = None

        for viaje in viajes:
            if viaje.getVehiculo().getTipo()==TipoVehiculo.BUS:
                if viaje is None or viaje.getTarifa() < viajeMasBarato.getTarifa():
                    viajeMasBarato = viaje
        
        return viajeMasBarato

    # Sobrecarga
    @multimethod
    def viajesParaRegularesYDiscapacitados(cantidad : int, viajes : list):
        """Método para filtrar viajes por cantidad de asientos solicitados"""
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.constantes.tipoPasajero import TipoPasajero

        viajesDisponibles = []

        for viaje in viajes:
            if viaje == None:
                continue
            if viaje.verificarAsientos()>=cantidad:
                viajesDisponibles.append(viaje)  

        return viajesDisponibles
    
    @multimethod
    def viajesParaRegularesYDiscapacitados(tipoVehiculo : TipoVehiculo, viajes : list):
        """Método para filtrar viajes por el tipo de vehiculo"""
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        viajesDisponibles = []

        for viaje in viajes:
            if viaje is None:
                continue
            if viaje.getVehiculo().getTipo()==tipoVehiculo:
                viajesDisponibles.append(viaje)  

        return viajesDisponibles
            
    # Sobrecarga
    @multimethod
    def viajesParaVips(cantidad : int, viajes : list):
        """Método para filtrar viajes por cantidad de asientos solicitados"""
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        viajesDisponibles = []

        for viaje in viajes:
            if viaje == None:
                continue
            if viaje.verificarAsientos()>=cantidad and viaje.getVehiculo().getTipo() is not TipoVehiculo.ESCALERA:
                viajesDisponibles.append(viaje)  

        return viajesDisponibles
    
    @multimethod
    def viajesParaVips(tipoVehiculo : TipoVehiculo, viajes : list):
        """Método para filtrar viajes por el tipo de vehiculo"""
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        viajesDisponibles = []

        for viaje in viajes:
            if viaje is None:
                continue
            if viaje.getVehiculo().getTipo()==tipoVehiculo:
                viajesDisponibles.append(viaje)  

        return viajesDisponibles

    # Sobrecarga
    @multimethod
    def viajesParaEstudiantes(viajes : list):
        from gestorAplicacion.administrativo.viaje import Viaje

        viajesDisponibles = []

        for viaje in viajes:
            if viaje.verificarAsientos()>=1 and viaje.getVehiculo().getTipo().name != 'TAXI':
                viajesDisponibles.append(viaje)

        return viajesDisponibles

    @multimethod
    def viajesParaEstudiantes(viajes: list, tipoVehiculo: str):
        """Método para filtrar viajes por el tipo de vehiculo"""
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        viajesDisponibles = []

        for viaje in viajes:
            if viaje.getVehiculo().getTipo().getCapacidad()>=1:
                if viaje.getVehiculo().getTipo().name == tipoVehiculo:
                    viajesDisponibles.append(viaje)

        return viajesDisponibles
        
    # Programación por Vehiculo ()
    @multimethod
    #@classmethod
    def programarViaje(cls, llegada: Destino, tipoVehiculo: TipoVehiculo, fecha: str, hora: str, salida: Destino):
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.transportadora import Transportadora
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        for transportadora in cls.getTransportadoras():
            if llegada in transportadora.getDestinos():
                for vehiculo in transportadora.getVehiculos():
                    if vehiculo.getTipo() == tipoVehiculo and vehiculo.disponibilidad():
                        conductorSeleccionado = None
                        for conductor in vehiculo.getConductores():
                            if conductor.getEstadoLicencia():
                                conductorSeleccionado = conductor
                                break
                        if conductorSeleccionado:
                            nuevoViaje = Viaje(transportadora.getTerminal(), hora, fecha, vehiculo, conductorSeleccionado, llegada, salida)
                            return nuevoViaje
                        else:
                            return None
                return None
        return None

    # Programación por Conductor ()
    @multimethod
    #@classmethod
    def programarViaje(cls, llegada: Destino, conductor = Conductor, tipoVehiculo = TipoVehiculo, fecha = str, hora = str, salida = Destino):
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.transportadora import Transportadora
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        for transportadora in cls.getTransportadoras:
            if llegada in transportadora.getDestinos():
                for vehiculo in transportadora.getVehiculos():
                    if vehiculo.getTipo() == tipoVehiculo and vehiculo.disponibilidad():
                        if (conductor in transportadora.conductoresDisponibles(fecha, tipoVehiculo)):
                            if (conductor.getEstadoLicencia()):
                                nuevoViaje = Viaje(transportadora.getTerminal(), hora, fecha, vehiculo, conductor, llegada, salida)
                                return nuevoViaje
                            else:
                                return None # SE PUEDEN AGREGAR RIPO STRINGS PARA EL TIPO DE ERROR
                        else: 
                            return None
                    else:
                        return None
            else:
                return None
        else:
            return None

    def cancelarViajeAbsoluto(viaje):
        """
        Cancela un viaje de forma absoluta, lo que implica eliminar el viaje de las listas de reservas y de viajes,
        así como reembolsar a todos los pasajeros que estaban en el viaje.

        Returns:
            String: Un mensaje que indica el resultado de la operación, en este caso, siempre retorna "Viaje cancelado".
        """
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.usuarios.pasajero import Pasajero

        cadena = "El viaje no tenía pasajeros" # Valor por default
        pasajeros = viaje.getPasajeros()
        
        if (pasajeros):
            for pasajero in pasajeros:
                pasajero.aumentarDinero(int(viaje.getTarifa()))
            cadena = "Viaje cancelado"
        
        reservas = Terminal.getReservas()
        if (viaje in reservas):
            reservas.remove(viaje)
        
        viajes = Terminal.getViajes()
        if (viaje in viajes):
            viajes.remove(viaje)
        
        return cadena

    def cancelarViaje(viaje):
        """
        Método de cancelación de viajes que verifica si hay viajes con caracteristicas similares donde se puedan reubicar los pasajeros del viaje a cancelar
        en caso afirmativo los reubica, de lo contrario reembolsa el dinero a los pasajeros involucrados.
        """
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.usuarios.pasajero import Pasajero

        pasajeros = viaje.getPasajeros()
        reubicados = False

        for v in Terminal.viajes:
            if v != viaje and v.getSalida() == viaje.getSalida() and v.getLlegada() == viaje.getLlegada() and v.getAsientosDisponibles() >= len(pasajeros):
                v.setTarifa(viaje.getTarifa())
                v.getPasajeros().extend(pasajeros)
                viaje.programacionAutomatica()
                reubicados = True
                break

        if reubicados:
            return "Los pasajeros han sido reubicados en otro viaje."
        else:
            for p in pasajeros:
                p.aumentarDinero(int(viaje.getTarifa()))
            viaje.programacionAutomatica()
            return "Los pasajeros han sido reembolsados."

    def consultarCapacidad(viaje):
        """
        Método para saber si hay asientos disponibles en un viaje
        """
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        capacidadVehiculo = viaje.getVehiculo().getTipo().getCapacidad()
        asientosOcupados = len(viaje.getPasajeros())
        #disponibles = capacidad_vehiculo - asientos_ocupados 

        if (capacidadVehiculo >= asientosOcupados):
            return True
        else:
            return False
        
    @classmethod
    def denegarReserva(cls,viaje):
        """
        Deniega una reserva de un viaje y maneja la reubicación de los pasajeros o el reembolso, según sea necesario.
        Returns: (String)
            Un mensaje que indica el resultado de la operación:
                "Los pasajeros han sido reubicados en otro viaje." si se ha encontrado un viaje adecuado para reubicar a los pasajeros.
                "Los pasajeros han sido reembolsados." si no se ha encontrado un viaje adecuado y se ha procedido a reembolsar a los pasajeros.
        """
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.usuarios.pasajero import Pasajero
        from gestorAplicacion.administrativo.vehiculo import Vehiculo

        pasajeros = viaje.getPasajeros()
        reubicados = False

        # Buscar un nuevo viaje con los mismos detalles de salida y llegada
        nuevoViaje = None
        nuevoViaje = cls.programarViaje(viaje.getSalida(), viaje.getVehiculo().getTipo(), viaje.getFecha(), viaje.getHora(), viaje.getLlegada())

        if (nuevoViaje != None):
            nuevoViaje.setTarifa(viaje.getTarifa())
            nuevoViaje.getPasajeros().extend(pasajeros)
            reubicados = True

        if (reubicados):
            cls.getReservas().append(nuevoViaje)
            cls.getReservas().remove(viaje)
            viaje.programacionAutomatica()
            return "Los pasajeros han sido reubicados en otro viaje."
        else:
            for pasajero in pasajeros:
                pasajero.aumentarDinero(int(viaje.getTarifa()))
            cls.getReservas().remove(viaje)
            cls.getViajes().remove(viaje)
            return "Los pasajeros han sido reembolsados; no se encontró disponibilidad."

    def calcularGanancias():
        pass

    def agregarVehiculoTerminal(self, vehiculo):
        "Agrega el vehiculo a la terminal y actualiza la capacidad de los mismos"
        self.vehiculosTerminal.append(vehiculo)
        self._capacidadVehiculos -= 1

    def removerVehiculoTerminal(self, vehiculo):
        "Remueve el vehiculo de la terminal y actualiza la capacidad de los mismos"
        self.vehiculosTerminal.remove(vehiculo)
        self._capacidadVehiculos +=1

    @classmethod
    def fechasDisponibles(cls,salidaFecha):
        """
        Genera una lista de fechas disponibles a partir de la fecha actual.
        Returns: (ArrayList)
            La lista contiene fechas desde el día siguiente hasta un máximo de seis días después.
        """
        fechas = []
        
        # Separar la fecha de entrada en día, mes y año
        dia, mes, año = map(int, salidaFecha.split('/'))
        
        for _ in range(6):  # Para obtener 6 fechas futuras
            dia += 1
            
            # Comprobar si el día supera el número máximo de días del mes
            if dia > 30:
                dia = 1
                mes += 1
                
                # Comprobar si el mes supera el número máximo de meses
                if mes > 12:
                    mes = 1
                    año += 1
            
            # Formatear la nueva fecha en la lista
            fechaLlegada = f"{dia}/{mes}/{año}"
            fechas.append(fechaLlegada)
        
        return fechas

    @classmethod
    def horasDisponibles(cls,fecha):
        """
        Genera una lista de horarios disponibles para una fecha dada.
        La lógica es la siguiente:
            1. La fecha se descompone en día, mes y año.
            2. Se determina si el día es par o impar.
            3. Se determina si el mes es igual al día.
            4. Se generan horarios disponibles basados en las siguientes reglas:
                - Si el día es par: horarios cada hora desde las 6:00 hasta las 20:00.
                - Si el día es impar: horarios cada hora, pero comienza a las 8:30.
                - Si el mes es igual al día:
                    - Se ajusta la lista para que contenga horarios cada dos horas.
                    - Para días pares, los horarios son cada dos horas desde las 6:00 hasta las 20:00.
                    - Para días impares con mes igual al día, los horarios son cada dos horas comenzando desde las 8:30.
        """
        horarios = []

        # Separar la fecha en día, mes y año
        dia, mes, año = map(int, fecha.split('/'))

        # Determinar si el día es par y si el mes es igual al día
        diaEsPar = dia % 2 == 0
        mesIgualADia = mes == dia

        for hora in range(6, 21):  # Iterar sobre las horas de 6 a 20
            if diaEsPar:  # Día par: horarios cada hora
                horarios.append(f"{hora:02d}:00")
            else:  # Día impar: horarios cada hora, pero comienza a las 8:30
                if hora >= 8:
                    horarios.append(f"{hora:02d}:30")

        if mesIgualADia:  # Si el mes es igual al día, ajustar para que sea cada dos horas
            horariosCadaDosHoras = []
            for hora in range(6, 21, 2):  # Cada dos horas
                if diaEsPar:
                    horariosCadaDosHoras.append(f"{hora:02d}:00")
                else:  # Día impar con mes igual al día: cada dos horas a partir de las 8:30
                    if hora >= 8:
                        horariosCadaDosHoras.append(f"{hora:02d}:30")
            horarios = horariosCadaDosHoras  # Reemplazar la lista original con la lista ajustada cada dos horas

        return horarios

    # Métodos Get y Set

    # Get y Set para nombre
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    # Get y Set para dinero
    def getDinero(self):
        return self._dinero
    
    def setDinero(self, dinero):
        self._dinero = dinero

    # Get y Set para capacidad de vehículos
    def getCapacidadVehiculos(self):
        return self._capacidadVehiculos
    
    def setCapacidadVehiculos(self, capacidadVehiculos):
        self._capacidadVehiculos = capacidadVehiculos

    # Get y Set para destinos
    def getDestinos(self):
        return self._destinos
    
    def setDestinos(self, destinos):
        self._destinos = destinos

    # Get y Set para comisión
    def getComision(self):
        return self._comision
    
    def setComision(self, comision):
        self._comision = comision

    # Get y Set para ubicación
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    # Get y Set para administrador
    def getAdministrador(self):
        return self._administrador
    
    def setAdministrador(self, administrador):
        self._administrador = administrador

    # Get y Set para transportadoras
    @classmethod
    def getTransportadoras(cls):
        return cls.transportadoras

    @classmethod
    def setTransportadoras(cls, transportadoras):
        cls.transportadoras = transportadoras

    # Get y Set para viajes
    @classmethod
    def getViajes(cls):
        return cls.viajes

    @classmethod
    def setViajes(cls, viajes):
        cls.viajes = viajes

    # Get y Set para viajesEnCurso
    @classmethod
    def getViajesEnCurso(cls):
        return cls.viajesEnCurso

    @classmethod
    def setViajesEnCurso(cls, viajesEnCurso):
        cls.viajesEnCurso = viajesEnCurso

    # Get y Set para reservas
    @classmethod
    def getReservas(cls):
        return cls.reservas

    @classmethod
    def setReservas(cls, reservas):
        cls.reservas = reservas

    # Get y Set para historial
    @classmethod
    def getHistorial(cls):
        return cls.historial

    @classmethod
    def setHistorial(cls, historial):
        cls.historial = historial

    # Get y Set para facturas
    @classmethod
    def getFacturas(cls):
        return cls.facturas

    @classmethod
    def setFacturas(cls, facturas):
        cls.facturas = facturas

    # Get y Set para pasajeros
    @classmethod
    def getPasajeros(cls):
        return cls.pasajeros

    @classmethod
    def setPasajeros(cls, pasajeros):
        cls.pasajeros = pasajeros

    # Get y Set para Lista de terminales
    @classmethod
    def getListaTerminales(cls):
        return cls.listaTerminales

    @classmethod
    def setListaTerminales(cls, listaTerminales):
        cls.listaTerminales = listaTerminales
