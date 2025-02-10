from politicas.base_policy import BasePolicy
from politicas.policy_registry import PolicyRegistry

class GuestPolicy(BasePolicy):
    def puede_acceder(self, clase_personaje: str) -> bool:
        return clase_personaje.lower() == "heroe"  # Solo puede elegir "heroe"

# Registro automático
PolicyRegistry.register("guest", GuestPolicy)
