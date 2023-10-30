import string
import random
import unittest

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

class TestGenerarContrasena(unittest.TestCase):
    def test_longitud_6(self):
        longitud_contrasena = 6
        contrasena_generada = generar_contrasena(longitud_contrasena)
        self.assertEqual(len(contrasena_generada), longitud_contrasena)

    def test_longitud_7(self):
        longitud_contrasena = 7
        contrasena_generada = generar_contrasena(longitud_contrasena)
        self.assertEqual(len(contrasena_generada), longitud_contrasena)

nombre = input("Ingrese su nombre: ")
print("Bienvenido al generador de contraseñas " + nombre)

contra = int(input("¿Cuántos caracteres necesita? 1. De 6 caracteres. 2. De 7 caracteres. 3. De 8 caracteres.: "))

if contra == 1:
    longitud_contrasena = 6
    contrasena_generada = generar_contrasena(longitud_contrasena)
    print("Tu contraseña generada es:", contrasena_generada)
elif contra == 2:
    longitud_contrasena = 7
    contrasena_generada = generar_contrasena(longitud_contrasena)
    print("Tu contraseña generada es:", contrasena_generada)
elif contra == 3:
    longitud_contrasena = 8
    contrasena_generada = generar_contrasena(longitud_contrasena)
    print("Tu contraseña generada es:", contrasena_generada)
else:
    print("Número diferente de 1, 2 o 3")


    unittest.main()