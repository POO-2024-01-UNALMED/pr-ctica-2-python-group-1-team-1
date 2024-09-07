import pickle
import os

from src.gestorAplicacion.administrativo.terminal import Terminal
from src.gestorAplicacion.administrativo.viaje import Viaje
from src.gestorAplicacion.administrativo.transportadora import Transportadora
from src.gestorAplicacion.administrativo.vehiculo import Vehiculo
from src.gestorAplicacion.administrativo.taller import Taller
from src.gestorAplicacion.administrativo.factura import Factura
from src.gestorAplicacion.usuarios.persona import Persona # Falta verificar que funcione como en Java que si hereda automaticamente se serializa
from src.gestorAplicacion.tiempo.tiempo import Tiempo

class Serializador():
    @staticmethod
    def serializar(nombre, lista):
        if not os.path.exists('src/baseDatos/temp'):
            os.makedirs('src/baseDatos/temp') # Crear la carpeta temp en caso que no exista

        picklefile = open(f'src/baseDatos/temp/{nombre}.txt', 'wb') # Crear la ruta que tendra nuestro archivo

        pickle.dump(lista, picklefile) # Operacion de serializado

        picklefile.close() # Cerrar el archivo

    @staticmethod
    def serializarListas():
        # Comentadas temporalmente hasta tener la lógica funcionando

        #Serializador.serializar("transportadora", Transportadora.getTransportadoras())  # OBJETOS DE TRANSPORTADORA
        #Serializador.serializar("transportadorasAsociadas", Terminal.getTransportadoras())  # OBJETOS TRANSPORTADORA ASOCIADOS A LA TERMINAL
        #Serializador.serializar("terminal", Terminal.getListaTerminales())  # OBJETO TERMINAL
        #Serializador.serializar("historialViajes", Terminal.getHistorial())  # VIAJES TERMINADOS - HISTORIAL
        #Serializador.serializar("viajesEnCurso", Terminal.getViajesEnCurso())  # VIAJES SIN TERMINAR - EN CURSO
        #Serializador.serializar("viajesDisponibles", Terminal.getViajes())  # VIAJES SIN SALIR - DISPONIBLES
        #Serializador.serializar("reservas", Terminal.getReservas())  # VIAJES EN RESERVA
        #Serializador.serializar("facturas", Terminal.getFacturas())  # FACTURAS ASOCIADAS
        #Serializador.serializar("pasajeros", Terminal.getPasajeros())  # PASAJEROS --- O solo pasajeros sin viaje??????????
        Serializador.serializar("tiempoObjetos", Tiempo.tiempos())  # OBJETOS TIEMPO - PROGRESO DEL TIEMPO
        #Serializador.serializar("personas", Persona.getSerializarPersonas())  # OBJETOS TIPO PERSONA ---- Aun no se crea el método
        #Serializador.serializar("facturas", Factura.getFacturasCreadas())  # OBJETOS TIPO FACTURA
        #Serializador.serializar("talleres", Taller.getListaTalleres())  # OBJETOS TIPO TALLER
        #Serializador.serializar("vehiculos", Vehiculo.getListaVehiculos())  # OBJETOS TIPO VEHICULO