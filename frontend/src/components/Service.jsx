// Example of how to map each Service
import React, { useState, useEffect } from 'react';
import InfoCard from './InfoCard'

export const Service = ({ services }) => {

    var length = services.length;
    console.log(length)

    if(length === 2) {
        return (
            <React.Fragment>
                <h1> {services[0]} </h1>
                <h3> {services[1][0].definition} </h3>
                <h3> "{services[1][0].example}" </h3>
            </React.Fragment>
        )
    } else {
        return (
            <div>
                {services.map(service => {
                    return (
                        <React.Fragment>
                            <h1 key={`${service.name}`}> {service.name} </h1>
                        </React.Fragment>
                    )
                })}
            </div>
        )
    }
    
}