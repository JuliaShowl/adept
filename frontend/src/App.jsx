import { useState, useEffect } from 'react'
import './App.css'
import User from './User';
import Stats from './Stats';

function App() {
  const [user, setUser] = useState([]);
  const [stat, setStat] = useState([]);

  useEffect(() => {
    fetchUser();
    fetchStat();
  }, [] )

  const fetchUser = async () => {
    const response = await fetch("http://127.0.0.1:5000/user");
    const data = await response.json();
    setUser(data.user);
  }

  const fetchStat = async () => {
    const response = await fetch("http://127.0.0.1:5000/stats");
    const data = await response.json();
    setStat(data.stats);
  }

  return (
    <>
      <User users={user}/>
      <Stats stats={stat}/>
    </>
  )
}

export default App
