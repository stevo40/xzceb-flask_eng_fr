import unittest

from machinetranslation import translator

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(translator.englishToFrench(''), '')

    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(translator.frenchToEnglish(''), '')

if __name__ == '__main__':
    unittest.main()

