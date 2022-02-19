import unittest

from pyrsistent import b
# assert reserved word
# assert 1 == 2, "Shows here a error message"

# escrevendo testes unitário / writing unit tests
def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
    
class TestClass(unittest.TestCase):
    def test_soma(self):
        result = soma(1,3)
        error_msg = f"{result} is not equal to 3"
        self.assertEqual(result,3,error_msg)
        
unittest.main()