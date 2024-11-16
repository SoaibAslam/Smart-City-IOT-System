# app.py
from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY,
        temperature REAL,
        air_quality REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

# Endpoint to fetch sensor data
@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')


# Run app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)


# run Code 
# new terminal : python app.py then go to like this http://127.0.0.1:5000/
# again new terminal : python sensor_simulation.py

