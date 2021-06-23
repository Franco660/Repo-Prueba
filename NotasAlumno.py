
"""Realizar un programa que permita agregar notas numéricas a cada estudiante y se pueda calcular
el promedio de cada estudiante.
El alumno posee nombre, apellido, nro de legajo, notas (sería una lista o array de números con decimal)."""


class Alumno:
    def __init__(self, nombre, apellido, legajo, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.notas = notas

    def __str__(self):
        return "Nombre: {nombre} - Apellido: {apellido} | Nro legajo: {legajo} | Lista de Notas: {notas}" \
            .format(nombre=self.nombre, apellido=self.apellido, legajo=self.legajo, notas=self.notas)

    def calcularPromedio(self, notasEvaluar):
        numeroNotas = len(notasEvaluar)
        totalNotas = 0
        for x in notasEvaluar:
            totalNotas += x
        print("El promedio de notas es de", totalNotas/numeroNotas)

    def agregarNota(self, nota, alumnoCuestion):
        if nota in range(1, 11):
            alumnoCuestion.notas.append(nota)
            print("Nota de valor", nota, "agregada exitosamente para el alumno", alumnoCuestion.nombre)
        else:
            print("El valor ingresado no es un numero del 1 al 10")

    def agregarMultiplesNotas(self, variasNotas, alumnoCuestion):
        notasAgregadas = []
        for notaM in variasNotas:
            if 10 >= notaM >= 1:
                alumnoCuestion.notas.append(notaM)
                notasAgregadas.append(notaM)
            else:
                print("La nota", notaM, "no es un valor numerico del 1 al 10")
        print("Notas", notasAgregadas, "agregadas exitosamente para el alumno", alumnoCuestion.nombre)


if __name__ == '__main__':
    alumnoJuan = Alumno("Juan", "Perez", 1, [])
    alumnoMarcos = Alumno("Marcos", "Lopez", 2, [])
    print("=============Valores iniciales=========")
    print(alumnoJuan)
    print(alumnoMarcos)
    # Agregar una unica nota al alumno Juan
    alumnoJuan.agregarNota(1, alumnoJuan)
    # Agregar varias notas al alumno Marcos
    alumnoMarcos.agregarMultiplesNotas([2, 1, 20, 8, 10, 5.30, 7.4, 85, 4], alumnoMarcos)
    print("=============Valores con notas agregadas=========")
    # Calcular promedios
    print(alumnoJuan)
    alumnoJuan.calcularPromedio(alumnoJuan.notas)
    print(alumnoMarcos)
    alumnoMarcos.calcularPromedio(alumnoMarcos.notas)

