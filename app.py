# app.py
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        db = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', ''),
            database=os.environ.get('DB_NAME', 'testdb')
        )
        cursor = db.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        return f"MySQL connected! Current time: {result[0]}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
