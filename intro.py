import unittest

from pyrsistent import b
# assert reserved word
# assert 1 == 2, "Shows here a error message"

# escrevendo testes unitário / writing unit tests
def soma(a,b):
    return a+b

test_number_list = [1,2,3]

def higherThan(higher,lower):
    return higher > lower

class TestClass(unittest.TestCase):
    def test_soma(self):
        result = soma(1,3)
        error_msg = f"{result} is not equal to 3"
        self.assertNotEqual(result,3,error_msg)
        
    def test_if_in(self):
        self.assertIn(2,test_number_list,"Não está na lista")
        
    def teste_higher_than(self):
        self.assertTrue(higherThan(3,2),"First num not higher than the second")
        
unittest.main()