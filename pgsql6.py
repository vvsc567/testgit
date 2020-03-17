from flask import Flask, request, jsonify
import psycopg2
con = psycopg2.connect(database="mydb", user="postgres", password="12345")
cur = con.cursor()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def sample():
    try:
        if request.method == 'POST':
            cur.execute(f'''INSERT INTO customers (customer_name, customer_id, contact) 
                        VALUES ('{request.json['name']}',{request.json['customer_id']},{request.json['contact']})''')
            cur.execute('select * from customers')
            a = cur.fetchall()
            con.commit()
            cur.close()
            con.close()

            return jsonify({"details": a})

    except:
        return "somthing went wrong"


if __name__ == '__main__':
    app.run(debug=True)
