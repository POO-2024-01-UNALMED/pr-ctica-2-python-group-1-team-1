from errorAplicacion import ErrorAplicacion

class exceptionError2(ErrorAplicacion):
    
    msg = "error2"
    
    def __init__(self):
        
        super().__init__(exceptionError2.msg)
        

    def mensaje(self):
        
        print("prueba")

if __name__ == "__main__":
    
    try:
        raise exceptionError2()
    
    except exceptionError2 as f:
        
        f.mensaje()
    
    