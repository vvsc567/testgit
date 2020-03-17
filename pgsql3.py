import psycopg2
con = psycopg2.connect(database="mydb", user="postgres", password="12345")
cur = con.cursor()
n = int(input("enter number of rows"))
print("enter the customer data: ")
for i in range(n):
    customer_id = int(input("enter customer id: "))
    name = str(input("enter customer name: "))
    name1 = f" '{name}' "
    contact = int(input("enter contact number: "))
    cur.execute(f'''INSERT INTO customers (customer_id, customer_name, contact)
                    VALUES ({customer_id},{name1},{contact})
                ''')
con.commit()
cur.close()
con.close()
print("\nvalues inserted")
