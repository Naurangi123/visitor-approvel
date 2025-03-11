import React, { useState, useEffect } from 'react';
import axios from 'axios';


const ReactData = () => {
  const [quotes, setQuotes] = useState([]);
  const [name, setName] = useState('')
  const [detail, setDetail] = useState('')

  useEffect(() => {
    axios.get('http://localhost:8000/react')
      .then(response => setQuotes(response.data))
      .catch(error => console.error("Error fetching doctors: ", error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/react/', {name, detail})
      .then(response => {
         setQuotes([...quotes, response.data]);
         setName('');
         setDetail('');
       })
      .catch(error => console.error("Error adding doctor: ", error));
  }
  

  return (
    <>
    <div className='form_handle'>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        <label>Detail:</label>
        <input type="text" value={detail} onChange={(e) => setDetail(e.target.value)} />
        <button type="submit">Submit</button>
      </form>
    </div>
    <div className='data_form'>
      <ol>
        {quotes.map(qoute => (
          <li key={qoute.id}>
            {qoute.name} {qoute.detail}
          </li>
        ))}
      </ol>
    </div>
    </>
  );
};

export default ReactData;
