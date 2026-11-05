import unittest

class TestSeguridadSistema(unittest.TestCase):
    def test_validacion_datos(self):
        self.assertEqual(validar_dato(350, 400, 600), 400)
        self.assertEqual(validar_dato(650, 400, 600), 600)
        self.assertEqual(validar_dato(500, 400, 600), 500)

if __name__ == '__main__':
    unittest.main()