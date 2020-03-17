from flask import Flask, request, jsonify
import psycopg2

con = psycopg2.connect(database="mydb", user="postgres", password="12345")
cur = con.cursor()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def sample():
        try:
            if request.method == 'POST':
                cur.execute(f'''select customer_name, contact, address
                                from customers
                                INNER JOIN orders
                                ON customers.customer_id = orders.customer_id
                                where order_number ={request.json['order']}''')
                data = cur.fetchall()
                customer_name = data[0][0]
                contact = data[0][1]
                address = data[0][2]
                return jsonify({"name": customer_name, "address": address, "contact": contact})

        except:
            return "order not found"

if __name__ == '__main__':
    app.run(debug=True)