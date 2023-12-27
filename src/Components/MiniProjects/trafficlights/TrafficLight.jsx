import React, {useState, useEffect} from 'react'
import "./trafficlight.css"

const lights = [
    {
        name: "red",
        color: "#610c04",
        duration: 6000,
        next: "green"
    },
    {
        name: "yellow",
        color: "#E9D700",
        duration: 1500,
        next: "red"
    },
    {
        name: "green",
        color: "#005900",
        duration: 5000,
        next: "yellow"
    }
]
const lightObj = {
    "green": 2,
    "yellow": 1,
    "red": 0
}

const Light = ({lightObject, currentColor}) => {
    return (
        <>
            <div
                className={`light-circle`} 
                style={{ backgroundColor: currentColor == lightObject.name ? lightObject.color : "gray"}}>
            </div>
        </>
    )
}


const TrafficLight = () => {
    const [currentColor, setCurrentColor] = useState("green")
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