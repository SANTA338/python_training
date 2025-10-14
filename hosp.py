import streamlit as st
import random
import time

st.set_page_config(page_title="Multi-Patient Live Monitoring", layout="wide")
st.title(" Multi-Patient Live Monitoring Dashboard")
st.write("Simulating live sensor data for multiple patients: Heart Rate, Temperature, Oxygen Level")

# --- List of patients ---
patients = ["Arun", "Meena", "John", "Priya", "Ravi"]

# --- Generator: Simulate live sensor data per patient ---
def patient_sensor_stream(patients):
    while True:
        data = []
        for p in patients:
            reading = {
                "name": p,
                "heart_rate": random.randint(60, 100),
                "temperature": round(random.uniform(97.0, 100.0), 1),  # °F
                "oxygen_level": random.randint(90, 100)
            }
            data.append(reading)
        yield data
        time.sleep(1)  # simulate real-time delay

# --- Create placeholders for each patient ---
patient_placeholders = {}
for p in patients:
    patient_placeholders[p] = {
        "container": st.container(),
        "hr_bar": None,
        "temp_bar": None,
        "ox_bar": None,
        "hr_text": None,
        "temp_text": None,
        "ox_text": None
    }

# Initialize patient sections
for p in patients:
    with patient_placeholders[p]["container"]:
        st.subheader(f" Patient: {p}")
        patient_placeholders[p]["hr_bar"] = st.progress(0, text="Heart Rate")
        patient_placeholders[p]["temp_bar"] = st.progress(0, text="Temperature")
        patient_placeholders[p]["ox_bar"] = st.progress(0, text="Oxygen Level")
        patient_placeholders[p]["hr_text"] = st.empty()
        patient_placeholders[p]["temp_text"] = st.empty()
        patient_placeholders[p]["ox_text"] = st.empty()

# --- Run live stream ---
for readings in patient_sensor_stream(patients):
    for reading in readings:
        p = reading["name"]
        hr = reading["heart_rate"]
        temp = reading["temperature"]
        ox = reading["oxygen_level"]

        # Update progress bars
        patient_placeholders[p]["hr_bar"].progress(hr, text=f"Heart Rate: {hr} bpm")
        temp_percent = int(((temp - 97) / 3) * 100)
        patient_placeholders[p]["temp_bar"].progress(temp_percent, text=f"Temperature: {temp} °F")
        patient_placeholders[p]["ox_bar"].progress(ox, text=f"Oxygen Level: {ox}%")

        # Update text values below
        patient_placeholders[p]["hr_text"].markdown(f" **Heart Rate:** {hr} bpm")
        patient_placeholders[p]["temp_text"].markdown(f" **Temperature:** {temp} °F")
        patient_placeholders[p]["ox_text"].markdown(f" **Oxygen Level:** {ox}%")

    # Sleep between updates
    time.sleep(1)
