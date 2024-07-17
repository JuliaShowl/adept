import { useState, useEffect } from 'react'
import './App.css'
import User from './User';
import Stats from './Stats';
import Docs from './Docs';

function App() {
  const [user, setUser] = useState([]);
  const [stat, setStat] = useState([]);
  const [doc, setDoc] = useState([]);

  useEffect(() => {
    fetchUser();
    fetchStat();
    fetchDoc();
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

  const fetchDoc = async () => {
    const response = await fetch("http://127.0.0.1:5000/documents");
    const data = await response.json();
    setDoc(data.docs);
  }


  return (
    <>
      <User users={user}/>
      <Stats stats={stat}/>
      <Docs docs={doc}/>
    </>
  )
}

export default App
