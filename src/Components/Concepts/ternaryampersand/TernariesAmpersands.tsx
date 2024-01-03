import React from 'react'
import DisplayDAmpersand from './DisplayDAmpersand'
import './ternariesampersands.css'

const TernariesAmpersands = () => {
    return (
        <div className="ternaries-page">
            <h2>The case against Ternaries (?:) and double-ampersands (&&) in JSX code</h2>
            <h3>Three Examples</h3>
            <div className="container-examples">
                <div className="example-d-ampersand">
                    <DisplayDAmpersand/>
                </div>
                <div className="example-d-ampersand">Example</div>
                <div className="example-d-ampersand">Example</div>
            </div>
        </div>
    )
}

export default TernariesAmpersands