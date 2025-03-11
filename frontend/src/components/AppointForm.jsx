import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AppointForm = () => {
  const [patients, setPatients] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [appointment, setAppointment] = useState({
    patient: '',
    doctor: '',
    appointment_date: '',
    reason_for_visit: ''
  });
  const [error, setError] = useState(null);

  // Fetch patients from the backend
  const fetchPatients = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/patients/');
      setPatients(response.data);
      console.log(response.data);
      
    } catch (error) {
      console.error('Error fetching patients: ', error);
      setError(error);
    }
  };

  // Fetch doctors from the backend
  const fetchDoctors = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/doctors/');
      setDoctors(response.data);
      console.log(response.data);
    } catch (error) {
      console.error('Error fetching doctors: ', error);
      setError(error);
    }
  };

  // Run the fetch functions when the component is mounted
  useEffect(() => {
    fetchPatients();
    fetchDoctors();
  }, []);

  // Handle changes to form fields
  const handleChange = (e) => {
    setAppointment({
      ...appointment,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
  
    const appointmentData = {
      doctor: { id: appointment.doctor },  // Send doctor as an object with id
      patient: { id: appointment.patient, reason_for_visit: appointment.reason_for_visit },  // Send patient as an object with id and reason_for_visit
      appointment_date: appointment.appointment_date,
    };
  
    axios
      .post('http://localhost:8000/appointments/', appointmentData)
      .then((response) => {
        console.log(response.data);
        alert('Appointment successfully created');
        setAppointment({
          patient: '',
          doctor: '',
          appointment_date: '',
          reason_for_visit: '',
        });
      })
      .catch((error) => {
        console.error('Error creating appointment:', error);
        alert('Error creating appointment. Please try again.');
      });
  };
  

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Patient:
        <select name="patient" onChange={handleChange} value={appointment.patient}>
          <option value="">Select a patient</option>
          {patients.map((patient) => (
            <option key={patient.id} value={patient.id}>
              {patient.first_name} {patient.last_name}
            </option>
          ))}
        </select>
      </label>

      <label>
        Doctor:
        <select name="doctor" onChange={handleChange} value={appointment.doctor}>
          <option value="">Select a doctor</option>
          {doctors.map((doctor) => (
            <option key={doctor.id} value={doctor.id}>
              Dr. {doctor.first_name} {doctor.last_name} ({doctor.specialty})
            </option>
          ))}
        </select>
      </label>

      <label>
        Appointment Date:
        <input
          type="datetime-local"
          name="appointment_date"
          value={appointment.appointment_date}
          onChange={handleChange}
        />
      </label>

      <label>
        Reason for Visit:
        <textarea
          name="reason_for_visit"
          value={appointment.reason_for_visit}
          onChange={handleChange}
        />
      </label>

      <button type="submit">Create Appointment</button>

      {error && <p className="error">There was an error: {error.message}</p>}
    </form>
  );
};

export default AppointForm;
