import unittest
from personajes.guerrero import Guerrero
from personajes.mago import Mago
from villano import Villano
from combate import simular_combate
from main import main

class TestMain(unittest.TestCase):
    
    def test_create_guerrero(self):
        guerrero = Guerrero(nombre="Arthas", salud=100, fuerza=20, inteligencia=5, espada=15)
        self.assertEqual(guerrero.nombre, "Arthas")
        self.assertEqual(guerrero.salud, 100)
        self.assertEqual(guerrero.fuerza, 20)
        self.assertEqual(guerrero.inteligencia, 5)
        self.assertEqual(guerrero.espada, 15)

if __name__ == '__main__':
    unittest.main()
