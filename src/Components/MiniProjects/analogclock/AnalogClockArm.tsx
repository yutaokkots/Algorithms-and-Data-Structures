import React from 'react'
import { AnalogClockArmProps } from './analogClockTypes';

const AnalogClockArm:React.FC<AnalogClockArmProps> = ({ height, degree, width }) => {
    return (
    <>    
        <div 
            className="analog-clock-arm"
            style={{height:`${height}px`, 
                    transform:`rotate(${degree+180}deg)`, 
                    width:`${width}px`}}>
        </div>
    </>
  )
}

export default AnalogClockArm;