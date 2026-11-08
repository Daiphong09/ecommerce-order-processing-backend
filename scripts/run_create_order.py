
from dotenv import load_dotenv

from app.db.unit_of_work import UnitOfWork
from app.orders.service import create_order


def main():
    load_dotenv()

    order_id = "ORD-UOW-REBUILD-001"
    payload = {
        "items": [
            {"productId": "P101", "quantity": 2},
            {"productId": "P102", "quantity": 3}
        ]
    }

    with UnitOfWork() as uow:
        result = create_order(uow.cursor, payload, order_id)
        uow.commit()

    print("ORDER_ID:", order_id)
    print("RESULT:", result)


if __name__ == "__main__":
    main()
