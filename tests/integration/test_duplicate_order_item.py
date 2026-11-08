
from dotenv import load_dotenv
from psycopg2.errors import UniqueViolation

from app.db.connection import get_connection
from app.db.unit_of_work import UnitOfWork
from app.orders.service import create_order

load_dotenv()

order_id = "ORD-DUP-ITEM-001"

payload = {
    "items": [
        {"productId": "P101", "quantity": 2},
        {"productId": "P101", "quantity": 1}
    ]
}

try:
    with UnitOfWork() as uow:
        create_order(uow.cursor, payload, order_id)
        uow.commit()

except UniqueViolation as error:
    print("EXPECTED_ERROR:", error.diag.constraint_name)

else:
    raise AssertionError("Expected UniqueViolation was not raised")

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
    conn.rollback()
    cur.close()
    conn.close()
