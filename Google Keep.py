# Google Keep
class Notas:
    def __init__(self, titulo, descripcion, color, prioridad, numero):
        self.numero = numero
        self.titulo = titulo
        self.descripcion = descripcion
        self.color = color
        self.prioridad = prioridad

    def __str__(self):
        return "\nNOTA NUMERO {numero} \nTitulo de nota: {titulo}  \nDescripción:    {descripcion}  " \
               "\nColor:          {color} \nPrioridad:      {prioridad} " \
            .format(titulo=self.titulo, descripcion=self.descripcion, color=self.color, prioridad=self.prioridad,
                    numero=self.numero)


class NotasUsuario:
    def __init__(self):
        self.listadoNotas = []

    def agregarNota(self, nota):
        self.listadoNotas.append(nota)

    def listarNotas(self):
        print("Las notas actuales: ")
        for x in self.listadoNotas:
            print(x)

    def borrarNota(self, ingreso):
        print("Se eliminara la nota numero ", ingreso)
        ingresoreal = ingreso - 1         # Como las listas van desde 0-inf, la nota 1 internamente es 0, la 2 es 1, etc
        largolista = len(self.listadoNotas)
        if largolista >= ingresoreal >= 0:             # Para asegurarse de que no termine en un numero negativo
            self.listadoNotas.pop(ingresoreal)
        else:
            print("Ese numero de nota no existe")


if __name__ == '__main__':
    tituloIngreso = "0"
    cantidadNotas = 0
    NotasUsuario = NotasUsuario()
    while "@" not in tituloIngreso:
        cantidadNotas += 1
        # Inputs para que el usuario ingrese los datos de la nota
        tituloIngreso = input("Ingrese el titulo de su nota (incluya ""@"" si es la ultima nota a ingresar): ")
        descripcionIngreso = input("Ingrese la descripcion de la nota: ")
        colorIngreso = input("Ingrese el color que desea utilizar para la nota: ")
        prioridadIngreso = input("Ingrese la prioridad de la nota: ")
        # Se crea la nota usando los datos
        Nota1 = Notas(tituloIngreso, descripcionIngreso, colorIngreso, prioridadIngreso, cantidadNotas)
        NotasUsuario.agregarNota(Nota1)
        NotasUsuario.listarNotas()
    print()
    notaBorrada = int(input("Ingrese la nota a borrar "))
    NotasUsuario.borrarNota(notaBorrada)
    NotasUsuario.listarNotas()
