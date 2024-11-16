# sensor_simulation.py
import sqlite3
import random
import time

def simulate_sensor_data():
    while True:
        conn = sqlite3.connect('C:\\Users\\SOAIB ASLAM\\OneDrive\\Desktop\\Smart City IOT System\\Smart-City-IOT-System\\database.db')
        cursor = conn.cursor()
        temperature = random.uniform(15, 30)
        air_quality = random.uniform(50, 100)
        cursor.execute("INSERT INTO sensor_data (temperature, air_quality) VALUES (?, ?)", 
                       (temperature, air_quality))
        conn.commit()
        conn.close()
        print(f"Inserted data - Temperature: {temperature}, Air Quality: {air_quality}")
        time.sleep(5)

simulate_sensor_data()
