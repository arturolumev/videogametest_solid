from abc import ABC, abstractmethod

class IAtacante(ABC):
    @abstractmethod
    def atacar(self, enemigo):
        """Método obligatorio que todas las clases deben implementar"""
        pass
