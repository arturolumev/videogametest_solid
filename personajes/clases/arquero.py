from personajes.personaje import Personaje
from personajes.registro import PersonajeRegistry

class Arquero(Personaje):  # Herencia
    def __init__(self, nombre, salud, fuerza, inteligencia, arco, **kwargs):
        super().__init__(nombre, salud, fuerza, inteligencia)
        self._arco = arco

    def atacar(self, enemigo):  # Polimorfismo
        dano = self._fuerza + self._arco
        print(f"{self._nombre} ataca con su arco causando {dano} de daño.")
        enemigo.recibir_dano(dano)

PersonajeRegistry.registrar_clase("arquero", Arquero)
