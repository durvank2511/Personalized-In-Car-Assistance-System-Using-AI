import streamlit as st
import pandas as pd
import numpy as np
import time

# Set the page configuration
st.set_page_config(page_title="In-Car AI Assistant", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Sensor Data Visualization", "Driving Alerts", "Smart Device Integration"])

# Home Section
if menu == "Home":
    st.title("Personalized In-Car Assistance System")
    st.markdown("""
    Welcome to the Personalized In-Car AI Assistant!  
    This app demonstrates the following features:  
    - *Sensor Data Visualization*: Real-time monitoring of vehicle health.  
    - *Driving Behavior Alerts*: Detect unsafe driving actions.  
    - *Smart Device Integration*: Mock commands for smart devices.  
    Use the navigation menu to explore each feature.
    """)

# Sensor Data Visualization
elif menu == "Sensor Data Visualization":
    st.title("Sensor Data Visualization")
    st.write("Simulated data showing vehicle health metrics.")

    # Simulate sensor data
    def simulate_data():
        data = {
            "Tire Pressure (PSI)": np.random.randint(28, 36),
            "Oil Level (%)": np.random.randint(20, 100),
            "Engine Temperature (°C)": np.random.randint(70, 120),
            "Battery Voltage (V)": np.random.uniform(11.5, 14.5)
        }
        return data

    # Display real-time sensor data
    placeholder = st.empty()
    for _ in range(10):  # Simulates 10 updates
        sensor_data = simulate_data()
        df = pd.DataFrame([sensor_data])
        placeholder.table(df)
        time.sleep(2)  # Update every 2 seconds

# Driving Behavior Alerts
elif menu == "Driving Alerts":
    st.title("Driving Behavior Alerts")
    st.write("Simulated alerts based on driving behavior.")

    # Alert conditions
    alerts = {
        "Speeding": "Speed exceeded 120 km/h.",
        "Drowsiness": "Drowsy driving detected from eye closure.",
        "Aggressive Driving": "Sudden acceleration and braking detected.",
        "Proximity Alert": "Vehicle too close to an obstacle."
    }

    # Mock data for alerts
    alert_trigger = np.random.choice(list(alerts.keys()))
    st.warning(f"🚨 Alert: {alerts[alert_trigger]}")

# Smart Device Integration
elif menu == "Smart Device Integration":
    st.title("Smart Device Integration")
    st.write("Simulated voice commands for smart devices.")

    # Dropdown for mock commands
    commands = ["Play Music", "Adjust Thermostat", "Turn Off Lights", "Remind Me Later"]
    command = st.selectbox("Choose a command", commands)

    # Mock response
    responses = {
        "Play Music": "🎵 Playing your favorite playlist.",
        "Adjust Thermostat": "🌡 Adjusting home thermostat to 22°C.",
        "Turn Off Lights": "💡 Turning off all home lights.",
        "Remind Me Later": "⏰ Reminder set for later."
    }
    if command:
        st.success(f"Response: {responses[command]}")