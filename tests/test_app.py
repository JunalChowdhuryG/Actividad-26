import unittest
from app import prueba


class Test_Prueba(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(prueba("Mundo"), "Hola Mundo")
        self.assertEqual(prueba("Junal"), "Hola Junal")


if __name__ == "__main__":
    unittest.main()
