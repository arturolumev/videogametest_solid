import json
import os
import importlib

class PersonajeRegistry:
    _personajes = {}
    _clases_personaje = {}  # Registro dinámico de clases

    @classmethod
    def registrar_clase(cls, tipo, clase_personaje):
        # print(f"Registrando clase: {tipo}")
        cls._clases_personaje[tipo] = clase_personaje
        # print(f"Clase {tipo} registrada.")

    @classmethod
    def cargar_personajes(cls, archivo_json):
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            for data in datos:
                tipo = data.get("tipo")
                cls.registrar(tipo, data)

    @classmethod
    def registrar(cls, tipo, data):
        if tipo not in cls._personajes:
            cls._personajes[tipo] = []

        # Usar la clase registrada dinámicamente
        clase_personaje = cls._clases_personaje.get(tipo)
        if clase_personaje:
            personaje = clase_personaje(**data)
            cls._personajes[tipo].append(personaje)
        else:
            print(f"Tipo de personaje no reconocido: {tipo}")

    @classmethod
    def listar_clases(cls):
        return list(cls._clases_personaje.keys())

    @classmethod
    def listar_personajes_por_clase(cls, clase):
        return cls._personajes.get(clase, [])

    @classmethod
    def obtener_personaje(cls, clase, nombre):
        personajes = cls._personajes.get(clase, [])
        for personaje in personajes:
            if personaje.nombre.lower() == nombre.lower():
                return personaje
        return None
    
    @classmethod
    def load_personajes(cls):
        # Importar todas las políticas de la carpeta politicas
        carpeta_clases = "personajes/clases"
        for archivo in os.listdir(carpeta_clases):
            if archivo.endswith(".py") and not archivo.startswith("__"):
                nombre_modulo = f"personajes.clases.{archivo[:-3]}"
                importlib.import_module(nombre_modulo)
