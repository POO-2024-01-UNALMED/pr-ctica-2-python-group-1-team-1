from src.excepciones.exceptionError1 import ExceptionError1

class ExceptionInput(ExceptionError1):
    def __init__(self, tipo,donde):
        msg = "Ingrese un valor " + tipo +" en " + donde
        super().__init__(msg)
    