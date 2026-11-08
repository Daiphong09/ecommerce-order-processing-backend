from dotenv import load_dotenv

from app.db.connection import get_connection
from app.orders.repository import insert_order, insert_order_items

order_id = "ORD-REPO-TEST-001"

order_items = [
    {"product_id": "P101", "quantity": 2, "unit_price": 100000},
    {"product_id": "P102", "quantity": 3, "unit_price": 50000}
]
load_dotenv()
conn = get_connection()
cur = conn.cursor()

try:
    insert_order(cur, order_id, 350000)
    insert_order_items(cur, order_id, order_items)

    cur.execute(
        "SELECT COUNT(*) FROM order_items WHERE order_id = %s",
        (order_id,)
    )

    print("ITEMS:", cur.fetchone()[0])

finally:
    conn.rollback()
    cur.close()
    conn.close()