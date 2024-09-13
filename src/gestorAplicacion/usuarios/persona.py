# SOLUCIÓN IMPORTACIONES --------------------------------------------------------------
import sys
import os
sys.path.append(os.path.abspath("src"))
#--------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
from multimethod import multimethod
from gestorAplicacion.constantes.incentivo import Incentivo
from gestorAplicacion.constantes.destino import Destino
"""from gestorAplicacion.administrativo.viaje import Viaje
from gestorAplicacion.administrativo.factura import Factura
from gestorAplicacion.administrativo.terminal import Terminal
from gestorAplicacion.administrativo.transportadora import Transportadora
from gestorAplicacion.usuarios.pasajero import Pasajero"""


class Persona(ABC, Incentivo):
    listapersonas = []
    
    @multimethod
    def __init__(self, id : int, edad: int, nombre: str, genero: str, historial: list, experiencia: int, dinero: float, facturas: list, diasRestantesContr: int, diasTrabajados: int):
        
        self.id = id
        self.edad = edad
        self.nombre = nombre
        self.genero = genero
        self.historial = historial
        self.experiencia = experiencia
        self.dinero = dinero
        self.facturas = facturas
        self.diasRestantesContr = diasRestantesContr
        self.diasTrabajados = diasTrabajados
        Persona.listapersonas.append(self)
    
    @multimethod
    def __init__(self, id: int, edad: int, nombre: str, genero: str, dinero: float):
        
        self.id = id
        self.edad = edad
        self.nombre = nombre
        self.genero = genero
        self.dinero = dinero
        Persona.listapersonas.append(self)
        
    @multimethod
    def __init__(self, id: int, edad: int, nombre: str):
        """Iniciador para clase Persona para heredar en Pasajero"""
        
        self.id = id
        self.edad = edad
        self.nombre = nombre
        Persona.listapersonas.append(self)

    def aumentarDinero(self, dinero):
        
        self.dinero += dinero
        
    def reducirDinero(self, dinero):
        
        self.dinero -= dinero
        
    def bonoBienvenida(self, transportadora):
        
        pass
        
    
    def verHistorialViajes(self):
        from gestorAplicacion.administrativo.viaje import Viaje
        
        resultado = ""
        
        if (len(self.historial) != 0):
            
            for viaje in self.historial:
                
                resultado += (
                    "Id : " + viaje.getId() +
                    "\nTarifa : " + viaje.getTarifa() +
                    "\nOrigen : " + viaje.getSalida() +
                    "\nDestino : " + viaje.getLlegada() + 
                    "\nHora de inicio : " + viaje.getHora() +
                    "\nDuración : " + viaje.getDuracion() + 
                    "\nFecha : " + viaje.getFecha() + "\n\n")

            return resultado
        
        else:
            
            return self.nombre + " no ha viajado a ningún lado"

    def mostrarFactura(self, factura):
        from gestorAplicacion.administrativo.viaje import Viaje #
        from gestorAplicacion.administrativo.factura import Factura #
        from gestorAplicacion.administrativo.terminal import Terminal #
        from gestorAplicacion.administrativo.transportadora import Transportadora #
        from gestorAplicacion.usuarios.pasajero import Pasajero #
        from gestorAplicacion.usuarios.conductor import Conductor #
        from gestorAplicacion.administrativo.vehiculo import Vehiculo #
        from gestorAplicacion.administrativo.taller import Taller #

        
        if (factura in self.getFacturas()):
            
            if(isinstance(self, Pasajero)):
                
                return (
                        "Numero de su factura: " + str(factura.getNumeroFactura()) +
                        "\nTotal: " + str(factura.getTotal()) +
                        "\nPasajero: " + factura.getPasajero().getNombre() + 
                        "\nTerminal: " + factura.getTerminal().getNombre() +
                        "\nConductor: " + factura.getConductor().getNombre() +
                        "\nViaje: " + factura.getViaje().getLlegada() + 
                        "\nVehículo: " + factura.getVehiculo().getModelo() +
                        "\nTransportadora: " + factura.getTransportadora().getNombre())	     
            
            elif (isinstance(self, Conductor)):
                
                return ("Numero de su factura: " + str(factura.getNumeroFactura()) + 
						"\nTotal:" + str(factura.getTotal()) + 
						"\nTransportadora: " + factura.getTransportadora().getNombre() +
						"\nVehículo conducido : " + factura.getVehiculo().getModelo())
                    
            
            return ("Numero de su factura: " + str(factura.getNumeroFactura()) + 
					"\nTotal:" + str(factura.getTotal()) + 
					"\nTransportadora: " + factura.getTransportadora().getNombre() +
					"\nTaller: " + factura.getTaller().getNombre())
                
    @abstractmethod
    def identificarse(self):
        
        pass
    
    def consultarDinero(self):
        from gestorAplicacion.administrativo.factura import Factura
        
        dinero_gastado = 0
        
        if  (self.facturas):
            
            for factura in self.facturas:
                
                dinero_gastado += factura.getTotal()
                
            self.dinero -= dinero_gastado
            return self.dinero
        
        else:
            
            return self.dinero
    
    def tomarViaje(self, destino, fecha, terminal):
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.usuarios.pasajero import Pasajero
        from gestorAplicacion.administrativo.terminal import Terminal
        from gestorAplicacion.administrativo.transportadora import Transportadora
        
        self.elegirDestino(destino, terminal)
        disponiblesAtomar = self.verDisponibilidad(destino, fecha, terminal)
        viajeElegido = disponiblesAtomar[0]
        
        for viaje in disponiblesAtomar:
            
            if (viaje.getTarifa() < viajeElegido.getTarifa()):
                
                viajeElegido = viaje
                
        
        if (self.dinero >= viajeElegido.getTarifa()):
            
            tarifa = viajeElegido.getTarifa()
            
            viajeElegido.getPasajeros().append(self)
            
            self.historial.append(viajeElegido)
            self.dinero -= tarifa
            
            
            for transportadora in Terminal.getTransportadoras():
                
                if (transportadora.getDestinoAsignado() == viajeElegido.getLlegada()):
                    
                    for pasajero in transportadora.getPasajeros():
                        
                        if (pasajero.getId() == self.getId()):
                            
                            transportadora.getPasajeros().remove(pasajero)
            
            return viajeElegido
        
        else: 
            return None
    
    def reservarViaje(self, destino, fecha, pasajeros, terminal):
        from gestorAplicacion.administrativo.terminal import Terminal
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo
        from gestorAplicacion.administrativo.transportadora import Transportadora
        
        costo = 0
        viajeReservado = None
        viajesReservables = []
        viajesReservablesOtraFecha = []
        
        for viaje in Terminal.getViajes():
            
            if ((viaje.getLlegada() == destino) and viaje.getFecha() == fecha and viaje.getVehiculo().getCapacidad() >= len(pasajeros)):
                
                viajesReservables.append(viaje)
            
            elif (viaje.getLlegada() == destino):
                
                viajesReservablesOtraFecha.append(viaje)
        
        if (viajesReservables):
            
            viajeReservado = viajesReservables[0]
            
            for viaje in viajesReservables:
                
                if (viaje.getTarifa() < viajeReservado.getTarifa()):
                    
                    viajeReservado = viaje
                    
            
            costo = viajeReservado.getTarifa()*len(pasajeros)
            
            if (costo <= self.dinero):
                
                viajeReservado.setPasajeros(pasajeros)
                Terminal.getViajes().remove(viajeReservado)
                self.dinero -= costo
                
            for pasajero in pasajeros:
                
                pasajero.getHistorial().append(viajeReservado)
        
        else:
            
            viajeReservado = viajesReservablesOtraFecha[0]
            
            for viaje in viajesReservablesOtraFecha:
                
                if (viaje.getTarifa() < viajeReservado.getTarifa()):
                    
                    viajeReservado = viaje
            
            costo = viajeReservado.getTarifa()*len(pasajeros)
            
            if (costo <= self.dinero):
                
                viajeReservado.setPasajeros(pasajeros)
                Terminal.getViajes().remove(viajeReservado)
                self.dinero -= costo
            
            for pasajero in pasajeros:
                
                pasajero.getHistorial().append(viajeReservado)
                    
        for transportadora in Terminal.getTransportadoras():
            
            if (transportadora.getDestinoAsignado() == viajeReservado.getLlegada()):
                
                for viaje in transportadora.getViajesAsignados():
                    
                    if (viaje.getId() == viajeReservado.getId()):
                        
                        transportadora.getViajesAsignados().remove(viaje)
                
        return viajeReservado
    
    def verDisponibilidad(self, destino, fecha, terminal):
        from gestorAplicacion.administrativo.terminal import Terminal
        from gestorAplicacion.administrativo.viaje import Viaje
        from gestorAplicacion.administrativo.vehiculo import Vehiculo
        from gestorAplicacion.usuarios.pasajero import Pasajero
        
        viajesDisponibles = []
        viajesDisponiblesEnOtraFecha = []
        
        for viaje in Terminal.getViajes():
            
            if (viaje.getLlegada() == destino and viaje.getFecha() == fecha and len(viaje.getPasajeros()) < viaje.getVehiculo().getCapacidad()):
                
                viajesDisponibles.append(viaje)
            
            elif (viaje.getLlegada() == destino and (not(viaje.getFecha() == fecha)) and len(viaje.getPasajeros()) < viaje.getVehiculo().getCapacidad()):
                
                viajesDisponiblesEnOtraFecha.append(viaje)
            
        
        if viajesDisponibles:
            
            return viajesDisponibles

        else:
            
            return viajesDisponiblesEnOtraFecha
        
    def elegirDestino(self, destino, terminal):
        from gestorAplicacion.administrativo.terminal import Terminal
        from gestorAplicacion.administrativo.transportadora import Transportadora
        from gestorAplicacion.usuarios.pasajero import Pasajero
        
        
        for d in Terminal.getDestinos():
            
            if (d == destino ):
                
                for transportadora in Terminal.getTransportadoras():
                    
                    if (destino == transportadora.getDestinoAsignado()):
                        
                        transportadora.getPasajeros().append(self)
                        
    
    @abstractmethod
    def renovarContrato(self):
        
        pass
    
    def setId(self, id):
        
        self.id = id
        
    def getId(self):
        
        return self.id
    
    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero

    def setHistorial(self, historial):
        self.historial = historial

    def getHistorial(self):
        return self.historial

    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def getExperiencia(self):
        return self.experiencia

    def setDinero(self, dinero):
        self.dinero = dinero

    def getDinero(self):
        return self.dinero

    def setFacturas(self, facturas):
        self.facturas = facturas

    def getFacturas(self):
        return self.facturas

    def setDiasRestantesContr(self, diasRestantesContr):
        self.diasRestantesContr = diasRestantesContr

    def getDiasRestantesContr(self):
        return self.diasRestantesContr

    def setDiasTrabajados(self, diasTrabajados):
        self.diasTrabajados = diasTrabajados

    def getDiasTrabajados(self):
        return self.diasTrabajados
                    
    @classmethod
    def getSerializarPersonas(cls):
        return cls.listapersonas
    
    @classmethod
    def setSerializarPersonas(cls, lista):
        cls.listapersonas = lista
                    
                
                
        
        
                
                
                
        
        
        
        
        
        
                
                
            
            
            
            
            
                
                
                
                
    
        
        
    
    
    
    