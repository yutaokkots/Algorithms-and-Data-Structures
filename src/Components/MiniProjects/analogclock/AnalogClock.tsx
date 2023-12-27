import React from 'react'
import AnalogClockFace from './AnalogClockFace'
import useCurrentTime from './useCurrentTime'
import './analogclock.css'

const AnalogClock:React.FC = () => {
    const time = useCurrentTime();
    const hr = time.getHours()
    const mn = time.getMinutes()
    const sc = time.getSeconds()

    return (
        <>
            <div className="analog-clock-page">
                <AnalogClockFace hr={hr} mn={mn} sc={sc}/>
            </div>
        </>
    )
}

export default AnalogClock