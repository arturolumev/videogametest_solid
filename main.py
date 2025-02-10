from villano import Villano
from combate import simular_combate
from personajes.registro import PersonajeRegistry
from politicas.policy_registry import PolicyRegistry

def main():        
    # Cargar todos los personajes dinámicamente
    PersonajeRegistry.load_personajes()
    
    # Cargar todas las políticas dinámicamente
    PolicyRegistry.load_policies()  
    
    villano = Villano()
    
    PersonajeRegistry.cargar_personajes("personajes.json")
            
    print("Selecciona tu tipo de usuario: ")
    politicas = PolicyRegistry.listar_politicas()
    for politica in politicas:
        print(f"- {politica}")
        
    rol = input("-> ").lower()
    
    politica = PolicyRegistry.get_policy(rol)
    
    if not politica:
        print(f"No hay una política registrada para el rol '{rol}'.")
        return
    
    politica = politica()  # Instanciar la política
    
    clases_disponibles = PersonajeRegistry.listar_clases()
    clases_autorizadas = [clase for clase in clases_disponibles if politica.puede_acceder(clase)]

    print("Clases disponibles:", ", ".join(clases_autorizadas))

    clase = input("Elige la clase de tu personaje: ").lower()
    if not politica.puede_acceder(clase):
        print(f"No tienes permisos para acceder a la clase {clase}.")
        return

    personajes = PersonajeRegistry.listar_personajes_por_clase(clase)
    if personajes:
        print("Personajes disponibles en la clase", clase + ":")
        for personaje in personajes:
            print(f"- {personaje.nombre}")

        nombre_personaje = input("Elige el nombre de tu personaje: ").lower()
        personaje_seleccionado = PersonajeRegistry.obtener_personaje(clase, nombre_personaje)

        if personaje_seleccionado:
            simular_combate(personaje_seleccionado, villano)
        else:
            print("Opción no válida.")
    else:
        print("No hay personajes en esta clase.")

if __name__ == "__main__":
    main()