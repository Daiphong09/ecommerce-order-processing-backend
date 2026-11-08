def ensure_products_exist(product_ids, products):   
    response_ids= set()
    for product in products:
        response_ids.add(product["product_id"]) 
    for product_id in product_ids:
        if product_id not in response_ids:
            raise ValueError(f"product_id not found: {product_id}")
    return products