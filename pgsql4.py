import psycopg2
con = psycopg2.connect(database="mydb", user="postgres", password="12345")
cur = con.cursor()
cur.execute(''' select customer_name, address, contact  
                from customers
                inner join orders 
                on customers.customer_id = orders.customer_id ''')
data = cur.fetchall()

cur.execute('''select customer_name, address, contact 
               from customers 
               left join orders
               on customers.customer_id = orders.customer_id''')
left_join = cur.fetchall()

cur.execute(''' select order_number, customer_name, contact, address 
                from orders 
                right join customers
                on customers.customer_id = orders.customer_id''')
right_join = cur.fetchall()

print(right_join)
print(left_join)
print(data)
