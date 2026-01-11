import unittest

class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

  def get_price(self, item):
    return self.menu.get(item.lower())

  def add_item(self, item, price):
    self.menu[item.lower()] = price

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 2.75)

    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price('mocha'))

    def test_add_item(self):
        self.menu.add_item('mocha', 3.50)
        self.assertEqual(self.menu.get_price('mocha'), 3.50)

if __name__ == '__main__':
  unittest.main()
