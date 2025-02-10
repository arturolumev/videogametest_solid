from personajes.personaje import Personaje
from personajes.registro import PersonajeRegistry

class Guerrero(Personaje):  # Herencia
    def __init__(self, nombre, salud, fuerza, inteligencia, espada, **kwargs):
        super().__init__(nombre, salud, fuerza, inteligencia)
        self._espada = espada

    def atacar(self, enemigo):  # Polimorfismo
        dano = self._fuerza + self._espada
        print(f"{self._nombre} ataca con su espada causando {dano} de daño.")
        enemigo.recibir_dano(dano)

PersonajeRegistry.registrar_clase("guerrero", Guerrero)
