import React from 'react'
import './Cards.css'
import portraitZanang from '../Portraits/ZanangPortraitPhoto.jpg'

function Cards({name, age, occupation, bio}) {
    
    return (
        <div className="card-container">
            <div className="image-container">
                <img src={portraitZanang} alt='' />
            </div>
            <div className="card-content">
                <div className="card-name">
                    <h4>{name}</h4>
                </div>
                <div className="card-age">
                    <p> {age} </p>
                </div>
                <div className="card-occupation">
                    <p> {occupation} </p>
                </div>
                <div className="card-bio">
                    <p> {bio} </p>
                </div>
            </div>
            <div className="btn2">
                <button>
                    <a className="bio-button">
                        View Bio
                    </a>
                </button>
            </div>
        </div>
    )
}

export default Cards;