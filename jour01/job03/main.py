class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def methode(self):
        print("le nombre1 est",self.nombre1)
        print("le nombre est",self.nombre2)
    
    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"{self.nombre1} + {self.nombre2} = {result}")

instance_operation = Operation(1,21)

instance_operation.methode()

instance_operation.addition()