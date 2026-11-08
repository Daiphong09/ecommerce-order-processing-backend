import unittest

from app.orders.product_checks import ensure_products_exist


class TestProductChecks(unittest.TestCase):

    def test_all_products_exist(self):
        product_ids = ["P101", "P102"]
        products = [
            {"product_id": "P101", "product_cost": 100000},
            {"product_id": "P102", "product_cost": 50000},
        ]

        result = ensure_products_exist(product_ids, products)

        self.assertIs(result, products)

    def test_missing_product(self):
        product_ids = ["P101", "P999"]
        products = [
            {"product_id": "P101", "product_cost": 100000}
        ]

        with self.assertRaisesRegex(
            ValueError, "product_id not found: P999"
        ):
            ensure_products_exist(product_ids, products)

    def test_empty_products(self):
        result = ensure_products_exist([], [])

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()