

###APL BANCO 
### Usuario (nombre, apellido, admin/user, cuentas)





class Usuario():

    def __init__(self,nombre,apellido,role,cuentas=[ ],baneado=False):
        self.set_nombre(nombre)
        self.set_baneado(baneado)
        self.set_apellido(apellido)
    
    
    def set_nombre(self,nuevo_nombre):
        self.nombre=nuevo_nombre

    def set_apellido(self,nuevo_apellido):
        if nuevo_apellido == "Lopez":
            self.set_baneado(True)
        self.apellido=nuevo_apellido   

    def set_baneado(self,baneado):
        self.baneado = baneado

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return f"Apellido de la persona: {self.apellido}"
    
    def __str__(self):#str(objeto) -> convierte
        return f"{self.get_nombre()} {self.get_apellido()}"
    #__sum__, __sub__, .... dunde classes
    def __eq__(self, objeto2):#devolver true o false objeto1 == objeto2
        if self.baneado == objeto2.baneado:
            return True
        else:
            return False

class UsuarioEspecial(Usuario):

    def __init__(self,nombre,apellido,role,cuentas=[ ],baneado=False):
        Usuario.__init__(self, nombre, apellido, role, cuentas)


    def get_apellido(self):
        return f"Apellido de la persona especial: {self.apellido}"
        #Se pueden sobreescribir métodos

if __name__ == "__main__":
    usuario = Usuario('Pedro','Maria','admin')
    usuario_especial = UsuarioEspecial('Pedro','Maria','admin')
    print(usuario_especial.get_nombre())
    print(usuario_especial.get_apellido())
    usuario2 = Usuario('Ibai','Maria','admin')



    print(f"Nombre de la persona: {usuario.nombre}")

    usuario.set_apellido('Jesus')
    a = str(usuario2)
    #ENVIAR LA VARIABLE a AL FRONT
    print(usuario == usuario2)