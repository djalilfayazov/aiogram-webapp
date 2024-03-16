from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


# Функция для получения данных из базы данных
def get_products():
    connection = sqlite3.connect('main.sql')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM items')
    products = cursor.fetchall()
    connection.close()
    return products


@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
