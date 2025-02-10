from politicas.base_policy import BasePolicy
from politicas.policy_registry import PolicyRegistry

class UserPolicy(BasePolicy):
    def puede_acceder(self, clase_personaje: str) -> bool:
        return clase_personaje.lower() != "mago"  # Restringe la clase mago

# Registro automático
PolicyRegistry.register("usuario", UserPolicy)