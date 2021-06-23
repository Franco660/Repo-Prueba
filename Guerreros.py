import random
# sufijo Atk significa "del atacante", sufijo Def significa "del defensor"
class Guerrero:
    def __init__(self, nombre, vida, fuerza, defensa, precision, velocidad):
        self.nombre = nombre  # STR
        self.vida = vida  # INT
        self.fuerza = fuerza
        self.defensa = defensa
        self.precision = precision  # FLOAT
        self.velocidad = velocidad

    def __str__(self):
        return "{nombre}"\
            .format(nombre=self.nombre)

    def golpear(self, precisionAtk, velocidadDef, fuerzaAtk, defensaDef, guerDef):
        chanceAcierto = (precisionAtk - velocidadDef) / 100
        chanceRoll = random.randrange(0, 100)
        print("La chance de golpear es:", chanceAcierto)
        print("La suerte dice:", chanceRoll)
        if chanceRoll <= chanceAcierto:
            print(">>>>>>Por lo tanto el golpe CONECTA")
            guerDef.calcularDmg(fuerzaAtk, defensaDef, guerDef)
        else:
            print(">>>>>>Por lo tanto el golpe FALLA")
            print("=======================================")

    def calcularDmg(self, fuerzaAtk, defensaDef, guerreroDef):
        dmg = (fuerzaAtk - defensaDef)
        variacion = random.randrange(-10, 11, 1)
        guerreroDef.vida -= dmg + variacion
        print("El golpe causó", dmg+variacion, "puntos de daño al guerrero", guerreroDef)
        print("=======================================")

    def ordenGolpes(self,vAzul,vRojo):
        if vAzul > vRojo:
            print("El guerrero azul es mas rapido asi que toma la iniciativa")
            return 1
        else:
            print("El guerrero rojo es mas rapido asi que toma la iniciativa")
            return 0

    def reporteVida(self):
        print("*********VIDA DEL GUERRERO AZUL", guerAzul.vida)
        print("*********VIDA DEL GUERRERO ROJO", guerRojo.vida)


    def iniciarBatalla(self,orden):
        if orden == 1:
            while guerAzul.vida > 0 and guerRojo.vida > 0:
                Guerrero.reporteVida("")
                print("Golpea el guerrero AZUL")
                guerAzul.golpear(guerAzul.precision, guerRojo.velocidad, guerAzul.fuerza, guerRojo.defensa, guerRojo)
                Guerrero.reporteVida("")
                print("Golpea el guerrero ROJO")
                guerRojo.golpear(guerRojo.precision, guerAzul.velocidad, guerRojo.fuerza, guerAzul.defensa, guerAzul)
        else:
            while guerAzul.vida > 0 and guerRojo.vida > 0:
                Guerrero.reporteVida("")
                print("Golpea el guerrero ROJO")
                guerRojo.golpear(guerRojo.precision, guerAzul.velocidad, guerRojo.fuerza, guerAzul.defensa, guerAzul)
                Guerrero.reporteVida("")
                print("Golpea el guerrero AZUL")
                guerAzul.golpear(guerAzul.precision, guerRojo.velocidad, guerAzul.fuerza, guerRojo.defensa, guerRojo)
        if guerAzul.vida <= 0:
            print("Ha ganado el guerrero Rojo!")
        else:
            print("Ha ganado el guerrero Azul!")


if __name__ == '__main__':
    guerAzul = Guerrero("Azul", 10000, 3500, 2000, 6700.18, 50.75)
    #                   NOMBRE  VIDA   FRZ    DEF   PRE     VEL
    guerRojo = Guerrero("Rojo", 10000, 4000, 2500, 8200.33, 30.5)
    ordenCalculado = Guerrero.ordenGolpes("", guerAzul.velocidad, guerRojo.velocidad)
    Guerrero.iniciarBatalla("",ordenCalculado)
