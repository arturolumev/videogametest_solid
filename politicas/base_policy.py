from abc import ABC, abstractmethod

class BasePolicy(ABC):
    @abstractmethod
    def puede_acceder(self, clase_personaje: str) -> bool:
        pass
