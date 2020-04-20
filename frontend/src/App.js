import React, { useEffect, useState } from 'react';
import Splash from './media/Splash.png'
import { Service } from './components/Service'
import './App.css';

function App() {
  const [service, setService] = useState([]);
  var path = window.location.pathname.substr(4, window.location.pathname.length);


  useEffect(() => {
      fetch(path)
      .then(res => res.json())
      .then(data => setService(data))
  }, [])
    console.log(service)
  return (
    <div className="App" style={{backgroundColor: "darkRed"}}>
      {/* <img src={Splash} /> */}
      <Service services={service} />
    </div>
  );
}

export default App;