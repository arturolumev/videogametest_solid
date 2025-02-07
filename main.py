from personajes.guerrero import Guerrero
from personajes.mago import Mago
from personajes.heroe import Heroe
from villano import Villano
from combate import simular_combate

def main():
    # guerrero = Guerrero(nombre="Arthas", salud=100, fuerza=20, inteligencia=5, espada=15)
    # mago = Mago(nombre="Merlin", salud=80, fuerza=5, inteligencia=25, libro=20)
    # villano = Villano()

    # eleccion = input("Elige tu personaje (guerrero/mago): ").lower()
    # if eleccion == "guerrero":
    #     simular_combate(guerrero, villano)
    # elif eleccion == "mago":
    #     simular_combate(mago, villano)
    # else:
    #     print("Opción no válida.")
    
    personajes_disponibles = {
        "guerrero": Guerrero(nombre="Arthas", salud=100, fuerza=20, inteligencia=5, espada=15),
        "mago": Mago(nombre="Merlin", salud=80, fuerza=5, inteligencia=25, libro=20),
        "heroe": Heroe(nombre="Leon", salud=90, fuerza=15, inteligencia=10, espada=15)
    }
    
    villano = Villano()
    
    personajes = ', '.join(list(personajes_disponibles.keys()))
    
    print("Personajes disponibles:", personajes)

    eleccion = input("Elige tu personaje: ").lower()
    personaje = personajes_disponibles.get(eleccion)

    if personaje:
        simular_combate(personaje, villano)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()