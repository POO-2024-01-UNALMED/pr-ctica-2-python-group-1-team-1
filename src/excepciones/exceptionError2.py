from errorAplicacion import ErrorAplicacion

class ExceptionError2(ErrorAplicacion):
    
    msg = "error2"
    
    def __init__(self):
        
        super().__init__(ExceptionError2.msg)
        

    def mensaje(self):
        
        print("prueba")

if __name__ == "__main__":
    
    try:
        raise ExceptionError2()
    
    except ExceptionError2 as f:
        
        f.mensaje()
    
    