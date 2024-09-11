from persona import Persona
from constantes.incentivo import Incentivo
from administrativo.vehiculo import Vehiculo
from administrativo.taller import Taller

class Mecanico (Persona, Incentivo):

    _mecanicos = []

    def __init__ (self, id, edad, nombre, genero, historial, experiencia, dinero, facturas, taller, diasRestantes, diasTrabajados):

        super.__init__(id, edad, nombre, genero, historial, experiencia, dinero, facturas, diasRestantes, diasTrabajados)

        self._taller = taller
        self._estado = True
        self._historialReparados = []
        self._vehiculosReparando = []
        taller.agregarMecanico(self)
        self._experiencia = 1
        Mecanico._mecanicos.append (self)

    #Overriding
    def identificarse (self):

        return (f"Soy un mecánico, mi nombre es {self._getNombre()}, estoy asociado al taller {self._taller.getNombre()} mi estado es {self._estado}")

    def agregarVehiculoCola (self, vehiculo):

        self._vehiculosReparando.append(vehiculo)

    def repararVehiculo (self, vehiculo):

        vehiculo.reparacion()
        self._vehiculosReparando.remove(vehiculo)
        vehiculo.getTransportadora().getTaller().removerVehiculoReparacion(vehiculo)
        self._historialReparados.append(vehiculo)
        vehiculo.setReparando (False)
        self.calcularExperiencia ()

    def calcularExperiencia (self):
        
        if (self._experiencia < 50 and len(self._historialReparados) % 10 == 0):

            self._experiencia = len(self._historialReparados)/5
    
    def renovarContrato (self, dias):

        self.setDiasRestantesContr (dias)

    #Override

    def descuento (self):

        dineroTransportadora = self._taller.getTransportadora().getDinero()

        if (len(self.getHistorialReparados()) > 10):

            self._dinero += Incentivo.incentivoBase
            self._taller.getTransportadora().setDinero (dineroTransportadora - Incentivo.incentivoBase)

    #Override

    def bonificacion (self):

        dineroTransportadora = self._taller.getTransportadora().getDinero()

        if (self._experiencia >= 5):

            self._dinero += Incentivo.incentivoBase
            self._taller.getTransportadora().setDinero (dineroTransportadora - Incentivo.incentivoBase)

    #getters and setters

    def setTaller (self, taller):

        self._taller = taller

    def getTaller (self):

        return (self._taller)
    
    def setHistorialReparados (self, historial):

        self._historialReparados = historial

    def getHistorialReparados (self):

        return (self._historialReparados)
    
    def setEstado (self, estado):

        self._estado = estado

    def getEstado (self):

        return (self._estado)
    
    def setVehiculosReparando (self, vehiculos):

        self._vehiculosReparando = vehiculos
    
    def getVehiculosReparando (self):

        return (self._vehiculosReparando)
    
    def getNombre (self):

        return(self._nombre)
    
    @classmethod
    def setMecanicos (cls, mecanicos):

        Mecanico._mecanicos = mecanicos
    
    @classmethod
    def getMecanicos (cls):

        return (Mecanico._mecanicos)
    
    @classmethod
    def agregarMecanico (cls, mecanico):

        cls._mecanicos.append(mecanico)

    def removerMecanico (cls, mecanico):

        cls._mecanicos.remove (mecanico)


    


