from personajes.personaje import Personaje
from personajes.registro import PersonajeRegistry

class Mago(Personaje):  # Herencia
    def __init__(self, nombre, salud, fuerza, inteligencia, libro, **kwargs):
        super().__init__(nombre, salud, fuerza, inteligencia)
        self._libro = libro

    def atacar(self, enemigo):  # Polimorfismo
        dano = self._inteligencia + self._libro
        print(f"{self._nombre} lanza un hechizo causando {dano} de daño.")
        enemigo.recibir_dano(dano)
        
PersonajeRegistry.registrar_clase("mago", Mago)
