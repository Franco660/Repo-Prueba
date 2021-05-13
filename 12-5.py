#EJERCICIO 3
class Empleado:
    def __init__(self, nombre, sueldo=1000):
        self.nombre = input("Ingrese el nombre del empleado ")
        self.sueldo = int(input("Ingrese el sueldo del empleado "))


empleadoDatos = Empleado("", 0)

if __name__ == "__main__":
    print("El empleado se llama", empleadoDatos.nombre)
    print("Su sueldo es de", empleadoDatos.sueldo, "pesos")
    if empleadoDatos.sueldo > 3000:
        print("Por lo tanto, debera pagar impuestos")
    else:
        print("No debe pagar impuestos")
"""
#EJERCICIO 4


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class EmpleadoHered(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo


if __name__ == "__main__":
    datosPersona = Persona(input("Ingrese su nombre "), input("Ingrese su edad "))
    datosEmpleado = EmpleadoHered(datosPersona.nombre, datosPersona.edad, input("Ingrese su sueldo "))
    print("El nombre ingresado es:", datosPersona.nombre)
    print("La edad ingresada es:", datosPersona.edad)
    print("El sueldo ingresado es:", datosEmpleado.sueldo)

"""
