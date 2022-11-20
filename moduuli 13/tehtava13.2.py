from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="lentopeli",
    user="root",
    password="kirkuk123",
    autocommit=True
)

cursor = connection.cursor()

app = Flask(__name__)


@app.route("/kenttä/<icao>")
def kentta(icao):
    sql = f'SELECT ident, NAME, municipality from airport WHERE ident = "{icao}"'
    cursor.execute(sql)
    results = cursor.fetchall()
    return {"ICAO": results[0][0], "Name": results[0][1], "Municipality": results[0][2]}


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4999)
