import psycopg2
con = psycopg2.connect(database="mydb", user="postgres", password="12345")
cur = con.cursor()


def sample(order):
    try:
        cur.execute(f'''select customer_name, contact, address
                        from customers
                        INNER JOIN orders
                        ON customers.customer_id = orders.customer_id
                        where order_number ={order}''')
        data = cur.fetchall()
        customer_name = data[0][0]
        contact = data[0][1]
        address = data[0][2]
        print(f"customer name : {customer_name}")
        print(f"customer contact number: {contact}")
        print(f"customer address: {address}")
    except IndexError:
        print("no orders found")


if __name__ == '__main__':
    order_no = int(input('enter order number'))
    sample(order_no)
