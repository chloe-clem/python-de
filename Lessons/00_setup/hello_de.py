import duckdb

print("Hello, data engineer!")

orders = duckdb.query("""
    SELECT * FROM (VALUES
       (1, 'Anna',  120.50),
        (2, 'Bram',   75.00),
        (3, 'Anna',   49.99),
        (4, 'Daan',  210.00)
    ) AS t(order_id, customer, amount)
    """)

print(orders)

print(duckdb.sql("""
    SELECT customer, SUM(amount) AS total
    FROM orders
    GROUP BY customer
    HAVING total > 100
    ORDER BY total DESC
"""))
