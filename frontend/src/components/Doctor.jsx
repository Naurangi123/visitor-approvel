import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DoctorsList = () => {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/')
      .then(response => setDoctors(response.data))
      .catch(error => console.error("Error fetching doctors: ", error));
  }, []);

  return (
    <div>
      <ul>
        {doctors.map(doctor => (
          <li key={doctor.id}>
            Dr. {doctor.first_name} {doctor.last_name} - Specialty: {doctor.specialty}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DoctorsList;
