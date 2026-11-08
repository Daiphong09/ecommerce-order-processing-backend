
from dotenv import load_dotenv

from app.db.connection import get_connection
from app.db.unit_of_work import UnitOfWork
from app.orders.service import create_order

load_dotenv()

order_id = "ORD-UOW-NO-COMMIT-001"

payload = {
    "items": [
        {"productId": "P101", "quantity": 2},
        {"productId": "P102", "quantity": 3}
    ]
}

with UnitOfWork() as uow:
    result = create_order(uow.cursor, payload, order_id)
    print("AMOUNT:", result["amount"])

    # KHÔNG gọi uow.commit()

# Kiểm tra bằng một Connection mới
conn = get_connection()
cur = conn.cursor()

try:
    cur.execute(
        "SELECT COUNT(*) FROM orders WHERE order_id = %s",
        (order_id,)
    )
    print("ORDERS_COUNT:", cur.fetchone()[0])

    cur.execute(
        "SELECT COUNT(*) FROM order_items WHERE order_id = %s",
        (order_id,)
    )
    print("ITEMS_COUNT:", cur.fetchone()[0])

finally:
    cur.close()
    conn.close()
