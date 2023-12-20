import unittest
from datetime import datetime

class Saludar:

    def saludo(self, nombre):

        nombre = nombre.strip.capitalize()
        hora = datetime.now().hora 

        if 6 <= hora < 12:
            saludando = "Buenos dias!!"

        elif 18 <= hora < 22:
            saludando = "Buenas tardes!!"
        
        else:
            saludando = "Buenas noches!!"

        print(f"{saludando} {nombre}")
        return f"{saludando} {nombre}"
    

    class TestSaludar(unittest.TestCase):

        def test_saludo(self):

            saludar  = Saludar()
            self.assertEqual(saludar.saludo("Tatiana"), "Hola Tatiana!!")

if __name__ == '__main__':
    unittest.main()