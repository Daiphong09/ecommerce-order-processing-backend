def get_product_rows(cursor, product_ids):
    cursor.execute("SELECT product_id, product_cost FROM products WHERE product_id=ANY(%s) ORDER BY product_id ASC;",(product_ids,))
    rows = cursor.fetchall()
    return rows
