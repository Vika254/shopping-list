
from pathlib import Path
import unittest


class ShoppingListTests(unittest.TestCase):
    def setUp(self):
        self.file_path = Path(__file__).resolve().parent.parent / "shopping_list.txt"

    def test_file_exists(self):
        self.assertTrue(self.file_path.exists())

    def test_list_is_not_empty(self):
        self.assertTrue(self.file_path.read_text(encoding="utf-8").strip())

    def test_milk_is_in_list(self):
        items = self.file_path.read_text(encoding="utf-8").splitlines()
        self.assertIn("Молоко", items)


if __name__ == "__main__":
    unittest.main()
