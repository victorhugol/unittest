from surfshop import ShoppingCart 
import unittest

class ShoppingCartTest(unittest.TestCase):
  cart = None

  def setUp(self):
    self.cart = ShoppingCart()
  def tearDown(self):
    del self.cart

  def test_add_surfboards(self):

    boards_quantities = ({"num":1,"suffix":''},{"num":2,"suffix":"s"})

    for quantity in boards_quantities:
      with self.subTest(quantity):
        message = f'Successfully added {quantity["num"]} surfboard{quantity["suffix"]} to cart!'
        self.assertEqual(self.cart.add_surfboards(quantity["num"]),message,'Board Adding failed!')
  @unittest.expectedFailure
  def test_add_board_limit(self):
    self.skipTest("No need this test for a while")
    self.cart.add_surfboards(5)

  def test_local_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)


unittest.main()



















