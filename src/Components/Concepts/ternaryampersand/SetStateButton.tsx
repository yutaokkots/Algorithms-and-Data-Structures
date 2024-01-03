import React from 'react'
import './ternariesampersands.css'
import { SetStateButtonOptions } from './interfaces'


const SetStateButton = ({ setState, stateInfo }:SetStateButtonOptions) => {

    const handleClick = () => {
        setState()
    }

    return (
        <>
            <input 
                className="set-state-button" 
                type="button" 
                value="Set State"
                onClick={handleClick}></input>
        </>
    )
}

export default SetStateButton