from gestorAplicacion.constantes.incentivo import Incentivo

class Transportadora (Incentivo):
from multimethod import multimethod

class Transportadora:
    _transportadoras = [] #No se utiliza

    def __init__(self, nombre, dinero, conductores, conductoresRegistrados, pasajeros, vehiculos,
                viajesAsignados, destinoAsignado, terminal, taller, viajesTerminados, dueño, estrellas):
        self._nombre = nombre
        self._dinero = dinero
        self._conductores = conductores
        self._conductoresRegistrados = conductoresRegistrados
        self._pasajeros = pasajeros
        self._vehiculos = vehiculos
        self._viajesAsignados = viajesAsignados
        self._destinoAsignado = destinoAsignado
        self._terminal = terminal
        self._taller = taller
        self._viajesTerminados = viajesTerminados
        self._dueño = dueño
        self._estrellas = estrellas
        Transportadora._transportadoras.append(self)
        self._conductoresDespedidos = []


    def encontrarConductor(self,id):
        """Encuentra el conductor con el id dado como argumento"""
        from gestorAplicacion.usuarios.conductor import Conductor
        for conductor in self._conductores:
            if (conductor.getId() == id):
                return conductor
        return None
    
    def transportadorasViaje(viajes):#Sacar tansportadoras sin repetir
        transportadoras = []

        for viaje in viajes:
            transportadora = viaje.getVehiculo().getTransportadora()
            if transportadora not in transportadoras:
                transportadoras.append(transportadora)
    
        return transportadoras

    def ejegirViajeTransportadora(self, viajes):
        """Método para elegir el primer viaje que encuentre con la misma transportadora"""

        for viaje in viajes:
            if viaje.getVehiculo().getTransportadora():
                return viaje

    
    def despedirConductor(self, id):
        """Metodo para despedir conductor al cual se le remueve el vehiculo,
	    se le remueve de la lista de conductores de la transportadora.
	    Para esto, primero se verifica que no tenga viajes programados y 
	    que su vehiculo tenga almenos 2 conductores. Si existe algun inconveniente
	    el metodo devolvera un valor diferente para cada caso.
        """
        from gestorAplicacion.usuarios.conductor import Conductor

        conductor : Conductor = self.encontrarConductor(id)

        if (len(conductor.getHorario()) == 0):
            
            if conductor.getVehiculo() is None:
                conductor.quitarVehiculo()
                conductor.getTransportadora().getConductores().remove(conductor)
                conductor.indemnizar()
                conductor.reinicioAtributos()
                return "Se ha despedido a " + conductor.getNombre()
            
            if len(conductor.getVehiculo().getConductores()) >= 2:
                conductor.quitarVehiculo()
                conductor.getTransportadora().getConductores().remove(conductor)
                conductor.indemnizar()
                conductor.reinicioAtributos()
                return "Se ha despedido a " + conductor.getNombre()
            else:
                return "No es posible porque no hay mas conductores asignados al vehiculo asociado al conductor"
            
        else:
            return "No es posible porque el conductor tiene viajes programados"

    def mostrarConductRegistrados(self):
        mensaje = ""
        for conductor in self._conductoresRegistrados:
            mensaje += "Nombre: " + conductor.getNombre() + "#Id: " + str(conductor.getId()) + "\n"

    @multimethod
    def contratarConductorId(self, id: int):
        from gestorAplicacion.usuarios.conductor import Conductor
        conductor : Conductor = None

        for driver in self._conductoresRegistrados:

            if driver.getId() == id:
                index = self._conductoresRegistrados.index(driver)
                conductor = self._conductoresRegistrados[index]
        
        return Transportadora.contratarConductor(conductor)
    
    @multimethod
    def contratarConductor(self, conductor): #Solucionar error de importacion para hacer la sobrecarga
        """Metodo para contratar un conductor el cual se agregara
	    a la lista de conductores de la transportadora."""

        if conductor == None:
            return "No se ha encontrado el conductor"
        else:

            if (conductor.getExperiencia() >= 5):

                if (conductor.getEstadoLicencia()):
                    conductor.reinicioAtributos()
                    self.getConductores().append(conductor)
                    self.getConductoresRegistrados().remove(conductor)
                    conductor.bonoBienvenida(conductor.getTransportadora())
                    return "Se contrato a " + conductor.getNombre() + " exitosamente"
                else:
                    return "No se pudo contratar a " + conductor.getNombre() + " porque no tiene licencia activa"
            else:
                return "No se pudo contratar a " + conductor.getNombre() + " porque tiene menos de cinco años de experiencia"

    def encontrarViaje(self, id):
        """Devuelve el viaje que coincida con el id dado como argumento"""
        for viaje in self._viajesAsignados:

            if (viaje.getId() == id):
                return viaje
        return None
    
    def descuento(self):
        
        valorPagar = self.retornarValorAPagar()
        verificacionViajes = 0
        
        if(len(self.getViajesAsignados()) == len(self.getViajesTerminados())):
            
            verificacionViajes = 1
            
        
        if (valorPagar > 0):
            
            if (verificacionViajes == 0):
                
                self._dinero -= valorPagar
                self._terminal.setDinero(self.getTerminal().getDinero() + valorPagar)
                
        else: 
            self.dinero -= (valorPagar - (valorPagar*0.05))
            self._terminal.setDinero(self.getTerminal().getDinero() + valorPagar)
    
    def bonificacion(self):
        
        dineroTerminal = self.getTerminal().getDinero()
        dineroaRestarTerminal = 0
        
        for pasajero in self.getPasajeros():
            
            if (pasajero.verificarBonificacion() != 0):
                
                dineroaRestarTerminal += Incentivo.INCENTIVOBASE
                self._dinero += dineroaRestarTerminal
                
        
        self.getTerminal().setDinero(dineroTerminal - dineroaRestarTerminal)
        
    def retornarValorAPagar(self):
        
        calcularValorApagar = self._terminal.getComision() * len(self.getViajesTerminados())
        
        if (self.verificarPagoTerminal()):
            
            return calcularValorApagar
        
        return 0.0
        
        
        
        
    
    
    def mostrarConductoresActivos(self):
        mensaje = ""

        for conductor in self.getConductores():
            mensaje += "Nombre: " + conductor.getNombre()+ "  #ID: " + conductor.getId() + "\n"

    def mostrarViajesDisponibles(self, digitoDia, tipoVehiculo, conductor):
        mensaje = ""
        viajesDisponibles = []

        for viaje in self.getViajesAsignados():
            if ((abs(viaje.getValue() - digitoDia) >= 1) and (viaje.getVehiculo().getTipo == tipoVehiculo)):
                if viaje in conductor.getHorario():
                    continue
                viajesDisponibles.append(viaje)
                mensaje += "\n" + viaje.detallesViaje()
        
        return mensaje
    
    def conductoresDisponibles(self, viaje):
        """ Metodo que muestra los conductores disponibles de la terminal
	    que no tengan un viaje asignado el mismo dia del viaje pasado como
	    parametro y que los otros conductores asociados al vehiculo de cada
	    conductor no tengan viajes asignados el mismo dia del pasado como parametro"""
        conductoresLibres = []
        mensaje = ""

        for conductor in self.getConductores():
            valor = True

            if conductor.getVehiculo().getTipo() == viaje.getVehiculo().getTipo():

                for driver in conductor.getVehiculo().getConductores():

                    if driver in conductoresLibres:
                        continue

                    if driver.getHorario() == None:
                         conductoresLibres.append(driver)
                         continue
                    
                    for viaje in driver.getHorario():

                        if ((viaje.getDia().getValue() - viaje.getDia().getValue) == 0):
                            valor = False
                            break
                        else:
                            valor=True

                    if valor:
                        conductoresLibres.append(driver)
        
        for conductor in conductoresLibres:
            mensaje += "Nombre: " + conductor.getNombre()+ "  #ID: " + str(conductor.getId()) + "\n"
        
        return mensaje



    # Métodos get

    # Devuelve el nombre de la transportadora
    def getNombre(self):
        return self._nombre

    # Devuelve el dinero disponible de la transportadora
    def getDinero(self):
        return self._dinero

    # Devuelve la lista de conductores de la transportadora
    def getConductores(self):
        return self._conductores
    
    def getConductoresRegistrados(self):
        """Devuelve la lista de conductores registrados de la transportadora"""
        return self._conductoresRegistrados

    # Devuelve la lista de pasajeros de la transportadora
    def getPasajeros(self):
        return self._pasajeros

    # Devuelve la lista de vehículos de la transportadora
    def getVehiculos(self):
        return self._vehiculos

    # Devuelve la lista de viajes asignados a la transportadora
    def getViajesAsignados(self):
        return self._viajesAsignados

    # Devuelve el destino asignado a la transportadora
    def getDestinoAsignado(self):
        return self._destinoAsignado

    # Devuelve la terminal de la transportadora
    def getTerminal(self):
        return self._terminal

    # Devuelve el taller asignado a la transportadora
    def getTaller(self):
        return self._taller

    # Devuelve la lista de viajes terminados por la transportadora
    def getViajesTerminados(self):
        return self._viajesTerminados

    # Devuelve el nombre del dueño de la transportadora
    def getDueño(self):
        return self._dueño

    # Devuelve la calificación en estrellas de la transportadora
    def getEstrellas(self):
        return self._estrellas
    
    @classmethod
    def getTransportadoras(cls):
        """Devuelve la lista de todas las instancias de Transportadora."""
        return cls._transportadoras

    # Métodos set

    # Establece el nombre de la transportadora
    def setNombre(self, nombre):
        self._nombre = nombre

    # Establece el dinero disponible de la transportadora
    def setDinero(self, dinero):
        self._dinero = dinero

    # Establece la lista de conductores de la transportadora
    def setConductores(self, conductores):
        self._conductores = conductores

    def setConductoresRegistrados(self, conductoresRegistrados):
        """Establece la lista de conductores registrados de la transportadora"""
        self._conductoresRegistrados = conductoresRegistrados

    # Establece la lista de pasajeros de la transportadora
    def setPasajeros(self, pasajeros):
        self._pasajeros = pasajeros

    # Establece la lista de vehículos de la transportadora
    def setVehiculos(self, vehiculos):
        self._vehiculos = vehiculos

    # Establece la lista de viajes asignados a la transportadora
    def setViajesAsignados(self, viajesAsignados):
        self._viajesAsignados = viajesAsignados

    # Establece el destino asignado a la transportadora
    def setDestinoAsignado(self, destinoAsignado):
        self._destinoAsignado = destinoAsignado

    # Establece la terminal de la transportadora
    def setTerminal(self, terminal):
        self._terminal = terminal

    # Establece el taller asignado a la transportadora
    def setTaller(self, taller):
        self._taller = taller

    # Establece la lista de viajes terminados por la transportadora
    def setViajesTerminados(self, viajesTerminados):
        self._viajesTerminados = viajesTerminados

    # Establece el nombre del dueño de la transportadora
    def setDueño(self, dueño):
        self._dueño = dueño

    # Establece la calificación en estrellas de la transportadora
    def setEstrellas(self, estrellas):
        self._estrellas = estrellas

    @classmethod
    def setTransportadoras(cls, transportadoras):
        """Establece la lista de instancias de Transportadora."""
        cls._transportadoras = transportadoras