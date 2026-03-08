import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [result, setResult] = useState("");
  const [sensorData, setSensorData] = useState({});

  useEffect(() => {

    const interval = setInterval(async () => {

      try {

        const res = await axios.get("http://127.0.0.1:5000/latest");

        if(res.data.result){
          setResult(res.data.result);
          setSensorData(res.data.sensor_data);
        }

      } catch(err){
        console.log(err);
      }

    }, 3000);

    return () => clearInterval(interval);

  }, []);

  return (

    <div className="container">

      <h1>🔥 CombustAI</h1>
      <p>AI Powered Combustion Monitoring</p>

      <div className="card">

        <h2>Live Sensor Data</h2>

        {Object.keys(sensorData).map((key) => (
          <p key={key}>
            <b>{key}</b> : {sensorData[key]}
          </p>
        ))}

      </div>

      <div className="result">

        <h2>Status:</h2>
        <h1>{result}</h1>

      </div>

    </div>

  );
}

export default App;