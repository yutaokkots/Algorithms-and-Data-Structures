import React, {useState, useEffect} from 'react'
import "./trafficlight.css"
import lights from './lib/lights'
import lightObj from './lib/lightObj'

interface LightProps {
    lightObject: Lights;
    currentColor: string;
}

interface Lights {
    name: string;
    color: string;
    duration: number;
    next: string;
}

const Light:React.FC<LightProps> = ({lightObject, currentColor}) => {
    return (
        <>
            <div
                className={`light-circle`} 
                style={{ backgroundColor: currentColor == lightObject.name ? lightObject.color : "gray"}}>
            </div>
        </>
    )
}

const TrafficLight:React.FC = () => {
    const [currentColor, setCurrentColor] = useState<string>("green")
    useEffect(()=>{
        const {duration, next} = lights[lightObj[currentColor]]
        const timer = setTimeout(()=> {
            setCurrentColor(next)
        }, duration)
        return () => {
            clearTimeout(timer)
        }
    },[currentColor])

    return (
        <>
            <div className="traffic-light-page">
                <div className="traffic-light-body">
                {
                    lights.map((obj, idx) => 
                        <Light key={idx} lightObject={obj} currentColor={currentColor} />
                        )
                }
                </div>
            </div>
        </>
    )
}

export default TrafficLight