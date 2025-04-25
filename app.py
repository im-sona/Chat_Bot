from flask import Flask, render_template, request, jsonify
from chat import get_response
from googletrans import Translator
import json
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    return connection

@app.get("/")
def index_get():
    return render_template("index.html")

@app.get("/app")
def chatbox_get():
    return render_template("app.py")

@app.post("/chatbox")
def chatbox_post():
    name = request.form['name']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO puser (name) VALUES (%s)', (name,))
    connection.commit()
    cursor.close()
    connection.close()
    return render_template('chatbox.html', name=name)




if __name__ == "__main__":
    app.run(debug=True)
