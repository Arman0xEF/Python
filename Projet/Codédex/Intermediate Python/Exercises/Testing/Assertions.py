import unittest

def reverse_string(s):
  return s[::-1]

def capitalize_string(s):
  return s.capitalize()

def is_capitalized(s):
  return s[0].isupper()


class MyTestCase(unittest.TestCase):
  def test_reverse_string(self):
    result = reverse_string('Hello')
    self.assertEqual(result, 'olleH')      

  def test_capitalize_string(self):
    text = capitalize_string('hello')
    self.assertEqual(text, 'Hello')  

  def test_text_contains_word(self):
    self.assertTrue(is_capitalized('hello'))  
   

if __name__ == '__main__':
  unittest.main()
