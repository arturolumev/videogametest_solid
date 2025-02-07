from personajes.personaje import Personaje

class Heroe(Personaje):  # Herencia
    def __init__(self, nombre, salud, fuerza, inteligencia, espada):
        super().__init__(nombre, salud, fuerza, inteligencia)
        self._espada = espada

    def atacar(self, enemigo):  # Polimorfismo
        dano = self._fuerza + self._espada + self._inteligencia
        print(f"{self._nombre} ataca con su espada causando {dano} de daño.")
        enemigo.recibir_dano(dano)