from app.orders.product_ids import extract_product_ids
from app.orders.validators import validate_create_order
from app.products.repository import get_product_rows
from app.products.mapper import map_product_rows
from app.orders.product_checks import ensure_products_exist
from app.orders.pricing import build_order_item
from app.orders.repository import insert_order, insert_order_items
def prepare_order(cursor, payload):
    items = validate_create_order(payload)
    product_ids = extract_product_ids(items)
    rows = get_product_rows(cursor, product_ids)
    products=map_product_rows(rows)
    result_products =ensure_products_exist(product_ids, products)
    order_items, amount = build_order_item(items, result_products)
    return {"order_items":order_items, "amount":amount}
def create_order(cursor,payload, order_id):
    results = prepare_order(cursor, payload)
    amount = results["amount"]
    order_items = results["order_items"]
    insert_order(cursor, order_id,amount)
    insert_order_items(cursor, order_id, order_items)
    return results