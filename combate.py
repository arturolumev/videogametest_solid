from interfaces.iatacante import IAtacante

def simular_combate(personaje: IAtacante, villano: IAtacante):
    print(f"\n¡Comienza el combate entre {personaje.nombre} y {villano.nombre}!")
    turno = 0
    while personaje.esta_vivo() and villano.esta_vivo():
        if turno % 2 == 0:
            personaje.atacar(villano)
        else:
            villano.atacar(personaje)
        turno += 1

    ganador = personaje if personaje.esta_vivo() else villano
    print(f"\n¡{ganador.nombre} ha ganado el combate!")