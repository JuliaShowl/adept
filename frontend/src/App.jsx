import { useState, useEffect } from 'react'
import './App.css'
import User from './User';

function App() {
  const [user, setUser] = useState([]);

  useEffect(() => {
    fetchUser();
  }, [] )

  const fetchUser = async () => {
    const response = await fetch("http://127.0.0.1:5000/user");
    const data = await response.json();
    setUser(data.user);
  }

  return <User users={user}/>
}

export default App
