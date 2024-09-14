class ErrorAplicacion(Exception):
    
    def __init__(self, msg):
        
        self.msg = msg
        self.mesagge = self.getmsg()
        super().__init__("Prueba excepción")
        
        
    def getmsg(self):
        
        print(self.msg)