CREATE TABLE IF NOT EXISTS products(product_id TEXT PRIMARY KEY,
                            product_cost INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS orders(order_id TEXT PRIMARY KEY, 
                    status TEXT NOT NULL DEFAULT 'PENDING_PAYMENT',
                    total_amount INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS order_items(order_id TEXT NOT NULL REFERENCES orders(order_id),
                        product_id TEXT NOT NULL REFERENCES products(product_id),
                        quantity INTEGER NOT NULL,
                        unit_price INTEGER NOT NULL,
                        PRIMARY KEY (order_id, product_id));
