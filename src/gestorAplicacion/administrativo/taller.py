# SOLUCIÓN IMPORTACIONES --------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath("src"))
#--------------------------------------------------------------------------------------

import math
import random
from gestorAplicacion.administrativo.transportadora import Transportadora
from src.gestorAplicacion.tiempo.tiempo import Tiempo

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
                vehiculo.setFechaHoraReparacion (Tiempo.fechaHora + 700 - round(i.getExperiencia() * 7))
                vehiculo.setMecanicoAsociado (i)
                self._vehiculosEnReparacion.append(vehiculo)
                vehiculo.setEstado(False)
                vehiculo.setReparando(True)
                vehiculo.getMecanicoAsociado().setEstado(False)
                i.setEstado(False)
                return
            
        for i in range (0, len(self._mecanicos), 1):

            if i == 0:

                mecanico = self._mecanicos[i]

            if self._mecanicos[i].getVehiculosReparando()[-1].getFechaHoraReparacion() <= mecanico.getVehiculosReparando()[-1].getFechaHoraReparacion():

                mecanico = self._mecanicos[i]

        mecanico.agregarVehiculoCola(vehiculo)
        vehiculo.setFechaHoraReparacion(mecanico.getVehiculosReparando()[-1].getFechaHoraReparacion() + 700 - round(mecanico.getExperiencia() * 7))
        vehiculo.setMecanicoAsociado(mecanico)
        self._vehiculosEnReparacion.append(vehiculo)
        vehiculo.setEstado(False)
        vehiculo.setReparando(True)
        vehiculo.getMecanicosAsociado().setEstado(False)
        mecanico.setEstado(False)
        return
        
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
                tiempo = 1440 - round(i.getExperiencia()*1440/100)

                count = False

        if count:

            for i in range (0, len(self._mecanicos), 1):

                if (i == 0):

                    mecanico = self._mecanicos[i]
                    
                if (self._mecanicos[i].getVehiculosReparando()[-1].getFechaHoraReparacion() <= mecanico.getVehiculosReparando()[-1].getFechaHoraReparacion()):
                        
                    mecanico = self._mecanicos [i]


            tiempo = (mecanico.getVehiculosReparando()[-1].getFechaHoraReparacion() + 1440 - round(mecanico.getExperiencia()*1440/100)) - Tiempo.fechaHora

        precio = round((vehiculo.getPrecio() - (vehiculo.getPrecio()*vehiculo.getIntegridad()/100))/2)
        precioFinal = round(precio + (mecanico.getExperiencia() * precio / 200))
  
        cotizacion = [precioFinal, tiempo]
        return (cotizacion)
    
    def aplicarGastos (self, vehiculo):

        precio = round((vehiculo.getPrecio() - (vehiculo.getPrecio()*vehiculo.getIntegridad()/100))/2)
        precioFinal = round (precio + (vehiculo.getMecanicoAsociado().getExperiencia()*precio/200))
        vehiculo.getTransportadora().reducirDinero(precioFinal)
        vehiculo.getMecanicoAsociado().aumentarDinero(round(precioFinal*0.3))

        
    def agregarVehiculoVenta (self, vehiculo):

        self._vehiculosEnVenta.append (vehiculo)
        vehiculo.setPrecio (self.calcularValor(vehiculo))
        vehiculo.setFechaHoraReparacion (round(Tiempo.getFechaHora() + (1440 + random.randint())))
        vehiculo.setReparando (True)

    def venderVehiculo (self, vehiculo):

        self._transportadora.aumentarDinero (vehiculo.getPrecio())
        self._vehiculosEnVenta.remove (vehiculo)
        self._transportadroa.removerVehiculo (vehiculo)
        vehiculo.setReparando (False)

    def calcularValor (self, vehiculo):

        return(round((vehiculo.getPrecio() - (vehiculo.getPrecio() * 0.3)) * vehiculo.getIntegridad()/100))

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

