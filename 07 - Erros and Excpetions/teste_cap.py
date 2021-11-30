import unittest
import cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'pedro lisboa'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Pedro Lisboa')


if __name__ == '__main__':
    unittest.main()
