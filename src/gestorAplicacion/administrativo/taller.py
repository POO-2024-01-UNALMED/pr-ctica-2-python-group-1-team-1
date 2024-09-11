import math
import random
from administrativo.transportadora import Transportadora

class Taller ():

    _listaTalleres = []

    def __init__ (self, transportadora, ubicacion, nombre, capacidad):

        self._factura = None #Necesario?

        self._transportadora = transportadora
        self._ubicacion = ubicacion
        self._nombre = nombre
        self._capacidad = capacidad
        transportadora.setTaller (self)
        self._mecanicos = []
        self._vehiculosEnReparacion = []
        self._vehiculosEnVenta = []
        Taller._listaTalleres.append (self)


    def agregarMecanico (self, mecanico):

        self._mecanicos.append(mecanico)

    def removerMecanico (self, mecanico):

        self._mecanicos.remove (mecanico)

    def agregarVehiculoReparacion (self, vehiculo):

        mecanico = None

        for i in self._mecanicos:

            if i.getEstado ():

                i.agregarVehiculoCola(vehiculo)
                vehiculo.setFechaHoraReparacion ()
        
    def removerVehiculoReparacion (self, vehiculo):

        self._vehiculosEnReparacion.remove (vehiculo)

        
    def generarCotizacion (self, vehiculo):

        cotizacion = []
        mecanico = None
        tiempo = 0
        count = True

        for i in self._mecanicos:

            if i.getEstado():

                mecanico = i
                tiempo = 1440 - math.round(i.getExperiencia()*1440/100)

            count = False

        if count:

            for i in range (0, len(self._mecanicos), 1):

                if (i == 0):

                    mecanico = self._mecanicos[i]
                    
                if (self._mecanicos[i].getVehiculosReparando()[-1].getFechaHoraReparacion() <= mecanico.getVehiculosReparando()[-1].getFechaHoraReparacion()):
                        
                    mecanico = self._mecanicos [i]


            tiempo = (mecanico.getVehiculosReparando[-1].getFechaHoraReparacion() + 1440 - math.round(mecanico.getExperiencia()*1440/100)) - Tiempo.getFechaHora()

        precio = math.round((vehiculo.getPrecio() - (vehiculo.getPrecio()*vehiculo.getIntegridad()/100))/2)
        precioFinal = math.round(precio + (vehiculo.getMecanicoAsociado().getExperiencia() * precio / 200))
        vehiculo.getTransportadora().reducirDinero(precioFinal)
        vehiculo.getMecanicoAsociado().aumentarDinero(math.round(precioFinal*0.3))

        
    def agregarVehiculoVenta (self, vehiculo):

        self._vehiculosEnVenta.append (vehiculo)
        vehiculo.setPrecio (self.calcularValor(vehiculo))
        vehiculo.setFechaHoraReparacion (math.round(Tiempo.getFechaHora() + (1440 + random.randint())))
        vehiculo.setReparando (True)

    def venderVehiculo (self, vehiculo):

        self._transportadora.aumentarDinero (vehiculo.getPrecio())
        self._vehiculosEnVenta.remove (vehiculo)
        self._transportadroa.removerVehiculo (vehiculo)
        vehiculo.setReparando (False)

    def calcularValor (self, vehiculo):

        return(math.round((vehiculo.getPrecio() - (vehiculo.getPrecio() * 0.3)) * vehiculo.getIntegridad()/100))

    #Getters and setters

    def setNombre (self, nombre):

        self._nombre = nombre

    def getNombre (self):

        return (self._nombre)
    
    def setVehiculosEnReparacion (self, vehiculos):

        self._vehiculosEnReparacion = vehiculos
    
    def getVehiculosEnReparacion (self):

        return (self._vehiculosEnReparacion)
    
    def setVehiculosEnVenta (self, vehiculos):

        self._vehiculosEnVenta = vehiculos

    def getVehiculosEnVenta (self):

        return (self._vehiculosEnVenta)
    
    def setTransportadora (self, transportadora):

        self._transportadora = transportadora

    def getTransportadora (self):

        return (self._transportadora)
    
    def setUbicacion (self, ubicacion):

        self._ubicacion = ubicacion

    def getUbicacion (self):

        return (self._ubicacion)
    
    def setFactura (self, factura):

        self._factura = factura
    
    def getFactura (self):

        return (self._factura)
    
    def setMecanicos (self, mecanicos):

        self._mecanicos = mecanicos
    
    def getMecanicos (self):

        return (self._mecanicos)
    
    def setCapacidad (self, capacidad):

        self._capacidad = capacidad

    def getCapacidad (self):

        return (self._capacidad)
    
    @classmethod
    def setListaTalleres (cls, talleres):

        Taller._listaTalleres = talleres

    @classmethod
    def getListaTalleres (cls):

        return (Taller._listaTalleres)

