import psycopg2
con = psycopg2.connect(database="mydb",
                       user="postgres",
                       password="12345")

cur = con.cursor()

table_orders = '''CREATE TABLE orders(
                    order_number INT PRIMARY KEY,
                    customer_id INT,
                    address VARCHAR,
                    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
                    );'''
cur.execute(table_orders)

cur.execute('''INSERT INTO orders 
               VALUES (12, 1, 'hyderabad'),
                      (13, 1, 'hyderabad'),
                      (14, 2, 'vijayawada');
            ''')
con.commit()
cur.close()
con.close()