"""Unit tests for the shopping_cart module."""
import unittest
from shopping_cart import calculate_total


class TestCalculateTotal(unittest.TestCase):
    """Tests for the calculate_total function."""

    def test_total_with_floats(self):
        """Test correct total with standard float prices."""
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
        ]
        result = calculate_total(cart)
        self.assertAlmostEqual(result, 16.98, places=2)

    def test_total_with_string_prices(self):
        """Test that string prices are correctly converted to float."""
        cart = [
            {'name': 'Item A', 'price': '8.49'},
            {'name': 'Item B', 'price': '2.00'},
        ]
        result = calculate_total(cart)
        self.assertAlmostEqual(result, 10.49, places=2)

    def test_empty_cart(self):
        """Test that an empty cart returns 0."""
        cart = []
        result = calculate_total(cart)
        self.assertEqual(result, 0)

    def test_single_item(self):
        """Test cart with a single item."""
        cart = [{'name': 'Item A', 'price': 19.99}]
        result = calculate_total(cart)
        self.assertAlmostEqual(result, 19.99, places=2)

    def test_total_with_mixed_types(self):
        """Test cart with both float and string prices."""
        cart = [
            {'name': 'Item A', 'price': 10.00},
            {'name': 'Item B', 'price': '5.50'},
        ]
        result = calculate_total(cart)
        self.assertAlmostEqual(result, 15.50, places=2)

    def test_full_cart(self):
        """Test the default CART from the module."""
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49},
        ]
        result = calculate_total(cart)
        self.assertAlmostEqual(result, 25.47, places=2)


if __name__ == '__main__':
    unittest.main()
