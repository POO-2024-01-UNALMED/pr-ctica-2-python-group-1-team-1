from src.excepciones.exceptionError2 import ExceptionError2

class NotFoundException(ExceptionError2):
    def __init__(self, s):
        super().__init__(s)
