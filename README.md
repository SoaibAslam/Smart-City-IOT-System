# Smart-City-IOT-System
# Smart City IoT Dashboard

A **Smart City IoT Dashboard** that integrates IoT data, Flask-based backend, and a SQLite database 
to track environmental metrics such as temperature and air quality. The project also features simulated 
real-time sensor data for showcasing IoT capabilities.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Tech Stack](#tech-stack)
5. [Setup Instructions](#setup-instructions)
6. [How It Works](#how-it-works)
7. [API Documentation](#api-documentation)
8. [Screenshots](#screenshots)
9. [Project Directory Structure](#project-directory-structure)
10. [Challenges Encountered](#challenges-encountered)
11. [Future Improvements](#future-improvements)
12. [FAQs](#faqs)
13. [License](#license)
14. [Contact](#contact)

---

## Overview

This project demonstrates a scalable architecture for IoT applications in smart cities. By simulating 
sensor readings for environmental metrics, the application showcases how to store, retrieve, and display 
real-time data effectively.

---

## Features

- **IoT Simulation**: Generates sensor data for temperature and air quality at regular intervals.
- **Database Management**: SQLite database to persist sensor readings.
- **API Access**: Provides an endpoint to fetch the latest data for integration with other applications.
- **Web Dashboard**: User-friendly interface to view real-time data.
- **Dynamic Updates**: Refreshes data every 5 seconds (or configurable interval).

---

## Architecture

1. **Sensor Simulation**:
   - Python script mimicking IoT sensor devices.
   - Sends periodic readings to the database.

2. **Data Storage**:
   - SQLite database stores sensor data with timestamps.

3. **Backend (Flask)**:
   - Serves API endpoints for data retrieval.
   - Renders a dashboard using HTML templates.

4. **Frontend**:
   - Displays data in a clean and user-friendly layout.
   - Can be enhanced with JavaScript for dynamic updates.

---

## Tech Stack

- **Backend**: Python (Flask)
- **Database**: SQLite
- **Frontend**: HTML, CSS (Flask templates)
- **Data Simulation**: Python (random module)
- **Others**: JSON (for API responses)

---

## Setup Instructions

### Prerequisites

- Python 3.x installed.
- Basic understanding of Flask and SQLite.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SoaibAslam/smart-city-iot-dashboard.git
   cd smart-city-iot-dashboard

### How It Works :-

- **Sensor Data Simulation**: Random values for temperature and air quality are generated every 5 seconds.
- **Database Updates**: Each simulated reading is stored in the sensor_data table in SQLite.
- **API Response**: The /data endpoint returns the 10 most recent records in JSON format.
- **Frontend Rendering**: The root route (/) renders an HTML page to display the data.

### GET /data
- **Description**: Fetches the latest 10 sensor readings.

### Response:

  {
    "id": 1,
    "temperature": 25.6,
    "air_quality": 89.5,
    "timestamp": "2024-11-16 12:34:56"
  },


### Challenges Encountered

- **Data Synchronization**: Ensuring real-time updates between sensor data generation and API responses.
- **Database Management**: Avoiding database locks during concurrent read/write operations.
- **Dynamic Updates**: Designing a frontend that could auto-refresh data seamlessly.


### Future Improvements

- **Dynamic Graphs**: Add a real-time chart for better data visualization.
- **Live Updates**: Implement WebSocket for seamless updates.
- **Cloud Deployment**: Host the application on platforms like AWS, Heroku, or Azure.
- **Multi-Sensor Support**: Include data from additional sensors (e.g., humidity, light intensity).


### FAQs
- **Q: How can I extend the simulation to include more sensors?**
       Modify the sensor_simulation.py script to generate additional metrics and update the database schema in app.py.

- **Q: Can I deploy this on a server?**
    Yes, you can deploy the app using services like Heroku or AWS. Replace sqlite with a more scalable database like
    PostgreSQL for production.

- **Q: How do I change the data simulation interval?**
    Edit the time.sleep(5) line in sensor_simulation.py to your desired interval in seconds.

### License
This project is licensed under the **MIT License**. See the LICENSE file for details.



