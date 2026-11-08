def extract_product_ids(items):
    if not items:
        return []
    product_seen = set()
    product_ids = []
    for item in items:
        product_id = item["productId"]
        if product_id not in product_seen:
            product_seen.add(product_id)
            product_ids.append(product_id)
    return product_ids
        