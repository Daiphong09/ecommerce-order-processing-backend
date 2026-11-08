

def map_product_rows(rows):
    products = []
    for row in rows:
        product_id = row[0]
        product_cost = row[1]
        result = {"product_id":product_id, "product_cost":product_cost}
        products.append(result)
    return products

#if __name__=="__main__":
    #rows_empty =[]
    #rows= [("P101",100000), ("P102", 50000), ("P999", 77777)]
    #print(f"CHECK_EMPTY: {map_product_rows(rows=rows_empty)}")
    #print(f"PRODUCTS: {map_product_rows(rows=rows)}")
        