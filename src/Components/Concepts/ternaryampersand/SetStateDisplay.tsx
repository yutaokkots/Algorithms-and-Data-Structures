import React from 'react'
import './ternariesampersands.css'
import { SetStateDisplayOptions } from './interfaces'

const SetStateDisplay = ({ stateInfo, stateName }: SetStateDisplayOptions) => {
    return (
        <div className="code-snippet">
            <pre>// current state </pre>
            <pre>// {stateName} </pre>
            <pre>{JSON.stringify(stateInfo, null, 2)}</pre>
        </div>
    )
}

export default SetStateDisplay