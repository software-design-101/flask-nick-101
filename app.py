from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mariadb'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4oYwDkVNXv9cQlzEZ86b'
app.config['MYSQL_DB'] = 'contactosdb'
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos')
    data = cur.fetchall()
    return render_template('index.html', contactos=data)


@app.route('/add_contact')
def add():
    return 'Contacto'


if __name__ == '__main__':
    app.run()
