from src.excepciones.errorAplicacion import ErrorAplicacion

class ExceptionError2(ErrorAplicacion):
    
 
    
    def __init__(self,s):
        
        super().__init__("Error de procesamiento de datos: "+str(s))
        

    
    