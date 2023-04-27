from flask import Flask,render_template
import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="192.168.1.1",
                        user="postgres",
                        password="Bogota.2023",
                        port="5432")

cursor = conn.cursor()

cursor.execute('SELECT * FROM "Auditoria" LIMIT 10')
#print(cursor.fetchall())

app = Flask(__name__)

@app.route('/')
def inicio():
    return cursor.fetchall()


if  __name__ == '__main__':
    app.run(debug=True,port=5000)
    #app.run()