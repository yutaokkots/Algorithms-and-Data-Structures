import React from 'react';
import AnalogClockArm from './AnalogClockArm';
import AnalogClockCover from './AnalogClockCover';
import { AnalogClockFaceProps } from './analogClockTypes';
import timeArms from './analogclockarms';

// 'sector' defines the sector of a clock (30°)
const sector= 30;

const AnalogClockFace:React.FC<AnalogClockFaceProps> = ({ hr, mn, sc }) => {
    const hour = hr * sector + (mn / 60) * sector;
    const min = mn / 60 * 360;
    const sec = sc / 60 * 360;
    return (
        <>
            <div 
                className="analog-clock-face">
                <AnalogClockArm height={timeArms.hr.height} degree={hour} width={timeArms.hr.width}/>
                <AnalogClockArm height={timeArms.mn.height} degree={min} width={timeArms.mn.width}/>
                <AnalogClockArm height={timeArms.sc.height} degree={sec} width={timeArms.sc.width}/>
                <AnalogClockCover />
            </div>
        </>
    )
}

export default AnalogClockFace;