import random
from personajes.personaje import Personaje

class Villano(Personaje):
    def __init__(self, nombre="Villano", salud=None, fuerza=None, inteligencia=None):
        salud = salud if salud else random.randint(50, 100)
        fuerza = fuerza if fuerza else random.randint(5, 15)
        inteligencia = inteligencia if inteligencia else random.randint(5, 15)
        super().__init__(nombre, salud, fuerza, inteligencia)

    def atacar(self, enemigo):
        dano = random.choice([self._fuerza, self._inteligencia])
        print(f"{self._nombre} ataca causando {dano} de daño.")
        enemigo.recibir_dano(dano)