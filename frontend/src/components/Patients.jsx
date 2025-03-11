import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PatientList = () => {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/patients/')
      .then(response => setPatients(response.data))
      .catch(error => console.error("Error fetching patients: ", error));
  }, []);

  return (
    <div>
      <ul>
        {patients.map(patient => (
          <li key={patient.id}>
            {patient.patient_name} - Reason for Visit: {patient.reason}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PatientList;
