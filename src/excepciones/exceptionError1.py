from errorAplicacion import ErrorAplicacion

class ExceptionError1(ErrorAplicacion):

    msg = "error1"
    
    def __init__(self):
        
        super().__init__(ExceptionError1.msg)
        

    def mensaje(self):
        
        print("prueba")

if __name__ == "__main__":
    
    try:
        raise ExceptionError1()
    
    except ExceptionError1 as f:
        
        f.mensaje()