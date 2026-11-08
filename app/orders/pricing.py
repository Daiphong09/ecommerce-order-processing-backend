
# output order_items, total_amount
def build_order_item(items, products):
    total_amount =0
    order_items =[]
    #Xây dựng cơ chế tìm product_cost tương ứng với từng productId.
    #Duyệt qua items và lấy quantity từ Request.
    for item in items:
        product_id = item.get("productId")
        quantity = item.get("quantity")
        for product in products:
            if product["product_id"] == product_id:
                product_cost = product["product_cost"]
    #Tính subtotal = quantity * product_cost.
                subtotal = quantity* product_cost
    #Cộng các subtotal thành total_amount.
                total_amount += subtotal
        order_item = {"product_id":product_id,"quantity":quantity, "unit_price":product_cost, "subtotal":subtotal}
        order_items.append(order_item)
    return order_items, total_amount
    #Trả về đúng Tuple (order_items, total_amount).
    # Nếu items = [], trả về ([], 0)
