import unittest

from pyrsistent import b
# assert reserved word
# assert 1 == 2, "Shows here a error message"

# escrevendo testes unitário / writing unit tests
def soma(a,b):
    return a+b

def up_calc_server():
    print("Upping calc server")

def down_calc_server():
    print("Downing calc server")

test_number_list = [1,2,3]

def higherThan(higher,lower):
    return higher > lower

class TestClass(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        up_calc_server()
    

    
    @unittest.expectedFailure
    def test_soma(self):
        result = soma(1,3)
        error_msg = f"{result} is not equal to 3"
        self.assertEqual(result,3,error_msg)
        
    def test_if_in(self):
        self.assertIn(2,test_number_list,"Is not in the list")
        
    def teste_higher_than(self):
        self.assertTrue(higherThan(3,2),"First num not higher than the second")
        
        
    def test_multiple_sum(self):
        
        numbers = [(1,2,3),(3,2,5)]
        
        for num_result in numbers:
            
            with self.subTest(num_result):
                
                a,b,result = num_result
                message = f"Sum error {a} + {b} not equal to {result}"
                self.assertEqual(soma(a,b),result,message)
    
    @classmethod
    def tearDownClass(cls) -> None:
        down_calc_server()
        
        
unittest.main()