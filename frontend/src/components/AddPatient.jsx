import React, { useState } from 'react';
import axios from 'axios';

const CreatePatient = () => {
  const [patient, setPatient] = useState({
    patient_name: '',
    address: '',
    gender: '',
    contact: '',
    age:"",
    blood: '',
    reason_for_visit: ''
  });

  const handleChange = (e) => {
    setPatient({
      ...patient,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/patients/', patient)
      .then(response => {
        alert('Patient successfully created');
        setPatient({
          first_name: '',
          last_name: '',
          date_of_birth: '',
          contact_number: '',
          reason_for_visit: ''
        });
      })
      .catch(error => console.error('Error creating patient:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        First Name:
        <input
          type="text"
          name="first_name"
          value={patient.first_name}
          onChange={handleChange}
        />
      </label>
      <label>
        Last Name:
        <input
          type="text"
          name="last_name"
          value={patient.last_name}
          onChange={handleChange}
        />
      </label>
      <label>
        Date of Birth:
        <input
          type="date"
          name="date_of_birth"
          value={patient.date_of_birth}
          onChange={handleChange}
        />
      </label>
      <label>
        Contact Number:
        <input
          type="text"
          name="contact_number"
          value={patient.contact_number}
          onChange={handleChange}
        />
      </label>
      <label>
        Reason for Visit:
        <textarea
          name="reason_for_visit"
          value={patient.reason_for_visit}
          onChange={handleChange}
        />
      </label>
      <button type="submit">Create Patient</button>
    </form>
  );
};

export default CreatePatient;
