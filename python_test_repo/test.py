"""def aprobados(alumnos):
    decision = []
    suspendido= False
    for alumno in alumnos:
        if alumno.alumno_aprobado():
            decision.append(False)
        else:
            decision.append(True)
    return(decision) """



class Alumno():

    def __init__(self, nombre, nota, clase):
        self._nombre = nombre
        self.nota = nota
        self.clase = clase


notas = [10, 9, 8, 7, 6, 5]
nombres= [ 'Luis', "Carlos", "Pedro", 'Alberto', "Victor"]
clases = [ 'a', 'b', 'a', 'a', 'b' ]

alumno = Alumno("Dani", "nota", "clase")
print(alumno._nombre)

"""
alumnos = []
for nombre, nota, clase in zip(nombres,notas,clases):
    alumnos.append(Alumno(nombre, nota, clase))
"""
"""
alumnos = [ Alumno(nombre, nota, clase) for nombre, nota, clase in zip(nombres,notas,clases)]


#clase b, notas <7 suspendido, Alberto == suspendido
resultado= aprobado(alumnos)
print(resultado)"""

