from translator import english_to_french, french_to_english
import unittest

class TestEnglishToEnglish(unittest.TestCase):
    def test_null_english(self):
        assert english_to_french('') == "Unable to validate payload size, the 'text' is empty."

    def test_string_english(self):
        assert english_to_french('Hello') == 'Bonjour'


class TestFrenchToEnglish(unittest.TestCase):
    def test_null_french(self):
        assert french_to_english('') == "Unable to validate payload size, the 'text' is empty."

    def test_string_french(self):
        assert french_to_english('Bonjour') == 'Hello'

unittest.main()