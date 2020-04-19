// Example of how to map each Service
import React from 'react';

export const Service = ({ services }) => {
    return (
        <div>
            {services.map(service => {
                return (
                        <div key={`${service.id}-${service.name}`}>
                            <h1 key={`${service.name}`}> {service.name} </h1>
                            <h3 key={`${service.id}`}> {service.id} </h3>
                            <h5 key={`${service.url}`}> {service.url} </h5>
                        </div>
                )
            })}
        </div>
    )
}