import React from 'react';
import { Header } from './components/Header'
import Navbar from './components/navbar'
import {BrowserRouter as Router}  from 'react-router-dom'

function App() {
  return (
    <Router>
      <Navbar />
    </Router>
  );
}

export default App;
