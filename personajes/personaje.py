# from abc import ABC, abstractmethod
from interfaces.iatacante import IAtacante

class Personaje(IAtacante):  # Abstracción
    def __init__(self, nombre, salud, fuerza, inteligencia):  # Encapsulamiento
        self._nombre = nombre
        self._salud = salud
        self._fuerza = fuerza
        self._inteligencia = inteligencia

    # @abstractmethod
    # def atacar(self, enemigo):
    #     pass

    def recibir_dano(self, dano):
        self._salud -= dano
        print(f"{self._nombre} recibe {dano} de daño. Salud restante: {self._salud}")

    def esta_vivo(self):
        return self._salud > 0

    @property
    def nombre(self):
        return self._nombre

    @property
    def salud(self):
        return self._salud