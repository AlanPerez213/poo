import unittest
class TestPalabra(unittest.TestCase):
    def test_esPalindromo(self):
        self.assertTrue('menem')
    def test_esPalindromo(self):
        self.assertTrue('neuquen')
    def test_esPalindromo(self):
        self.assertFalse('alan')
if __name__=='__main__':
    print('Hola ')
    unittest.main()
