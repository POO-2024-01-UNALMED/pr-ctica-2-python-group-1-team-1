from errorAplicacion import ErrorAplicacion

class exceptionError1(ErrorAplicacion):

    msg = "error1"
    
    def __init__(self):
        
        super().__init__(exceptionError1.msg)
        

    def mensaje(self):
        
        print("prueba")

if __name__ == "__main__":
    
    try:
        raise exceptionError1()
    
    except exceptionError1 as f:
        
        f.mensaje()