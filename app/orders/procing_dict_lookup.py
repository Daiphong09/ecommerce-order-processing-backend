items =[
    {"productId": "P101", "quantity": 2},
    {"productId": "P102", "quantity": 3}
]
items_1 = []
products=[
    {"product_id": "P101", "product_cost": 100000},
    {"product_id": "P102", "product_cost": 50000}
]

def build_order_item(items, products):
    total_amount =0
    order_items = []
    product_map = {}
    for product in products:
        product_map[product["product_id"]] = product["product_cost"]
    for item in items:
        product_id = item.get("productId")
        quantity = item.get("quantity")
        unit_price = product_map[product_id]
        subtotal = unit_price*quantity
        total_amount += subtotal
        order_item = {"product_id":product_id, "quantity":quantity, "unit_price":unit_price, "subtotal":subtotal}
        order_items.append(order_item)
    return order_items, total_amount
if __name__=="__main__":
    print(build_order_item(items, products))