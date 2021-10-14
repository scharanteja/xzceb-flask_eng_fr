from translator import english_to_french,french_to_english
import unittest


class Tests(unittest.TestCase):
      def test(self):     
               self.assertEqual(english_to_french("Hello"),"Bonjour")
      def test1(self):
               self.assertEqual(french_to_english("Bonjour"),"Hello")
      def test2(self):
               self.assertEqual(english_to_french("  "),"  ")
      def test3(self):
                self.assertEqual(french_to_english("  "),"  ")
#print(english_to_french("Hello"))

if __name__=='__main__':
      unittest.main()