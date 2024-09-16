import pickle

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gestorAplicacion.administrativo.terminal import Terminal
from src.gestorAplicacion.administrativo.viaje import Viaje
from src.gestorAplicacion.administrativo.transportadora import Transportadora
from src.gestorAplicacion.administrativo.vehiculo import Vehiculo
from src.gestorAplicacion.administrativo.taller import Taller
from src.gestorAplicacion.administrativo.factura import Factura
from src.gestorAplicacion.usuarios.persona import Persona # Falta verificar que funcione como en Java que si hereda automaticamente se serializa
from src.gestorAplicacion.usuarios.pasajero import Pasajero
from src.gestorAplicacion.usuarios.mecanico import Mecanico
from src.gestorAplicacion.usuarios.conductor import Conductor
from src.gestorAplicacion.constantes.tipoPasajero import TipoPasajero
from src.gestorAplicacion.constantes.tipoVehiculo import TipoVehiculo
from src.gestorAplicacion.constantes.destino import Destino
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

        Serializador.serializar("transportadora", Transportadora.getTransportadoras())  # OBJETOS DE TRANSPORTADORA
        Serializador.serializar("transportadorasAsociadas", Terminal.getTransportadoras())  # OBJETOS TRANSPORTADORA ASOCIADOS A LA TERMINAL
        Serializador.serializar("terminal", Terminal.getListaTerminales())  # OBJETO TERMINAL
        Serializador.serializar("historialViajes", Tiempo.listahistorial())  # VIAJES TERMINADOS - HISTORIAL
        Serializador.serializar("viajesEnCurso", Terminal.getViajesEnCurso())  # VIAJES SIN TERMINAR - EN CURSO
        Serializador.serializar("viajesDisponibles", Terminal.getViajes())  # VIAJES SIN SALIR - DISPONIBLES
        Serializador.serializar("reservas", Terminal.getReservas())  # VIAJES EN RESERVA
        Serializador.serializar("facturas", Terminal.getFacturas())  # FACTURAS ASOCIADAS
        Serializador.serializar("pasajeros", Terminal.getPasajeros())  # PASAJEROS
        Serializador.serializar("personas", Persona.getSerializarPersonas())  # OBJETOS TIPO PERSONA ---- Aun no se crea el método
        Serializador.serializar("facturas", Factura.getFacturasCreadas())  # OBJETOS TIPO FACTURA
        Serializador.serializar("talleres", Taller.getListaTalleres())  # OBJETOS TIPO TALLER
        Serializador.serializar("vehiculos", Vehiculo.getListaVehiculos())  # OBJETOS TIPO VEHICULO
        Serializador.serializar("tiempoObjetos", Tiempo.getTiempos())  # OBJETOS TIEMPO - PROGRESO DEL TIEMPO

    @staticmethod
    def objetosPrueba():
        Tiempo()

        #TERMINAL
        terminal = Terminal("Terminal del norte", 99999999, 500, 1, 20, None, None, 0, Destino.MEDELLIN)

        #TRANSPORTADORAS
        transportadoraRapida = Transportadora("Transportadora Rapida", 196000.0, [], [], [], [], None, terminal, None, [], [], None, 4.5)
        transportadoraEficiente = Transportadora("Transportadora Eficiente", 189000.0, [], [], [], [], None, terminal, None, [], [], None, 4.0)
        transportadoraExpress = Transportadora("Transportadora Express", 223000.0, [], [], [], [], None, terminal, None, [], [], None, 3.5)
        transportadoraSegura = Transportadora("Transportadora Segura", 204000.0, [], [], [], [], None, terminal, None, [], [], None, 5.0)
        transportadoraGlobal = Transportadora("Transportadora Global", 305000.0, [], [], [], [], None, terminal, None, [], [], None, 2.5)
        transportadoraLocal = Transportadora("Transportadora Local", 250000.0, [], [], [], [], None, terminal, None, [], [], None, 4.7)
        # Crear lista de transportadoras
        transportadoras = [
            transportadoraRapida,
            transportadoraEficiente,
            transportadoraExpress,
            transportadoraSegura,
            transportadoraGlobal,
            transportadoraLocal
        ]
        # Asignar la lista de transportadoras a la terminal
        Terminal.setTransportadoras(transportadoras)

    @staticmethod
    def crearObjetos():

        #TERMINAL
        terminal = Terminal("Terminal del norte", 99999999, 500, 1, 20, None, None, 0, Destino.MEDELLIN)

        #TRANSPORTADORAS
        transportadoraRapida = Transportadora("Transportadora Rapida", 196000.0, [], [], [], [], [], terminal, None, [], [], None, 4.5)
        transportadoraEficiente = Transportadora("Transportadora Eficiente", 189000.0, [], [], [], [], [], terminal, None, [], [], None, 4.0)
        transportadoraExpress = Transportadora("Transportadora Express", 223000.0, [], [], [], [], [], terminal, None, [], [], None, 3.5)
        transportadoraSegura = Transportadora("Transportadora Segura", 204000.0, [], [], [], [], [], terminal, None, [], [], None, 5.0)
        transportadoraGlobal = Transportadora("Transportadora Global", 305000.0, [], [], [], [], [], terminal, None, [], [], None, 2.5)
        transportadoraLocal = Transportadora("Transportadora Local", 250000.0, [], [], [], [], [], terminal, None, [], [], None, 4.7)
        # Crear lista de transportadoras
        transportadoras = [
            transportadoraRapida,
            transportadoraEficiente,
            transportadoraExpress,
            transportadoraSegura,
            transportadoraGlobal,
            transportadoraLocal
        ]
        # Asignar la lista de transportadoras a la terminal
        Terminal.setTransportadoras(transportadoras)

        #DESTINOS PARA CADA TRANSPORTADORA
        # Crear y asignar listas de destinos
        destinos1 = [
            Destino.COOPACABANA,
            Destino.BELLO,
            Destino.CALI,
            Destino.ITAGUI,
            Destino.ENVIGADO,
            Destino.GUARNE,
            Destino.RIONEGRO,
            Destino.MARINILLA
        ]
        transportadoraExpress.setDestinos(destinos1)

        destinos2 = [
            Destino.SABANETA,
            Destino.LAESTRELLA,
            Destino.RIONEGRO,
            Destino.GIRARDOTA,
            Destino.GUARNE,
            Destino.MARINILLA,
            Destino.BOGOTA,
            Destino.LAPINTADA
        ]
        transportadoraSegura.setDestinos(destinos2)

        destinos3 = [
            Destino.BARBOSA,
            Destino.BUENAVENTURA,
            Destino.BUCARAMANGA,
            Destino.ANGELOPOLIS,
            Destino.COOPACABANA,
            Destino.BELLO,
            Destino.GIRARDOTA,
            Destino.GUATAPE,
            Destino.LAGUAJIRA
        ]
        transportadoraGlobal.setDestinos(destinos3)

        destinos4 = [
            Destino.GIRARDOTA,
            Destino.BARRANQUILLA,
            Destino.CALI,
            Destino.BARBOSA,
            Destino.ANGELOPOLIS,
            Destino.BELLO,
            Destino.LAPINTADA,
            Destino.SANTAMARTA
        ]
        transportadoraLocal.setDestinos(destinos4)

        destinos5 = [
            Destino.CARTAGENA,
            Destino.BARRANQUILLA,
            Destino.SANTAMARTA,
            Destino.BELLO,
            Destino.GIRARDOTA,
            Destino.ITAGUI,
            Destino.CALI,
            Destino.BARBOSA
        ]
        transportadoraRapida.setDestinos(destinos5)

        destinos6 = [
            Destino.GUARNE,
            Destino.LAPINTADA,
            Destino.GUATAPE,
            Destino.BARBOSA,
            Destino.MARINILLA,
            Destino.BARRANQUILLA,
            Destino.CALDAS,
            Destino.MEDELLIN
        ]
        transportadoraEficiente.setDestinos(destinos6)

        #TALLERES

        # Creación de talleres en Transportadora1
        tallerRapido = Taller(transportadoraRapida, transportadoraRapida.getDestinoAsignado(), "Taller Rápido", 10)
        # Transportadora2
        tallerEficiente = Taller(transportadoraEficiente, transportadoraEficiente.getDestinoAsignado(), "Taller Eficiente", 10)
        # Transportadora3
        tallerExpress = Taller(transportadoraExpress, transportadoraExpress.getDestinoAsignado(), "Taller Express", 10)
        # Transportadora4
        tallerSegura = Taller(transportadoraSegura, transportadoraSegura.getDestinoAsignado(), "Taller Seguro", 10)
        # Transportadora5
        tallerGlobal = Taller(transportadoraGlobal, transportadoraGlobal.getDestinoAsignado(), "Taller Global", 10)
        # Transportadora6
        # tallerLocal = Taller(transportadoraLocal, transportadoraLocal.getDestinoAsignado(), "Taller Local", 10)

        """# MECANICOS
        mecanicos1 = []
        mecanicos2 = []
        mecanicos3 = []
        mecanicos4 = []
        mecanicos5 = []
        mecanicos6 = []

        # Mecánicos que se asignarán a la transportadora1
        mecanico121 = Mecanico(121, 34, "Alejandro Vargas", 'M', [], 5, 1600.0, [], tallerRapido, None, True, 15, 200)
        mecanico122 = Mecanico(122, 28, "Sergio Morales", 'M', [], 4, 1450.0, [], tallerEficiente, None, True, 12, 180)
        mecanico123 = Mecanico(123, 37, "Ricardo López", 'M', [], 7, 1750.0, [], tallerExpress, None, True, 20, 220)

        mecanicos1.append(mecanico121)
        mecanicos1.append(mecanico122)
        mecanicos1.append(mecanico123)

        # Mecánicos que se asignarán a la transportadora2
        mecanico124 = Mecanico(124, 31, "Carlos Martínez", 'M', [], 6, 1650.0, [], tallerSegura, None, True, 14, 210)
        mecanico125 = Mecanico(125, 40, "Javier Ramírez", 'M', [], 8, 1800.0, [], tallerGlobal, None, True, 18, 230)
        mecanico126 = Mecanico(126, 29, "Fernando Pérez", 'M', [], 5, 1550.0, [], tallerRapido, None, True, 13, 200)

        mecanicos2.append(mecanico124)
        mecanicos2.append(mecanico125)
        mecanicos2.append(mecanico126)

        # Mecánicos que se asignarán a la transportadora3
        mecanico127 = Mecanico(127, 33, "Héctor Jiménez", 'M', [], 6, 1600.0, [], tallerEficiente, None, True, 17, 220)
        mecanico128 = Mecanico(128, 35, "Luis Rodríguez", 'M', [], 7, 1700.0, [], tallerExpress, None, True, 16, 230)
        mecanico129 = Mecanico(129, 30, "Manuel García", 'M', [], 5, 1500.0, [], tallerSegura, None, True, 15, 200)

        mecanicos3.append(mecanico127)
        mecanicos3.append(mecanico128)
        mecanicos3.append(mecanico129)

        # Mecánicos que se asignarán a la transportadora4
        mecanico130 = Mecanico(130, 38, "Tomás Fernández", 'M', [], 7, 1750.0, [], tallerGlobal, None, True, 19, 220)
        mecanico131 = Mecanico(131, 32, "Óscar López", 'M', [], 6, 1600.0, [], tallerRapido, None, True, 14, 210)
        mecanico132 = Mecanico(132, 31, "David Martínez", 'M', [], 5, 1550.0, [], tallerEficiente, None, True, 13, 200)

        mecanicos4.append(mecanico130)
        mecanicos4.append(mecanico131)
        mecanicos4.append(mecanico132)

        # Mecánicos que se asignarán a la transportadora5
        mecanico133 = Mecanico(133, 36, "Gabriel Silva", 'M', [], 8, 1800.0, [], tallerExpress, None, True, 20, 230)
        mecanico134 = Mecanico(134, 29, "Ricardo Vargas", 'M', [], 5, 1500.0, [], tallerSegura, None, True, 12, 180)
        mecanico135 = Mecanico(135, 34, "Adrián Rodríguez", 'M', [], 7, 1650.0, [], tallerGlobal, None, True, 18, 220)

        mecanicos5.append(mecanico133)
        mecanicos5.append(mecanico134)
        mecanicos5.append(mecanico135)

        # Mecánicos que se asignarán a la transportadora6
        mecanico136 = Mecanico(136, 40, "Héctor Hernández", 'M', [], 9, 1750.0, [], tallerRapido, None, True, 22, 240)
        mecanico137 = Mecanico(137, 33, "Eduardo Díaz", 'M', [], 6, 1600.0, [], tallerEficiente, None, True, 15, 210)

        mecanicos6.append(mecanico136)
        mecanicos6.append(mecanico137)"""

        #VEHICULOS
        # Crear listas de vehículos para cada transportadora
        vehiculos1 = []
        vehiculos2 = []
        vehiculos3 = []
        vehiculos4 = []
        vehiculos5 = []
        vehiculos6 = []

        # Vehículos para la transportadora1
        vehiculo1 = Vehiculo("ABC123", "ModeloA", 12500.00, 120.0, TipoVehiculo.BUS, transportadoraRapida)
        vehiculo2 = Vehiculo("DEF456", "ModeloB", 13500.00, 130.0, TipoVehiculo.ESCALERA, transportadoraRapida)
        vehiculo3 = Vehiculo("GHI789", "ModeloC", 14500.00, 125.0, TipoVehiculo.VANS, transportadoraRapida)
        vehiculo4 = Vehiculo("JKL012", "ModeloD", 15500.00, 140.0, TipoVehiculo.TAXI, transportadoraRapida)
        vehiculo5 = Vehiculo("MNO345", "ModeloE", 16500.00, 135.0, TipoVehiculo.BUS, transportadoraRapida)
        vehiculo6 = Vehiculo("HYU485", "ModeloF", 18500.00, 132.0, TipoVehiculo.ESCALERA, transportadoraRapida)
        vehiculo7 = Vehiculo("OIU328", "ModeloG", 14500.00, 121.0, TipoVehiculo.VANS, transportadoraRapida)
        vehiculo8 = Vehiculo("PQK748", "ModeloH", 17500.00, 139.0, TipoVehiculo.TAXI, transportadoraRapida)
       

        vehiculos1.extend([vehiculo1, vehiculo2, vehiculo3, vehiculo4, vehiculo5, vehiculo6, vehiculo7, vehiculo8])
        transportadoraRapida.setVehiculos(vehiculos1)


        # Vehículos para la transportadora2
        vehiculo11 = Vehiculo("EFG123", "ModeloK", 22500.00, 140.0, TipoVehiculo.ESCALERA, transportadoraEficiente)
        vehiculo12 = Vehiculo("HIJ456", "ModeloL", 23500.00, 145.0, TipoVehiculo.VANS, transportadoraEficiente)
        vehiculo13 = Vehiculo("KLM789", "ModeloM", 24500.00, 120.0, TipoVehiculo.TAXI, transportadoraEficiente)
        vehiculo14 = Vehiculo("NOP012", "ModeloN", 25500.00, 125.0, TipoVehiculo.BUS, transportadoraEficiente)
        vehiculo15 = Vehiculo("QRS345", "ModeloO", 26500.00, 130.0, TipoVehiculo.ESCALERA, transportadoraEficiente)
        vehiculo16 = Vehiculo("QWE788", "ModeloP", 25400.00, 144.0, TipoVehiculo.VANS, transportadoraEficiente)
        vehiculo17 = Vehiculo("VEG777", "ModeloQ", 24800.00, 128.0, TipoVehiculo.TAXI, transportadoraEficiente)
        vehiculo18 = Vehiculo("NOP000", "ModeloR", 25000.00, 129.0, TipoVehiculo.BUS, transportadoraEficiente)

        vehiculos2.extend([vehiculo11, vehiculo12, vehiculo13, vehiculo14, vehiculo15, vehiculo16, vehiculo17, vehiculo18])
        transportadoraEficiente.setVehiculos(vehiculos2)

        # Vehículos para la transportadora3
        vehiculo21 = Vehiculo("IJK123", "ModeloU", 32500.00, 135.0, TipoVehiculo.BUS, transportadoraExpress)
        vehiculo22 = Vehiculo("LMN456", "ModeloV", 33500.00, 140.0, TipoVehiculo.ESCALERA, transportadoraExpress)
        vehiculo23 = Vehiculo("OPQ789", "ModeloW", 34500.00, 145.0, TipoVehiculo.VANS, transportadoraExpress)
        vehiculo24 = Vehiculo("RST012", "ModeloX", 25000.00, 120.0, TipoVehiculo.TAXI, transportadoraExpress)
        vehiculo25 = Vehiculo("UVW345", "ModeloY", 26000.00, 125.0, TipoVehiculo.BUS, transportadoraExpress)
        vehiculo26 = Vehiculo("LMN456", "ModeloZ", 33200.00, 125.0, TipoVehiculo.ESCALERA, transportadoraExpress)
        vehiculo27 = Vehiculo("OPQ789", "ModeloLÑ", 38500.00, 127.0, TipoVehiculo.VANS, transportadoraExpress)
        vehiculo28 = Vehiculo("RST012", "ModeloHJ", 27000.00, 137.0, TipoVehiculo.TAXI, transportadoraExpress)

        vehiculos3.extend([vehiculo21, vehiculo22, vehiculo23, vehiculo24, vehiculo25, vehiculo26, vehiculo27, vehiculo28])
        transportadoraExpress.setVehiculos(vehiculos3)

        # Vehículos para la transportadora4
        vehiculo31 = Vehiculo("MNO123", "ModeloEE", 16000.00, 125.0, TipoVehiculo.ESCALERA, transportadoraSegura)
        vehiculo32 = Vehiculo("PQR456", "ModeloFF", 17000.00, 130.0, TipoVehiculo.VANS, transportadoraSegura)
        vehiculo33 = Vehiculo("STU789", "ModeloGG", 18000.00, 135.0, TipoVehiculo.TAXI, transportadoraSegura)
        vehiculo34 = Vehiculo("VWX012", "ModeloHH", 19000.00, 140.0, TipoVehiculo.BUS, transportadoraSegura)
        vehiculo35 = Vehiculo("YZA345", "ModeloII", 20000.00, 145.0, TipoVehiculo.ESCALERA, transportadoraSegura)
        vehiculo36 = Vehiculo("JIS456", "ModeloFF1", 17800.00, 133.0, TipoVehiculo.VANS, transportadoraSegura)
        vehiculo37 = Vehiculo("KFD999", "ModeloGG2", 20100.00, 112.0, TipoVehiculo.TAXI, transportadoraSegura)
        vehiculo38 = Vehiculo("ÑÑÑ123", "ModeloHH3", 19600.00, 144.0, TipoVehiculo.BUS, transportadoraSegura)

        vehiculos4.extend([vehiculo31, vehiculo32, vehiculo33, vehiculo34, vehiculo35, vehiculo36, vehiculo37, vehiculo38])
        transportadoraSegura.setVehiculos(vehiculos4)

        # Vehículos para la transportadora5
        vehiculo41 = Vehiculo("QRS123", "ModeloOO", 26000.00, 145.0, TipoVehiculo.VANS, transportadoraGlobal)
        vehiculo42 = Vehiculo("TUV456", "ModeloPP", 27000.00, 120.0, TipoVehiculo.TAXI, transportadoraGlobal)
        vehiculo43 = Vehiculo("WXY789", "ModeloQQ", 28000.00, 125.0, TipoVehiculo.BUS, transportadoraGlobal)
        vehiculo44 = Vehiculo("ZAB012", "ModeloRR", 29000.00, 130.0, TipoVehiculo.ESCALERA, transportadoraGlobal)
        vehiculo45 = Vehiculo("CDE345", "ModeloSS", 30000.00, 135.0, TipoVehiculo.VANS, transportadoraGlobal)
        vehiculo46 = Vehiculo("ZXC283", "ModeloPPQ", 27600.00, 140.0, TipoVehiculo.TAXI, transportadoraGlobal)
        vehiculo47 = Vehiculo("OQI283", "ModeloQQF", 22000.00, 127.0, TipoVehiculo.BUS, transportadoraGlobal)
        vehiculo48 = Vehiculo("POO578", "ModeloRRT", 19000.00, 131.0, TipoVehiculo.ESCALERA, transportadoraGlobal)

        vehiculos5.extend([vehiculo41, vehiculo42, vehiculo43, vehiculo44, vehiculo45, vehiculo46, vehiculo47, vehiculo48])
        transportadoraGlobal.setVehiculos(vehiculos5)

        # Vehículos para la transportadora6
        vehiculo51 = Vehiculo("ABC234", "ModeloYY", 11500.00, 110.0, TipoVehiculo.TAXI, transportadoraLocal)
        vehiculo52 = Vehiculo("DEF567", "ModeloZZ", 12500.00, 120.0, TipoVehiculo.BUS, transportadoraLocal)
        vehiculo53 = Vehiculo("GHI890", "ModeloAAA", 13500.00, 130.0, TipoVehiculo.ESCALERA, transportadoraLocal)
        vehiculo54 = Vehiculo("JKL123", "ModeloBBB", 14500.00, 140.0, TipoVehiculo.VANS, transportadoraLocal)
        vehiculo55 = Vehiculo("MNO456", "ModeloCCC", 15500.00, 125.0, TipoVehiculo.TAXI, transportadoraLocal)
        vehiculo56 = Vehiculo("AWN672", "ModeloZZw", 14500.00, 127.0, TipoVehiculo.BUS, transportadoraLocal)
        vehiculo57 = Vehiculo("AKN210", "ModeloAAE", 19500.00, 139.0, TipoVehiculo.ESCALERA, transportadoraLocal)
        vehiculo58 = Vehiculo("VCC912", "ModeloBBJ", 17500.00, 125.0, TipoVehiculo.VANS, transportadoraLocal)

        vehiculos6.extend([vehiculo51, vehiculo52, vehiculo53, vehiculo54, vehiculo55, vehiculo56, vehiculo57, vehiculo58])
        transportadoraLocal.setVehiculos(vehiculos6)

        #CONDUCTORES
        conductores1 = []
        conductores2 = []
        conductores3 = []
        conductores4 = []
        conductores5 = []
        conductores6 = []

        # Conductores que tienen contrato con la transportadora1
        conductores1.extend([
            Conductor(1, 30, "Carlos Gómez", 'M', [], 5, 1500.0, True, vehiculo1, transportadoraRapida, [], [], 10, 200),
            Conductor(2, 28, "José Martínez", 'M', [], 4, 1400.0, True, vehiculo3, transportadoraRapida, [], [], 123, 190),
            Conductor(3, 35, "Luis Rodríguez", 'M', [], 7, 1600.0, True, vehiculo5, transportadoraRapida, [], [], 92, 210),
            Conductor(4, 32, "Miguel Sánchez", 'M', [], 6, 1550.0, True, vehiculo7, transportadoraRapida, [], [], 81, 220),
            Conductor(5, 29, "Juan Pérez", 'M', [], 4, 1450.0, True, vehiculo1, transportadoraRapida, [], [], 148, 180),
            Conductor(6, 31, "Pedro Fernández", 'M', [], 5, 1500.0, True, vehiculo2, transportadoraRapida, [], [], 106, 200),
            Conductor(7, 27, "Antonio López", 'M', [], 3, 1300.0, True, vehiculo7, transportadoraRapida, [], [], 120, 170),
            Conductor(8, 34, "Francisco García", 'M', [], 6, 1575.0, True, vehiculo8, transportadoraRapida, [], [], 299, 215),
            Conductor(9, 33, "Jorge Hernández", 'M', [], 7, 1620.0, True, vehiculo8, transportadoraRapida, [], [], 257, 230),
            Conductor(10, 29, "Alberto Ruiz", 'M', [], 4, 1460.0, True, vehiculo6, transportadoraRapida, [], [], 213, 190),
            Conductor(121, 40, "Cristiano Ronaldo", 'M', [], 7, 1760.0, True, vehiculo4, transportadoraRapida, [], [], 241, 263),
            Conductor(122, 35, "Leo Messi", 'M', [], 10, 1710.0, True, vehiculo2, transportadoraRapida, [], [], 155, 196)
        ])

        vehiculo1.asociarConductor(conductores1[0])
        vehiculo1.asociarConductor(conductores1[4])
        vehiculo2.asociarConductor(conductores1[5])
        vehiculo2.asociarConductor(conductores1[11])
        vehiculo3.asociarConductor(conductores1[1])
        vehiculo4.asociarConductor(conductores1[10])
        vehiculo5.asociarConductor(conductores1[2])
        vehiculo6.asociarConductor(conductores1[9])
        vehiculo7.asociarConductor(conductores1[3])
        vehiculo7.asociarConductor(conductores1[6])
        vehiculo8.asociarConductor(conductores1[7])
        vehiculo8.asociarConductor(conductores1[8])
        
        

        # Suponiendo que transportadora1 es una instancia de una clase con un método setConductores
        transportadoraRapida.setConductores(conductores1)

        # Conductores que tienen contrato con la transportadora2
        conductores2.extend([
            Conductor(21, 36, "Rubén Vargas", 'M', [], 8, 1700.0, True, vehiculo11, transportadoraEficiente, [], [], 213, 230),
            Conductor(22, 30, "Adrián Muñoz", 'M', [], 5, 1500.0, True, vehiculo11, transportadoraEficiente, [], [], 122, 200),
            Conductor(23, 29, "Santiago Reyes", 'M', [], 4, 1400.0, True, vehiculo12, transportadoraEficiente, [], [], 214, 190),
            Conductor(24, 37, "Sebastián Castillo", 'M', [], 9, 1750.0, True, vehiculo13, transportadoraEficiente, [], [], 310, 240),
            Conductor(25, 32, "Martín Rojas", 'M', [], 6, 1550.0, True, vehiculo13, transportadoraEficiente, [], [], 412, 210),
            Conductor(26, 31, "Iván Morales", 'M', [], 5, 1520.0, True, vehiculo14, transportadoraEficiente, [], [], 131, 220),
            Conductor(27, 30, "Tomás Herrera", 'M', [], 4, 1490.0, True, vehiculo15, transportadoraEficiente, [], [], 141, 180),
            Conductor(28, 38, "Enrique Romero", 'M', [], 10, 1800.0, True, vehiculo15, transportadoraEficiente, [], [], 153, 250),
            Conductor(29, 33, "Eduardo Morales", 'M', [], 6, 1570.0, True, vehiculo16, transportadoraEficiente, [], [], 123, 220),
            Conductor(30, 31, "Gabriel Paredes", 'M', [], 5, 1500.0, True, vehiculo17, transportadoraEficiente, [], [], 212, 210),
            Conductor(123, 38, "Mario Baloteli", 'M', [], 9, 1750.0, True, vehiculo17, transportadoraEficiente, [], [], 256, 244),
            Conductor(124, 33, "James Rodriguez", 'M', [], 8, 1200.0, True, vehiculo18, transportadoraEficiente, [], [], 175, 111)
        ])

        vehiculo11.asociarConductor(conductores2[0])
        vehiculo11.asociarConductor(conductores2[1])
        vehiculo12.asociarConductor(conductores2[2])
        vehiculo13.asociarConductor(conductores2[3])
        vehiculo13.asociarConductor(conductores2[4])
        vehiculo14.asociarConductor(conductores2[5])
        vehiculo15.asociarConductor(conductores2[6])
        vehiculo15.asociarConductor(conductores2[7])
        vehiculo16.asociarConductor(conductores2[8])
        vehiculo17.asociarConductor(conductores2[9])
        vehiculo17.asociarConductor(conductores2[10])
        vehiculo18.asociarConductor(conductores2[11])

        # Suponiendo que transportadora2 es una instancia de una clase con un método setConductores
        transportadoraEficiente.setConductores(conductores2)

        # Conductores que tienen contrato con la transportadora3
        conductores3.extend([
            Conductor(41, 29, "Álvaro Soto", 'M', [], 4, 1450.0, True, vehiculo21, transportadoraExpress, [], [], 313, 185),
            Conductor(42, 31, "Carlos Guzmán", 'M', [], 5, 1500.0, True, vehiculo22, transportadoraExpress, [], [], 111, 195),
            Conductor(43, 34, "Luis Ortega", 'M', [], 7, 1650.0, True, vehiculo22, transportadoraExpress, [], [], 121, 210),
            Conductor(44, 28, "Marcelo Fernández", 'M', [], 4, 1400.0, True, vehiculo23, transportadoraExpress, [], [], 414, 190),
            Conductor(45, 33, "Antonio Vargas", 'M', [], 6, 1550.0, True, vehiculo24, transportadoraExpress, [], [], 123, 220),
            Conductor(46, 30, "Ricardo Ruiz", 'M', [], 5, 1480.0, True, vehiculo24, transportadoraExpress, [], [], 112, 210),
            Conductor(47, 32, "Roberto Pérez", 'M', [], 6, 1600.0, True, vehiculo25, transportadoraExpress, [], [], 121, 225),
            Conductor(48, 27, "Javier Romero", 'M', [], 4, 1350.0, True, vehiculo26, transportadoraExpress, [], [], 135, 185),
            Conductor(49, 36, "Felipe Calderón", 'M', [], 8, 1700.0, True, vehiculo26, transportadoraExpress, [], [], 101, 240),
            Conductor(50, 31, "Julio Martínez", 'M', [], 5, 1500.0, True, vehiculo27, transportadoraExpress, [], [], 131, 215),
            Conductor(125, 36, "Radamel Falcao", 'M', [], 9, 1450.0, True, vehiculo28, transportadoraExpress, [], [], 14, 196),
            Conductor(126, 37, "Dorlan Pabon", 'M', [], 8, 1100.0, True, vehiculo28, transportadoraExpress, [], [], 88, 188)
        ])

        vehiculo21.asociarConductor(conductores3[0])
        vehiculo22.asociarConductor(conductores3[1])
        vehiculo22.asociarConductor(conductores3[2])
        vehiculo23.asociarConductor(conductores3[3])
        vehiculo24.asociarConductor(conductores3[4])
        vehiculo24.asociarConductor(conductores3[5])
        vehiculo25.asociarConductor(conductores3[6])
        vehiculo26.asociarConductor(conductores3[7])
        vehiculo26.asociarConductor(conductores3[8])
        vehiculo27.asociarConductor(conductores3[9])
        vehiculo28.asociarConductor(conductores3[10])
        vehiculo28.asociarConductor(conductores3[11])

        # Suponiendo que transportadora3 es una instancia de una clase con un método setConductores
        transportadoraExpress.setConductores(conductores3)

        # Conductores que tienen contrato con la transportadora4
        conductores4.extend([
            Conductor(61, 29, "Mauricio Álvarez", 'M', [], 4, 1450.0, True, vehiculo31, transportadoraSegura, [], [], 123, 190),
            Conductor(62, 32, "Gabriel Herrera", 'M', [], 6, 1500.0, True, vehiculo31, transportadoraSegura, [], [], 131, 205),
            Conductor(63, 30, "Eduardo Rivas", 'M', [], 5, 1550.0, True, vehiculo32, transportadoraSegura, [], [], 113, 220),
            Conductor(64, 34, "Ricardo Beltrán", 'M', [], 7, 1600.0, True, vehiculo33, transportadoraSegura, [], [], 124, 225),
            Conductor(65, 28, "Alejandro Guzmán", 'M', [], 4, 1400.0, True, vehiculo33, transportadoraSegura, [], [], 141, 200),
            Conductor(66, 31, "Fabián López", 'M', [], 5, 1500.0, True, vehiculo34, transportadoraSegura, [], [], 11, 210),
            Conductor(67, 33, "Héctor Cordero", 'M', [], 6, 1550.0, True, vehiculo35, transportadoraSegura, [], [], 12, 220),
            Conductor(68, 36, "Manuel Vargas", 'M', [], 8, 1700.0, True, vehiculo35, transportadoraSegura, [], [], 10, 240),
            Conductor(69, 30, "Luis Cuenca", 'M', [], 5, 1480.0, True, vehiculo36, transportadoraSegura, [], [], 14, 195),
            Conductor(70, 32, "Oscar Mendoza", 'M', [], 6, 1550.0, True, vehiculo37, transportadoraSegura, [], [], 13, 210),
            Conductor(127, 33, "Neymar Junior", 'M', [], 8, 1650.0, True, vehiculo37, transportadoraSegura, [], [], 89, 110),
            Conductor(128, 30, "Daniel Alves", 'M', [], 5, 1900.0, True, vehiculo38, transportadoraSegura, [], [], 155, 598)
        ])

        vehiculo31.asociarConductor(conductores4[0])
        vehiculo31.asociarConductor(conductores4[1])
        vehiculo32.asociarConductor(conductores4[2])
        vehiculo33.asociarConductor(conductores4[3])
        vehiculo33.asociarConductor(conductores4[4])
        vehiculo34.asociarConductor(conductores4[5])
        vehiculo35.asociarConductor(conductores4[6])
        vehiculo35.asociarConductor(conductores4[7])
        vehiculo36.asociarConductor(conductores4[8])
        vehiculo37.asociarConductor(conductores4[9])
        vehiculo37.asociarConductor(conductores4[10])
        vehiculo38.asociarConductor(conductores4[11])

        

        # Suponiendo que transportadora4 es una instancia de una clase con un método setConductores
        transportadoraSegura.setConductores(conductores4)

        #Conductores que tienen contrato con la transportadora5
        
        
        conductores5.extend([
            Conductor(81, 30, "Jorge Sandoval", 'M', [], 5, 1550.0, True, vehiculo41, transportadoraGlobal, [], [], 123, 210),
            Conductor(82, 32, "Sergio Montoya", 'M', [], 6, 1600.0, True, vehiculo42, transportadoraGlobal, [], [], 135, 220),
            Conductor(83, 31, "Ricardo Morales", 'M', [], 5, 1500.0, True, vehiculo42, transportadoraGlobal, [], [], 113, 215),
            Conductor(84, 29, "Mauricio Valenzuela", 'M', [], 4, 1450.0, True, vehiculo43, transportadoraGlobal, [], [], 141, 200),
            Conductor(85, 35, "Héctor Mejía", 'M', [], 7, 1650.0, True, vehiculo44, transportadoraGlobal, [], [], 122, 230),
            Conductor(86, 30, "Fernando Arrieta", 'M', [], 5, 1520.0, True, vehiculo44, transportadoraGlobal, [], [], 133, 210),
            Conductor(87, 37, "Mario Cordero", 'M', [], 9, 1750.0, True, vehiculo45, transportadoraGlobal, [], [], 154, 240),
            Conductor(88, 33, "Javier Hernández", 'M', [], 6, 1570.0, True, vehiculo46, transportadoraGlobal, [], [], 125, 225),
            Conductor(89, 32, "Luis Palacios", 'M', [], 6, 1600.0, True, vehiculo46, transportadoraGlobal, [], [], 114, 220),
            Conductor(90, 34, "Ángel Peña", 'M', [], 7, 1650.0, True, vehiculo47, transportadoraGlobal, [], [], 101, 230),
            Conductor(129, 37, "Kevin Bruyne", 'M', [], 9, 1150.0, True, vehiculo48, transportadoraGlobal, [], [], 99, 288),
            Conductor(130, 41, "Robert Lewandowski", 'M', [], 5, 1660.0, True, vehiculo48, transportadoraGlobal, [], [], 89, 201)
        ])

        vehiculo41.asociarConductor(conductores5[0])
        vehiculo42.asociarConductor(conductores5[1])
        vehiculo42.asociarConductor(conductores5[2])
        vehiculo43.asociarConductor(conductores5[3])
        vehiculo44.asociarConductor(conductores5[4])
        vehiculo44.asociarConductor(conductores5[5])
        vehiculo45.asociarConductor(conductores5[6])
        vehiculo46.asociarConductor(conductores5[7])
        vehiculo46.asociarConductor(conductores5[8])
        vehiculo47.asociarConductor(conductores5[9])
        vehiculo48.asociarConductor(conductores5[10])
        vehiculo48.asociarConductor(conductores5[11])



        # Suponiendo que transportadora5 es una instancia de una clase con un método setConductores
        transportadoraGlobal.setConductores(conductores5)

        conductores6.extend([
            Conductor(101, 30, "Héctor Jiménez", 'M', [], 5, 1550.0, True, vehiculo51, transportadoraLocal, [], [], 123, 210),
            Conductor(102, 32, "Santiago Díaz", 'M', [], 6, 1600.0, True, vehiculo51, transportadoraLocal, [], [], 134, 225),
            Conductor(103, 31, "Gabriel Andrade", 'M', [], 5, 1500.0, True, vehiculo52, transportadoraLocal, [], [], 211, 215),
            Conductor(104, 29, "Alejandro Rodríguez", 'M', [], 4, 1450.0, True, vehiculo53, transportadoraLocal, [], [], 134, 200),
            Conductor(105, 35, "Mauricio Ortega", 'M', [], 7, 1650.0, True, vehiculo53, transportadoraLocal, [], [], 112, 230),
            Conductor(106, 30, "Ricardo Vargas", 'M', [], 5, 1520.0, True, vehiculo54, transportadoraLocal, [], [], 513, 210),
            Conductor(107, 37, "Javier Sánchez", 'M', [], 9, 1750.0, True, vehiculo55, transportadoraLocal, [], [], 315, 240),
            Conductor(108, 33, "Luis Carrillo", 'M', [], 6, 1570.0, True, vehiculo55, transportadoraLocal, [], [], 122, 220),
            Conductor(109, 32, "Carlos Martínez", 'M', [], 6, 1600.0, True, vehiculo56, transportadoraLocal, [], [], 90, 225),
            Conductor(110, 34, "Óscar Morales", 'M', [], 7, 1650.0, True, vehiculo57, transportadoraLocal, [], [], 10, 230),
            Conductor(131, 39, "Toni Kross", 'M', [], 6, 1850.0, True, vehiculo57, transportadoraLocal, [], [], 75, 54),
            Conductor(132, 35, "Kilian Mbape", 'M', [], 7, 1650.0, True, vehiculo58, transportadoraLocal, [], [], 112, 230)
        ])

        vehiculo51.asociarConductor(conductores6[0])
        vehiculo51.asociarConductor(conductores6[1])
        vehiculo52.asociarConductor(conductores6[2])
        vehiculo53.asociarConductor(conductores6[3])
        vehiculo53.asociarConductor(conductores6[4])
        vehiculo54.asociarConductor(conductores6[5])
        vehiculo55.asociarConductor(conductores6[6])
        vehiculo55.asociarConductor(conductores6[7])
        vehiculo56.asociarConductor(conductores6[8])
        vehiculo57.asociarConductor(conductores6[9])
        vehiculo57.asociarConductor(conductores6[10])
        vehiculo58.asociarConductor(conductores6[11])

        # Suponiendo que transportadora6 es una instancia de una clase con un método setConductores
        transportadoraLocal.setConductores(conductores6)

        #Listas de conductores que se agregaran a las transportadoras como registrados(no contratados)
        
        conductoresRegistrados1 = []
        conductoresRegistrados2 = []
        conductoresRegistrados3 = []
        conductoresRegistrados4 = []
        conductoresRegistrados5 = []
        conductoresRegistrados6 = []

        #Conductores que se registraran(no estan contratados) en la transportadora1

        conductoresRegistrados1.extend([
            Conductor(11, 28, "Fernando Castro", 'M', [], 5, 1490.0, False, None, transportadoraRapida, [], [], 11, 200),
            Conductor(12, 36, "Raúl Ramírez", 'M', [], 7, 1650.0, True, None, transportadoraRapida, [], [], 9, 210),
            Conductor(13, 31, "Manuel Torres", 'M', [], 6, 1580.0, False, None, transportadoraRapida, [], [], 8, 220),
            Conductor(14, 30, "Héctor Gil", 'M', [], 5, 1520.0, True, None, transportadoraRapida, [], [], 10, 200),
            Conductor(15, 29, "Vicente Díaz", 'M', [], 4, 1450.0, True, None, transportadoraRapida, [], [], 14, 180),
            Conductor(16, 32, "Ángel Ramos", 'M', [], 6, 1550.0, False, None, transportadoraRapida, [], [], 12, 210),
            Conductor(17, 30, "Javier Navarro", 'M', [], 5, 1480.0, True, None, transportadoraRapida, [], [], 9, 220),
            Conductor(18, 34, "Mario Ortiz", 'M', [], 6, 1570.0, True, None, transportadoraRapida, [], [], 8, 215),
            Conductor(19, 29, "Andrés Flores", 'M', [], 1, 1420.0, True, None, transportadoraRapida, [], [], 10, 200),
            Conductor(20, 35, "Daniel Maldonado", 'M', [], 7, 1610.0, False, None, transportadoraRapida, [], [], 11, 230)
        ])

        transportadoraRapida.setConductoresRegistrados(conductoresRegistrados1)

        #Conductores que se registraran(no estan contratados) en la transportadora2

        conductoresRegistrados2.extend([
            Conductor(31, 28, "Emilio Duarte", 'M', [], 4, 1450.0, True, None, transportadoraEficiente, [], [], 14, 190),
            Conductor(32, 35, "Felipe Soto", 'M', [], 7, 1650.0, True, None, transportadoraEficiente, [], [], 10, 230),
            Conductor(33, 29, "Gonzalo Montalvo", 'M', [], 5, 1480.0, True, None, transportadoraEficiente, [], [], 11, 200),
            Conductor(34, 36, "Hugo Escobar", 'M', [], 5, 1720.0, False, None, transportadoraEficiente, [], [], 12, 240),
            Conductor(35, 32, "Diego Olivares", 'M', [], 4, 1580.0, True, None, transportadoraEficiente, [], [], 13, 220),
            Conductor(36, 34, "Iván Castañeda", 'M', [], 7, 1600.0, True, None, transportadoraEficiente, [], [], 11, 230),
            Conductor(37, 30, "Joaquín Salinas", 'M', [], 5, 1500.0, False, None, transportadoraEficiente, [], [], 14, 200),
            Conductor(38, 37, "Ismael Peña", 'M', [], 9, 1750.0, True, None, transportadoraEficiente, [], [], 15, 240),
            Conductor(39, 33, "Rafael Marín", 'M', [], 6, 1570.0, True, None, transportadoraEficiente, [], [], 12, 220),
            Conductor(40, 31, "Alejandro Campos", 'M', [], 2, 1490.0, True, None, transportadoraEficiente, [], [], 13, 210)
        ])

        transportadoraEficiente.setConductoresRegistrados(conductoresRegistrados2)

        #Conductores que se registraran(no estan contratados) en la transportadora3

        conductoresRegistrados3.extend([
            Conductor(51, 29, "Héctor Villalobos", 'M', [], 10, 1450.0, False, None, transportadoraExpress, [], [], 14, 200),
            Conductor(52, 34, "Luis González", 'M', [], 7, 1600.0, True, None, transportadoraExpress, [], [], 12, 225),
            Conductor(53, 30, "Samuel Morales", 'M', [], 5, 1550.0, True, None, transportadoraExpress, [], [], 11, 210),
            Conductor(54, 37, "Victor Gómez", 'M', [], 9, 1750.0, True, None, transportadoraExpress, [], [], 15, 240),
            Conductor(55, 33, "Óscar Sandoval", 'M', [], 2, 1600.0, True, None, transportadoraExpress, [], [], 12, 225),
            Conductor(56, 32, "Mauricio Ramírez", 'M', [], 3, 1550.0, True, None, transportadoraExpress, [], [], 13, 220),
            Conductor(57, 35, "Fernando Vega", 'M', [], 7, 1650.0, True, None, transportadoraExpress, [], [], 10, 230),
            Conductor(58, 31, "Emmanuel Ruiz", 'M', [], 5, 1500.0, False, None, transportadoraExpress, [], [], 14, 200),
            Conductor(59, 28, "Jorge Silva", 'M', [], 4, 1400.0, True, None, transportadoraExpress, [], [], 15, 190),
            Conductor(60, 30, "Esteban Cruz", 'M', [], 5, 1500.0, True, None, transportadoraExpress, [], [], 13, 215)
        ])

        transportadoraExpress.setConductoresRegistrados(conductoresRegistrados3)

        #Conductores que se registraran(no estan contratados) en la transportadora4

        conductoresRegistrados4.extend([
            Conductor(71, 31, "Luis Silva", 'M', [], 5, 1500.0, True, None, transportadoraSegura, [], [], 12, 220),
            Conductor(72, 29, "Carlos Martínez", 'M', [], 4, 1450.0, True, None, transportadoraSegura, [], [], 13, 200),
            Conductor(73, 34, "Felipe Díaz", 'M', [], 7, 1600.0, True, None, transportadoraSegura, [], [], 12, 225),
            Conductor(74, 30, "Javier López", 'M', [], 5, 1550.0, False, None, transportadoraSegura, [], [], 14, 210),
            Conductor(75, 36, "Mario Castro", 'M', [], 1, 1700.0, True, None, transportadoraSegura, [], [], 10, 240),
            Conductor(76, 32, "Fernando Soto", 'M', [], 6, 1600.0, True, None, transportadoraSegura, [], [], 13, 220),
            Conductor(77, 33, "Adrián Díaz", 'M', [], 6, 1570.0, True, None, transportadoraSegura, [], [], 12, 225),
            Conductor(78, 28, "Ramiro Aguirre", 'M', [], 4, 1400.0, True, None, transportadoraSegura, [], [], 14, 190),
            Conductor(79, 35, "Mauricio Araya", 'M', [], 7, 1650.0, False, None, transportadoraSegura, [], [], 11, 230),
            Conductor(80, 31, "Luis Hernández", 'M', [], 5, 1500.0, True, None, transportadoraSegura, [], [], 14, 205)
        ])

        transportadoraSegura.setConductoresRegistrados(conductoresRegistrados4)

        #Conductores que se registraran(no estan contratados) en la transportadora5

        conductoresRegistrados5.extend([
            Conductor(91, 31, "Carlos Ramírez", 'M', [], 5, 1500.0, True, None,  transportadoraGlobal, [], [], 12, 210),
            Conductor(92, 29, "Andrés Soto", 'M', [], 4, 1400.0, True, None,  transportadoraGlobal, [], [], 14, 190),
            Conductor(93, 33, "Jorge Morales", 'M', [], 6, 1550.0, False, None,  transportadoraGlobal, [], [], 13, 215),
            Conductor(94, 30, "Oscar Hernández", 'M', [], 5, 1500.0, True, None,  transportadoraGlobal, [], [], 14, 205),
            Conductor(95, 36, "Luis García", 'M', [], 8, 1700.0, True, None,  transportadoraGlobal, [], [], 10, 240),
            Conductor(96, 32, "Samuel Lozano", 'M', [], 1, 1600.0, True, None,  transportadoraGlobal, [], [], 11, 220),
            Conductor(97, 31, "Ricardo Nieto", 'M', [], 5, 1500.0, True, None,  transportadoraGlobal, [], [], 13, 210),
            Conductor(98, 28, "Felipe Castaño", 'M', [], 4, 1400.0, True, None,  transportadoraGlobal, [], [], 15, 195),
            Conductor(99, 35, "Manuel Vargas", 'M', [], 7, 1650.0, True, None,  transportadoraGlobal, [], [], 10, 230),
            Conductor(100, 33, "Eduardo Peña", 'M', [], 2, 1550.0, True, None,  transportadoraGlobal, [], [], 12, 215)
        ])

        transportadoraGlobal.setConductoresRegistrados(conductoresRegistrados5)

        #Conductores que se registraran(no estan contratados) en la transportadora6

        conductoresRegistrados6.extend([
            Conductor(111, 31, "Mario Ruiz", 'M', [], 4, 1500.0, True, None, transportadoraLocal, [], [], 12, 215),
            Conductor(112, 29, "Ramiro Guzmán", 'M', [], 1, 1400.0, True, None, transportadoraLocal, [], [], 14, 190),
            Conductor(113, 33, "Fernando Pérez", 'M', [], 6, 1550.0, True, None, transportadoraLocal, [], [], 13, 220),
            Conductor(114, 30, "Álvaro Díaz", 'M', [], 5, 1500.0, True, None, transportadoraLocal, [], [], 14, 205),
            Conductor(115, 36, "Jorge Calderón", 'M', [], 8, 1700.0, False, None, transportadoraLocal, [], [], 10, 240),
            Conductor(116, 32, "Héctor Mendoza", 'M', [], 6, 1600.0, True, None, transportadoraLocal, [], [], 11, 225),
            Conductor(117, 31, "Esteban Cordero", 'M', [], 5, 1500.0, True, None, transportadoraLocal, [], [], 13, 210),
            Conductor(118, 28, "Ricardo Silva", 'M', [], 4, 1400.0, True, None, transportadoraLocal, [], [], 15, 195),
            Conductor(119, 35, "José Martínez", 'M', [], 7, 1650.0, False, None, transportadoraLocal, [], [], 10, 230),
            Conductor(120, 33, "Óscar Guerrero", 'M', [], 6, 1550.0, True, None, transportadoraLocal, [], [], 12, 215)
        ])

        transportadoraLocal.setConductoresRegistrados(conductoresRegistrados6)




        #Pasajeros de la Terminal
        pasajerosTerminal = [
            #Pasajeros ESTUDIANTE - 80
            Pasajero(TipoPasajero.ESTUDIANTE, 1002, 19, "Ana García"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1003, 20, "Luis Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1004, 21, "María López"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1005, 22, "Carlos Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1006, 18, "Laura Sánchez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1007, 19, "José Rodríguez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1008, 20, "Isabel Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1009, 21, "Antonio Díaz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1010, 22, "Carmen Pérez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1011, 18, "Manuel Ruiz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1012, 19, "Marta Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1013, 20, "Javier Morales"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1014, 21, "Paula Castro"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1015, 22, "Francisco Ortega"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1016, 18, "Sara Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1017, 19, "Pedro Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1018, 20, "Victoria Moreno"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1019, 21, "David Torres"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1020, 22, "Elena Romero"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1021, 18, "Rafael Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1022, 19, "Nerea Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1023, 20, "Ángel Hernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1024, 21, "Sofía García"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1025, 22, "Mario Sánchez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1026, 18, "Beatriz López"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1027, 19, "Guillermo Morales"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1028, 20, "Natalia Díaz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1029, 21, "Álvaro Rodríguez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1030, 22, "Inés Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1031, 18, "Raúl Sánchez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1032, 19, "Carmen Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1033, 20, "José Antonio Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1034, 21, "Laura Rodríguez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1035, 22, "Alejandro López"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1036, 18, "Sonia Pérez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1037, 19, "Cristian García"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1038, 20, "Andrea Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1039, 21, "Jorge Rodríguez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1040, 22, "Silvia Moreno"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1041, 18, "Luis Sánchez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1042, 19, "Marina Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1043, 20, "Rosa Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1044, 21, "Felipe Pérez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1045, 22, "Clara López"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1046, 18, "Esteban Ruiz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1047, 19, "Mónica Romero"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1048, 20, "Luis Ángel Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1049, 21, "Nerea Ruiz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1050, 22, "Óscar Sánchez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1051, 18, "Belén González"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1052, 19, "Antonio Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1053, 20, "Patricia Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1054, 21, "Alejandro Díaz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1055, 22, "Julia Torres"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1056, 18, "Mario López"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1057, 19, "Álvaro Pérez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1058, 20, "Beatriz Rodríguez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1059, 21, "Miguel Ángel Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1060, 22, "Lola Sánchez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1061, 18, "Ricardo Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1062, 19, "Rosa María Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1063, 20, "Cristina López"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1064, 21, "Juan Antonio Ruiz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1065, 22, "Marta García"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1066, 18, "Jesús Morales"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1067, 19, "Lorena Romero"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1068, 20, "Javier Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1069, 21, "Elena Rodríguez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1070, 22, "Guadalupe Sánchez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1071, 18, "Félix Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1072, 19, "Ana Isabel Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1073, 20, "Mario Hernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1074, 21, "Marina López"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1075, 22, "Pablo Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1076, 18, "Carlos Gómez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1077, 19, "Sara Martínez"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1078, 20, "Raúl Fernández"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1079, 21, "Lorena Díaz"),
            Pasajero(TipoPasajero.ESTUDIANTE, 1080, 22, "Antonio López"),
            #Pasajeros VIP - 80
            Pasajero(TipoPasajero.VIP, 2001, 25, "Juan Pérez"),
            Pasajero(TipoPasajero.VIP, 2002, 30, "María González"),
            Pasajero(TipoPasajero.VIP, 2003, 28, "Carlos Sánchez"),
            Pasajero(TipoPasajero.VIP, 2004, 32, "Ana Martínez"),
            Pasajero(TipoPasajero.VIP, 2005, 29, "Luis Rodríguez"),
            Pasajero(TipoPasajero.VIP, 2006, 35, "Sofía Fernández"),
            Pasajero(TipoPasajero.VIP, 2007, 27, "Jorge Ramírez"),
            Pasajero(TipoPasajero.VIP, 2008, 33, "Patricia López"),
            Pasajero(TipoPasajero.VIP, 2009, 26, "Diego Morales"),
            Pasajero(TipoPasajero.VIP, 2010, 31, "Laura Torres"),
            Pasajero(TipoPasajero.VIP, 2011, 24, "Miguel Hernández"),
            Pasajero(TipoPasajero.VIP, 2012, 23, "Daniela Romero"),
            Pasajero(TipoPasajero.VIP, 2013, 22, "Fernando Castro"),
            Pasajero(TipoPasajero.VIP, 2014, 32, "Lucía Delgado"),
            Pasajero(TipoPasajero.VIP, 2015, 21, "Andrés Vega"),
            Pasajero(TipoPasajero.VIP, 2016, 29, "Valentina Ortiz"),
            Pasajero(TipoPasajero.VIP, 2017, 28, "Ricardo Flores"),
            Pasajero(TipoPasajero.VIP, 2018, 26, "Camila Ruiz"),
            Pasajero(TipoPasajero.VIP, 2019, 35, "Antonio Mendoza"),
            Pasajero(TipoPasajero.VIP, 2020, 33, "Gabriela Navarro"),
            Pasajero(TipoPasajero.VIP, 2021, 26, "Santiago Guzmán"),
            Pasajero(TipoPasajero.VIP, 2022, 34, "Isabel Ríos"),
            Pasajero(TipoPasajero.VIP, 2023, 29, "Manuel Cruz"),
            Pasajero(TipoPasajero.VIP, 2024, 28, "Rosa Paredes"),
            Pasajero(TipoPasajero.VIP, 2025, 32, "Cristian Ponce"),
            Pasajero(TipoPasajero.VIP, 2026, 30, "Elena Reyes"),
            Pasajero(TipoPasajero.VIP, 2027, 31, "Pablo Cordero"),
            Pasajero(TipoPasajero.VIP, 2028, 33, "Teresa Salazar"),
            Pasajero(TipoPasajero.VIP, 2029, 35, "David Márquez"),
            Pasajero(TipoPasajero.VIP, 2030, 29, "Silvia Palacios"),
            Pasajero(TipoPasajero.VIP, 2031, 27, "Raúl Aguirre"),
            Pasajero(TipoPasajero.VIP, 2032, 30, "Claudia Blanco"),
            Pasajero(TipoPasajero.VIP, 2033, 34, "Sebastián Serrano"),
            Pasajero(TipoPasajero.VIP, 2034, 28, "Mónica Ibáñez"),
            Pasajero(TipoPasajero.VIP, 2035, 31, "Rodrigo Herrera"),
            Pasajero(TipoPasajero.VIP, 2036, 32, "Paula Gallardo"),
            Pasajero(TipoPasajero.VIP, 2037, 29, "Tomás Rivero"),
            Pasajero(TipoPasajero.VIP, 2038, 33, "Natalia Cabrera"),
            Pasajero(TipoPasajero.VIP, 2039, 26, "Francisco Luna"),
            Pasajero(TipoPasajero.VIP, 2040, 27, "Diana Medina"),
            Pasajero(TipoPasajero.VIP, 2041, 30, "Álvaro Peña"),
            Pasajero(TipoPasajero.VIP, 2042, 34, "Carmen Castro"),
            Pasajero(TipoPasajero.VIP, 2043, 32, "Eduardo Escobar"),
            Pasajero(TipoPasajero.VIP, 2044, 35, "Julia Muñoz"),
            Pasajero(TipoPasajero.VIP, 2045, 28, "Héctor León"),
            Pasajero(TipoPasajero.VIP, 2046, 29, "Irene Carrillo"),
            Pasajero(TipoPasajero.VIP, 2047, 31, "Emilio Peña"),
            Pasajero(TipoPasajero.VIP, 2048, 34, "Marta Campos"),
            Pasajero(TipoPasajero.VIP, 2049, 32, "Adrián Lara"),
            Pasajero(TipoPasajero.VIP, 2050, 26, "Sara Núñez"),
            Pasajero(TipoPasajero.VIP, 2051, 33, "Javier Fuentes"),
            Pasajero(TipoPasajero.VIP, 2052, 30, "Victoria Bravo"),
            Pasajero(TipoPasajero.VIP, 2053, 35, "Rafael Mora"),
            Pasajero(TipoPasajero.VIP, 2054, 29, "Liliana Fuentes"),
            Pasajero(TipoPasajero.VIP, 2055, 27, "Fabián Vázquez"),
            Pasajero(TipoPasajero.VIP, 2056, 31, "Lorena Paredes"),
            Pasajero(TipoPasajero.VIP, 2057, 32, "Ángel Soto"),
            Pasajero(TipoPasajero.VIP, 2058, 28, "Rebeca Duarte"),
            Pasajero(TipoPasajero.VIP, 2059, 26, "Guillermo Solís"),
            Pasajero(TipoPasajero.VIP, 2060, 33, "Natalia Ramos"),
            Pasajero(TipoPasajero.VIP, 2061, 34, "José Olivares"),
            Pasajero(TipoPasajero.VIP, 2062, 31, "Alicia Valencia"),
            Pasajero(TipoPasajero.VIP, 2063, 30, "Ignacio Bautista"),
            Pasajero(TipoPasajero.VIP, 2064, 28, "Rocío Cortés"),
            Pasajero(TipoPasajero.VIP, 2065, 35, "Víctor Castro"),
            Pasajero(TipoPasajero.VIP, 2066, 26, "Marcela García"),
            Pasajero(TipoPasajero.VIP, 2067, 29, "Enrique Vargas"),
            Pasajero(TipoPasajero.VIP, 2068, 33, "Verónica Castaño"),
            Pasajero(TipoPasajero.VIP, 2069, 31, "Raquel Parra"),
            Pasajero(TipoPasajero.VIP, 2070, 27, "Mario Arroyo"),
            Pasajero(TipoPasajero.VIP, 2071, 35, "Sonia Zamora"),
            Pasajero(TipoPasajero.VIP, 2072, 30, "Felipe Escamilla"),
            Pasajero(TipoPasajero.VIP, 2073, 32, "Marisol Andrade"),
            Pasajero(TipoPasajero.VIP, 2074, 28, "Hugo Villalobos"),
            Pasajero(TipoPasajero.VIP, 2075, 33, "Antonia Ramírez"),
            Pasajero(TipoPasajero.VIP, 2076, 29, "Roberto Ávila"),
            Pasajero(TipoPasajero.VIP, 2077, 27, "Ruth Muñoz"),
            Pasajero(TipoPasajero.VIP, 2078, 34, "Alfonso Herrera"),
            Pasajero(TipoPasajero.VIP, 2079, 30, "Lidia Salinas"),
            Pasajero(TipoPasajero.VIP, 2080, 28, "Esteban Duarte"),
            #Pasajeros REGULAR - 100
            Pasajero(TipoPasajero.REGULAR, 3001, 28, "Carlos Gómez"),
            Pasajero(TipoPasajero.REGULAR, 3002, 32, "Ana Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3003, 29, "Luis Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3004, 31, "María Rodríguez"),
            Pasajero(TipoPasajero.REGULAR, 3005, 27, "Antonio Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3006, 30, "Isabel García"),
            Pasajero(TipoPasajero.REGULAR, 3007, 33, "José González"),
            Pasajero(TipoPasajero.REGULAR, 3008, 28, "Laura López"),
            Pasajero(TipoPasajero.REGULAR, 3009, 35, "Manuel Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3010, 26, "Carmen Díaz"),
            Pasajero(TipoPasajero.REGULAR, 3011, 30, "Francisco Romero"),
            Pasajero(TipoPasajero.REGULAR, 3012, 34, "Paula Ortega"),
            Pasajero(TipoPasajero.REGULAR, 3013, 29, "David Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3014, 27, "Clara Morales"),
            Pasajero(TipoPasajero.REGULAR, 3015, 32, "Rafael Ruiz"),
            Pasajero(TipoPasajero.REGULAR, 3016, 33, "Sofía Hernández"),
            Pasajero(TipoPasajero.REGULAR, 3017, 28, "Ángel Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3018, 31, "Marina Gómez"),
            Pasajero(TipoPasajero.REGULAR, 3019, 34, "Felipe Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3020, 26, "Elena García"),
            Pasajero(TipoPasajero.REGULAR, 3021, 30, "Óscar Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3022, 29, "Javier Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3023, 35, "Marta Rodríguez"),
            Pasajero(TipoPasajero.REGULAR, 3024, 32, "Pedro López"),
            Pasajero(TipoPasajero.REGULAR, 3025, 33, "Beatriz Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3026, 28, "Luis González"),
            Pasajero(TipoPasajero.REGULAR, 3027, 31, "Silvia Moreno"),
            Pasajero(TipoPasajero.REGULAR, 3028, 29, "Raúl Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3029, 30, "Mónica Díaz"),
            Pasajero(TipoPasajero.REGULAR, 3030, 27, "Víctor Ruiz"),
            Pasajero(TipoPasajero.REGULAR, 3031, 32, "Lucía Rodríguez"),
            Pasajero(TipoPasajero.REGULAR, 3032, 34, "Antonio Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3033, 35, "Patricia López"),
            Pasajero(TipoPasajero.REGULAR, 3034, 28, "Jesús Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3035, 30, "Isabel Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3036, 29, "Manuel Rodríguez"),
            Pasajero(TipoPasajero.REGULAR, 3037, 33, "Alicia Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3038, 31, "Carlos Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3039, 32, "Laura Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3040, 34, "Álvaro Gómez"),
            Pasajero(TipoPasajero.REGULAR, 3041, 28, "Sonia Ruiz"),
            Pasajero(TipoPasajero.REGULAR, 3042, 35, "José Antonio Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3043, 27, "Marta González"),
            Pasajero(TipoPasajero.REGULAR, 3044, 30, "Francisco Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3045, 29, "Clara Díaz"),
            Pasajero(TipoPasajero.REGULAR, 3046, 33, "David López"),
            Pasajero(TipoPasajero.REGULAR, 3047, 34, "Ana Romero"),
            Pasajero(TipoPasajero.REGULAR, 3048, 28, "Rosa Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3049, 31, "Antonio Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3050, 32, "Silvia Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3051, 27, "Óscar Gómez"),
            Pasajero(TipoPasajero.REGULAR, 3052, 29, "María Moreno"),
            Pasajero(TipoPasajero.REGULAR, 3053, 33, "Luis Hernández"),
            Pasajero(TipoPasajero.REGULAR, 3054, 35, "Patricia Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3055, 30, "Carlos Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3056, 28, "Mónica Gómez"),
            Pasajero(TipoPasajero.REGULAR, 3057, 34, "Pedro Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3058, 29, "Marta Rodríguez"),
            Pasajero(TipoPasajero.REGULAR, 3059, 32, "Ángel Moreno"),
            Pasajero(TipoPasajero.REGULAR, 3060, 31, "Ana Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3061, 33, "Víctor López"),
            Pasajero(TipoPasajero.REGULAR, 3062, 27, "Laura García"),
            Pasajero(TipoPasajero.REGULAR, 3063, 30, "Cristina Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3064, 29, "Javier González"),
            Pasajero(TipoPasajero.REGULAR, 3065, 28, "Felipe Díaz"),
            Pasajero(TipoPasajero.REGULAR, 3066, 34, "Nerea Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3067, 32, "Carlos Romero"),
            Pasajero(TipoPasajero.REGULAR, 3068, 31, "Sofía Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3069, 33, "José Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3070, 35, "Marina Rodríguez"),
            Pasajero(TipoPasajero.REGULAR, 3071, 27, "Raúl González"),
            Pasajero(TipoPasajero.REGULAR, 3072, 29, "Elena Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3073, 30, "Jesús Gómez"),
            Pasajero(TipoPasajero.REGULAR, 3074, 34, "Alicia Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3075, 31, "Antonio Romero"),
            Pasajero(TipoPasajero.REGULAR, 3076, 33, "Carmen García"),
            Pasajero(TipoPasajero.REGULAR, 3077, 27, "María López"),
            Pasajero(TipoPasajero.REGULAR, 3078, 30, "Óscar Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3079, 29, "Víctor Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3080, 32, "Luis Ruiz"),
            Pasajero(TipoPasajero.REGULAR, 3081, 35, "José Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3082, 28, "Nerea Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3083, 30, "Laura Romero"),
            Pasajero(TipoPasajero.REGULAR, 3084, 34, "Álvaro Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3085, 31, "Carmen Díaz"),
            Pasajero(TipoPasajero.REGULAR, 3086, 29, "Carlos González"),
            Pasajero(TipoPasajero.REGULAR, 3087, 27, "Sofía Rodríguez"),
            Pasajero(TipoPasajero.REGULAR, 3088, 32, "Víctor Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3089, 30, "María Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3090, 31, "José Luis Romero"),
            Pasajero(TipoPasajero.REGULAR, 3091, 28, "Ángel Sánchez"),
            Pasajero(TipoPasajero.REGULAR, 3092, 33, "Patricia Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3093, 35, "Carlos Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3094, 27, "Clara Ruiz"),
            Pasajero(TipoPasajero.REGULAR, 3095, 30, "José Gómez"),
            Pasajero(TipoPasajero.REGULAR, 3096, 29, "Ana García"),
            Pasajero(TipoPasajero.REGULAR, 3097, 32, "Luis Fernández"),
            Pasajero(TipoPasajero.REGULAR, 3098, 28, "Manuel Martínez"),
            Pasajero(TipoPasajero.REGULAR, 3099, 31, "Marta Pérez"),
            Pasajero(TipoPasajero.REGULAR, 3100, 34, "Óscar Sánchez"),
            #Pasajeros DISCAPACITADO - 60
            Pasajero(TipoPasajero.DISCAPACITADO, 4001, 45, "Luis Mendoza"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4002, 52, "Ana Ruiz"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4003, 38, "Carlos Martínez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4004, 41, "María López"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4005, 49, "Jorge Fernández"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4006, 36, "Patricia Gómez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4007, 47, "José Pérez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4008, 53, "Laura Martínez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4009, 39, "Francisco Morales"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4010, 50, "Sofía Ramírez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4011, 46, "Miguel Castro"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4012, 43, "Daniela Romero"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4013, 42, "Fernando López"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4014, 48, "Isabel Delgado"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4015, 40, "Andrés Vega"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4016, 44, "Valentina Ortega"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4017, 37, "Ricardo Morales"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4018, 49, "Camila Salazar"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4019, 50, "Antonio Fernández"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4020, 51, "Gabriela Navarro"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4021, 35, "Santiago Guzmán"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4022, 46, "Isabel Ríos"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4023, 41, "Manuel Cruz"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4024, 44, "Rosa Paredes"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4025, 47, "Cristian Ponce"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4026, 38, "Elena Reyes"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4027, 49, "Pablo Cordero"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4028, 42, "Teresa Salazar"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4029, 45, "David Márquez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4030, 50, "Silvia Palacios"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4031, 33, "Raúl Aguirre"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4032, 40, "Claudia Blanco"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4033, 43, "Sebastián Serrano"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4034, 37, "Mónica Ibáñez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4035, 46, "Rodrigo Herrera"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4036, 48, "Paula Gallardo"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4037, 44, "Tomás Rivero"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4038, 49, "Natalia Cabrera"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4039, 50, "Francisco Luna"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4040, 52, "Diana Medina"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4041, 45, "Álvaro Peña"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4042, 48, "Carmen Castro"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4043, 50, "Eduardo Escobar"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4044, 43, "Julia Muñoz"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4045, 42, "Héctor León"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4046, 39, "Irene Carrillo"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4047, 36, "Emilio Peña"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4048, 44, "Marta Campos"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4049, 48, "Adrián Lara"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4050, 50, "Sara Núñez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4051, 37, "Javier Fuentes"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4052, 40, "Victoria Bravo"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4053, 41, "Rafael Mora"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4054, 46, "Liliana Fuentes"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4055, 34, "Fabián Vázquez"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4056, 32, "Lorena Paredes"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4057, 30, "Ángel Soto"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4058, 27, "Rebeca Duarte"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4059, 31, "Guillermo Solís"),
            Pasajero(TipoPasajero.DISCAPACITADO, 4060, 39, "Natalia Ramos")
        ]
        #Agregar los pasajeros a la terminal
        Terminal.setPasajeros(pasajerosTerminal)

        # VIAJES
        lista = []
        reservas = []

        # TRANSPORTADORA 1
        lista.append(Viaje(terminal, "8:0", "2/1/2024", conductores1[1].getVehiculo(), conductores1[1], Destino.CARTAGENA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "10:0", "2/1/2024", conductores1[3].getVehiculo(), conductores1[3], Destino.BARRANQUILLA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "12:0", "2/1/2024", conductores1[7].getVehiculo(), conductores1[7], Destino.BELLO, Destino.MEDELLIN))
        a = Viaje(terminal, "14:0", "14/1/2024", conductores1[9].getVehiculo(), conductores1[9], Destino.SANTAMARTA, Destino.MEDELLIN)

        lista.append(a)
        reservas.append(a)

        # TRANSPORTADORA 2
        lista.append(Viaje(terminal, "8:30", "3/1/2024", conductores2[1].getVehiculo(), conductores2[1], Destino.GUARNE, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "10:30", "5/1/2024", conductores2[3].getVehiculo(), conductores2[3], Destino.LAPINTADA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "12:30", "7/1/2024", conductores2[7].getVehiculo(), conductores2[7], Destino.GUATAPE, Destino.MEDELLIN))
        b = Viaje(terminal, "14:30", "18/1/2024", conductores2[9].getVehiculo(), conductores2[9], Destino.BARBOSA, Destino.MEDELLIN)

        lista.append(a)
        reservas.append(a)

        # TRANSPORTADORA 3
        lista.append(Viaje(terminal, "19:0", "12/1/2024", conductores3[1].getVehiculo(), conductores3[1], Destino.CALI, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "10:0", "15/1/2024", conductores3[3].getVehiculo(), conductores3[3], Destino.ITAGUI, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "13:0", "16/1/2024", conductores3[7].getVehiculo(), conductores3[7], Destino.ENVIGADO, Destino.MEDELLIN))
        c = Viaje(terminal, "9:0", "1/2/2024", conductores3[9].getVehiculo(), conductores3[9], Destino.MARINILLA, Destino.MEDELLIN)
        
        lista.append(c)
        reservas.append(c)

        # TRANSPORTADORA 4
        lista.append(Viaje(terminal, "11:0", "1/2/2024", conductores4[1].getVehiculo(), conductores4[1], Destino.GIRARDOTA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "9:0", "1/2/2024", conductores4[3].getVehiculo(), conductores4[3], Destino.RIONEGRO, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "10:0", "1/3/2024", conductores4[7].getVehiculo(), conductores4[7], Destino.BOGOTA, Destino.MEDELLIN))
        d = Viaje(terminal, "9:0", "1/3/2024", conductores4[9].getVehiculo(), conductores4[9], Destino.LAESTRELLA, Destino.MEDELLIN)
        
        lista.append(d)
        reservas.append(d)

        #TRANSPORTADORA 5
        lista.append(Viaje(terminal, "13:0", "1/3/2024", conductores5[1].getVehiculo(), conductores5[1], Destino.BUENAVENTURA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "9:25", "12/3/2024", conductores5[7].getVehiculo(), conductores5[7], Destino.BUCARAMANGA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "9:30", "2/3/2024", conductores5[3].getVehiculo(), conductores5[3], Destino.ANGELOPOLIS, Destino.MEDELLIN))
        e = Viaje(terminal, "10:0", "10/4/2024", conductores5[9].getVehiculo(), conductores3[9], Destino.COOPACABANA, Destino.MEDELLIN)
        
        lista.append(e)
        reservas.append(e)

        # TRANSPORTADORA 6
        lista.append(Viaje(terminal, "18:0", "1/3/2024", conductores6[1].getVehiculo(), conductores6[1], Destino.SANTAMARTA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "20:0", "10/3/2024", conductores6[3].getVehiculo(), conductores6[3], Destino.BARRANQUILLA, Destino.MEDELLIN))
        lista.append(Viaje(terminal, "14:0", "14/3/2024", conductores6[7].getVehiculo(), conductores6[7], Destino.CALI, Destino.MEDELLIN))
        f = Viaje(terminal, "8:0", "11/3/2024", conductores6[9].getVehiculo(), conductores6[9], Destino.LAPINTADA, Destino.MEDELLIN)
        
        lista.append(f)
        reservas.append(f)

        # VINCULAR LOS VIAJES A LA TERMINAL
        
        Terminal.setViajes(lista)
        Terminal.setReservas(reservas)

        Tiempo(1)
