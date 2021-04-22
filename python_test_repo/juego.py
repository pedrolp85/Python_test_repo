

class Guerrero():
    
    def __init__(self,ataque=3,defensa=3,vida=10):
        self.ataque=self.set_ataque()
        self.defensa=self.set_defensa()

    def set_ataque(self,nuevo_ataque):
        
        if int (nuevo_ataque) > 10:
            self.ataque=nuevo_ataque
        else:
            raise ValueError ("El ataque no puede ser mayor que 10")
    
    def set_defensa(self,nueva_defensa):
        
        if int (nueva_defensa) > 10:
            self.defensa=nueva_defensa
        else:
            raise ValueError ("La defensa no puede ser mayor que 10")


if __name__== "main":

    guerrero_1=Guerrero()