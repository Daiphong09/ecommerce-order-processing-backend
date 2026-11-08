import unittest
from app.orders.validators import validate_create_order
class TestCreateOrderValidation(unittest.TestCase):
    def test_valid_payload(self):
        items = [
            {"productId": "P101", "quantity": 2},
            {"productId": "P102", "quantity": 3}
        ]
        result = validate_create_order({"items": items})
        self.assertIs(result, items)
    def test_invalid_payloads(self):
        invalid_cases = [
            None,
            {},
            {"items": "invalid"},
            {"items": []},
            {"items": [123]},
            {"items": [{"quantity": 2}]},
            {"items": [{"productId": "   ", "quantity": 2}]},
            {"items": [{"productId": "P101", "quantity": True}]},
            {"items": [{"productId": "P101", "quantity": "2"}]},
            {"items": [{"productId": "P101", "quantity": 0}]},
            {"items": [{"productId": "P101", "quantity": -1}]},
        ]
        for payload in invalid_cases:
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    validate_create_order(payload)
if __name__ == "__main__":
    unittest.main()