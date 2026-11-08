from dotenv import load_dotenv

from app.db.connection import get_connection
from app.db.unit_of_work import UnitOfWork
from app.orders.service import create_order

load_dotenv()

order_id = "ORD-UOW-FAIL-REBUILD-001"

payload = {
    "items": [
        {"productId": "P101", "quantity": 2},
        {"productId": "P102", "quantity": 3}
    ]
}

try:
    with UnitOfWork() as uow:
        create_order(uow.cursor, payload, order_id)

        raise RuntimeError("SIMULATED_FAILURE")

        uow.commit()

except RuntimeError as error:
    print("EXPECTED_ERROR:", error)


# Kiểm tra dữ liệu bằng Connection mới
conn = get_connection()
cur = conn.cursor()

try:
    cur.execute(
        "SELECT COUNT(*) FROM orders WHERE order_id = %s",
        (order_id,)
    )
    orders_count = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM order_items WHERE order_id = %s",
        (order_id,)
    )
    items_count = cur.fetchone()[0]

    print("ORDERS_COUNT:", orders_count)
    print("ITEMS_COUNT:", items_count)

    assert orders_count == 0
    assert items_count == 0

finally:
    cur.close()
    conn.close()