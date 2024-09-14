from errorAplicacion import ErrorAplicacion

class exceptionError2(ErrorAplicacion):
    
    def __init__(self):
        
        super().__init__("w")
    
    def lanzarExepcion(self):
        
        raise exceptionError2()
    

if __name__ == "__main__":
    
    raise exceptionError2()
    