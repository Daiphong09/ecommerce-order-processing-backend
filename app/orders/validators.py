def validate_create_order(payload):
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a dict")
    items = payload.get("items")
    if items is None:
        raise ValueError("Items required")
    if not isinstance(items, list):
        raise ValueError("Items must be a list")
    if len(items) ==0:
        raise ValueError("Item cannot be empty")

    for item in items:   
        if not isinstance(item, dict):
            raise ValueError("Item must be a dict")
        productId = item.get("productId")
        if productId is None:
            raise ValueError("productId required")
        if not isinstance(productId, str):
            raise ValueError("productId must be string")
        if not productId.strip():
            raise ValueError("productId required")
        quantity = item.get("quantity")
        if quantity is None:
            raise ValueError("quantity required")
        if type(quantity) is bool:
            raise ValueError("quantity not be Boolean")
        if type(quantity) is not int:
            raise ValueError("quantity must be int")
        if quantity <=0:
            raise ValueError("quantity must be positive")
    return items

#payload không phải Dictionary	raise ValueError
    #Thiếu items	raise ValueError
    #items không phải List	raise ValueError
    #items là List rỗng	raise ValueError
    #Phần tử trong items không phải Dictionary	raise ValueError
    #Thiếu hoặc rỗng productId	raise ValueError
    #productId không phải String	raise ValueError
    #quantity không phải Integer	raise ValueError
    #quantity <= 0	raise ValueError
    #quantity là Boolean	raise ValueError
    #Tất cả hợp lệ
