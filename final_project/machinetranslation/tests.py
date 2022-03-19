from translator import english_to_french, french_to_english
import unittest

class TestEnglishToEnglish(unittest.TestCase):
    def test_null_english(self):
        self.assertEqual(english_to_french(''), "Unable to validate payload size, the 'text' is empty.")

    def test_string_english(self):
        self.assertNotEqual(english_to_french('Hello'),'Oui')


class TestFrenchToEnglish(unittest.TestCase):
    def test_null_french(self):
        self.assertEqual(french_to_english(''),"Unable to validate payload size, the 'text' is empty.")

    def test_string_french(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Yes')

unittest.main()