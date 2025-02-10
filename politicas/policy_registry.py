import os
import importlib
from politicas.base_policy import BasePolicy

class PolicyRegistry:
    _policies = {}

    @classmethod
    def register(cls, role_name: str, policy_class: BasePolicy):
        cls._policies[role_name.lower()] = policy_class

    @classmethod
    def get_policy(cls, role_name: str):
        return cls._policies.get(role_name.lower(), None)

    @classmethod
    def load_policies(cls):
        # Importar todas las políticas de la carpeta politicas
        carpeta_politicas = "politicas/roles"
        for archivo in os.listdir(carpeta_politicas):
            if archivo.endswith(".py") and not archivo.startswith("__"):
                nombre_modulo = f"politicas.roles.{archivo[:-3]}"
                importlib.import_module(nombre_modulo)
    
    @classmethod
    def listar_politicas(cls):
        return list(cls._policies.keys())
