import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Appointment = () => {
  const [appoints, setAppoints] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/appointments/')
      .then(response => setAppoints(response.data))
      .catch(error => console.error("Error fetching doctors: ", error));
  }, []);

  return (
    <div>
      <ul>
        {appoints.map(appo => (
          <li key={appo.id}>
            <p>Name : Dr.{appo.doctor} </p>
            <p>Patient : {appo.patient}</p>
            <p>Reason : {appo.reason}</p>
            <p>Date : {appo.date}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Appointment;
