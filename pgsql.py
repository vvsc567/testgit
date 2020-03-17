import psycopg2
con = psycopg2.connect(database="mydb",
                       user="postgres",
                       password="12345")
cur = con.cursor()

cur.execute('''drop table customers''')

table_cutomers = '''CREATE TABLE customers(
                    customer_id INT PRIMARY KEY,
                    customer_name VARCHAR, 
                    contact BIGINT);'''
cur.execute(table_cutomers)

values = ''' INSERT INTO customers
             VALUES (1, 'sai' , 9856344344),
                    (2, 'harsha', 9435434344),
                    (3, 'abhiram', 9324832432)'''
cur.execute(values)

select = '''SELECT * FROM customers; '''
cur.execute(select)
data = cur.fetchall()

for i in range(len(data)):
    customer_id = data[i][0]
    customer_name = data[i][1]
    customer_number = data[i][2]
    print("id =", customer_id)
    print("name =", customer_name)
    print("number =", customer_number, "\n")

con.commit()
cur.close()
con.close()
