from src.excepciones.errorAplicacion import ErrorAplicacion

class ExceptionError2(ErrorAplicacion):
    
    msg = "error2"
    
    def __init__(self,s):
        
        super().__init__(ExceptionError2.msg)
        

    
    