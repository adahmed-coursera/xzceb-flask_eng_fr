from translator import englishToFrench, frenchToEnglish
import unittest


class TestEnglishToEnglish(unittest.TestCase):
    def test_null_english(self):
        self.assertEqual(englishToFrench(''), "Unable to validate payload size, the 'text' is empty.")

    def test_string_english(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test_null_french(self):
        self.assertEqual(frenchToEnglish(''), "Unable to validate payload size, the 'text' is empty.")

    def test_string_french(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()