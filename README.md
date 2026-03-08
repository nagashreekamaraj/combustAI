#  CombustAI – AI-Powered Industrial Combustion Monitoring

CombustAI is a project that combines **Artificial Intelligence and IoT concepts** to monitor combustion in industrial systems.  
The goal of this project is to determine whether combustion is **complete or incomplete** by analyzing parameters such as temperature, pressure, and emission levels.

By using a trained AI model along with a real-time dashboard, CombustAI helps detect inefficient combustion conditions early and allows industries to monitor their systems more effectively.

---

##  Project Features

- Predicts **complete or incomplete combustion** using an AI model
- Displays **live sensor data** on a web dashboard
- Backend API built using **Flask**
- Interactive dashboard built using **React**
- Simulated IoT sensor data for real-time monitoring
- Alarm system simulation (buzzer) when combustion becomes inefficient
- Automatic dashboard updates every few seconds

---

##  Problem

In many industries, inefficient combustion can lead to several problems such as:

- Increased **carbon emissions**
- **Energy loss** due to incomplete burning
- Higher **fuel consumption**
- Possible safety risks and equipment damage

Industries require smart monitoring systems that can continuously analyze combustion performance and detect problems early.

---

##  Solution

CombustAI provides a **smart monitoring system** powered by AI.

The system works by:

1. Collecting combustion-related sensor data  
2. Sending the data to a backend server  
3. Using a trained AI model to analyze combustion efficiency  
4. Displaying the results on a web dashboard  
5. Triggering alerts when inefficient combustion is detected  

---

## 🧠 AI Model

The machine learning model is built using **TensorFlow** and predicts combustion efficiency based on several input parameters.

### Input Parameters
AT – Ambient Temperature
AP – Ambient Pressure
AH – Ambient Humidity
AFDP – Air Flow Differential Pressure
GTEP – Gas Turbine Exhaust Pressure
TIT – Turbine Inlet Temperature
TAT – Turbine After Temperature
TEY – Turbine Energy Yield
CDP – Compressor Discharge Pressure
CO – Carbon Monoxide Emissions
NOX – Nitrogen Oxide Emissions


### Output

Complete Combustion
or
Incomplete Combustion

