import React, { useEffect, useState } from 'react';
import { Service } from './components/Service'
import './App.css';

function App() {
  const [service, setService] = useState([]);

  useEffect(() => {
      fetch("/operations")
      .then(res => res.json())
      .then(data => setService(data))
  }, [])

  console.log(service)

  return (
    /* Basic Mapping */
    <div className="App">
      <Service services={service}/>
    </div>
  );
}

export default App;