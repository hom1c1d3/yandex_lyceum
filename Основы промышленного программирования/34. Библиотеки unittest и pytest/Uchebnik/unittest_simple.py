from unittest import TestCase
from reverse import reverse


class TestRevers(TestCase):

    def test_empty(self):
        self.assertEqual(reverse(""), "")

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)