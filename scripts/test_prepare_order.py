from dotenv import load_dotenv
from app.db.connection import get_connection
from app.orders.service import prepare_order

load_dotenv()

payload = {
    "items": [
        {"productId": "P101", "quantity": 2},
        {"productId": "P102", "quantity": 3}
    ]
}

conn = get_connection()
cur = conn.cursor()

try:
    result = prepare_order(cur, payload)

    print("AMOUNT:", result["amount"])
    print("ORDER_ITEMS:", result["order_items"])

finally:
    conn.rollback()
    cur.close()
    conn.close()