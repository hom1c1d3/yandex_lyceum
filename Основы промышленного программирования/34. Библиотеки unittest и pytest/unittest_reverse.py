import unittest
from yandex_testing_lesson import reverse  # будет доступна


class TestReverse(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse(""), "")

    def test_single_symbol(self):
        self.assertEqual(reverse("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse("хакер в реках"), "хакер в реках")

    def test_just_string(self):
        self.assertEqual(reverse("just string"), "gnirts tsuj")

    def test_wrong_type_non_iterable(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_iterable(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()