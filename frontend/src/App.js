import React, { Component } from 'react';
import Navbar from './components/Navbar/Navbar';
import Cards from './components/Cards';
import './App.css';


class App extends Component {
    render() {
        return (
            <div className='App'>
                <Navbar />
                <Cards 
                name='Name: Zanang Dangata'
                age='Age: 25'
                occupation='Occupation: Data Scientist'
                bio='Bio: I was born in Edinburgh and have lived in Scotland for most of my life, with brief stints in London and the US. I studied Chemical Engineering at Uni and then pursued a career in technology!'/>
            </div>
        );
    };
}
export default App;