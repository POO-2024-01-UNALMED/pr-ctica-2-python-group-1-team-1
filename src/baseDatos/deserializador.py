import pickle

from src.gestorAplicacion.administrativo.terminal import Terminal
from src.gestorAplicacion.administrativo.viaje import Viaje
from src.gestorAplicacion.administrativo.transportadora import Transportadora
from src.gestorAplicacion.administrativo.vehiculo import Vehiculo
from src.gestorAplicacion.administrativo.taller import Taller
from src.gestorAplicacion.administrativo.factura import Factura
from src.gestorAplicacion.usuarios.persona import Persona # Falta verificar que funcione como en Java que si hereda automaticamente se serializa
from src.gestorAplicacion.tiempo.tiempo import Tiempo

class Deserializador():
    @staticmethod
    def deserializar(nombre, listaSet):

        picklefile = open(f'src/baseDatos/temp/{nombre}.txt', 'rb') # Abrir la ruta de nuestro archivo
        
        objetos = pickle.load(picklefile) # Deserializar la lista
        
        listaSet(objetos) # Aplicar el Seteo de los objetos

        picklefile.close() # Cerrar el archivo

    @staticmethod
    def deserializarListas():
        # Comentadas temporalmente hasta tener la lógica funcionando

        Deserializador.deserializar("transportadora", Transportadora.setTransportadoras)
        Deserializador.deserializar("transportadorasAsociadas", Terminal.setTransportadoras)
        Deserializador.deserializar("terminal", Terminal.setListaTerminales)
        Deserializador.deserializar("historialViajes", Terminal.setHistorial)
        Deserializador.deserializar("viajesEnCurso", Terminal.setViajesEnCurso)
        Deserializador.deserializar("viajesDisponibles", Terminal.setViajes)
        Deserializador.deserializar("reservas", Terminal.setReservas)
        Deserializador.deserializar("facturas", Terminal.setFacturas)
        #Deserializador.deserializar("pasajeros", Terminal.setPasajeros)
        #Deserializador.deserializar("tiempoObjetos", Tiempo.setTiempos)
        # Serializador.deserializar("personas", Persona.setPersonas)  # Aún no se crea el método
        Deserializador.deserializar("facturas", Factura.setFacturasCreadas)
        Deserializador.deserializar("talleres", Taller.setListaTalleres)
        Deserializador.deserializar("vehiculos", Vehiculo.setListaVehiculos)

