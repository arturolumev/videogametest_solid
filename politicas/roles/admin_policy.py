from politicas.base_policy import BasePolicy
from politicas.policy_registry import PolicyRegistry

class AdminPolicy(BasePolicy):
    def puede_acceder(self, clase_personaje: str) -> bool:
        return True  # El admin puede acceder a todas las clases

# Registro automático
PolicyRegistry.register("admin", AdminPolicy)