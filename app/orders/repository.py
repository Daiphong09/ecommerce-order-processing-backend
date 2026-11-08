def insert_order(cursor, order_id, total_amount):
    cursor.execute("INSERT INTO orders(order_id, total_amount) VALUES (%s,%s);", (order_id, total_amount))
def insert_order_items(cursor, order_id, order_items):
    for order_item in order_items:
        cursor.execute("INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES(%s,%s,%s,%s);", (order_id, 
                                                                        order_item["product_id"],
                                                                        order_item["quantity"], 
                                                                        order_item["unit_price"]))
