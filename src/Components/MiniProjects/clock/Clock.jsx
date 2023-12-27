import React, {useEffect, useState} from 'react'
import "./clock.css"

const timeDigits = {
    1: {
        top:"right",
        mid:"",
        bot:"right"
    },
    2: {
        top:"right top",
        mid:"center",
        bot:"left bottom"
    },
    3: {
        top:"top right",
        mid:"center",
        bot:"bottom right"
    },
    4: {
        top:"left right",
        mid:"center",
        bot:"right"
    },
    5: {
        top:"left top",
        mid:"center",
        bot:"bottom right"
    },
    6: {
        top:"left top",
        mid:"center",
        bot:"left bottom right"
    },
    7: {
        top:"top right",
        mid:"",
        bot:"right"
    },
    8: {
        top:"left top right",
        mid:"center",
        bot:"left bottom right"
    },
    9: {
        top:"left top right",
        mid:"center",
        bot:"bottom right"
    },
    0: {
        top:"left top right",
        mid:"",
        bot:"left bottom right"
    }
}


const useCurrentTime = () => {
    const [time, setTime] = useState(new Date())
    useEffect(() => {
        const time = window.setInterval(()=>{
            setTime(new Date())
        }, 1000)
        return () => {
            window.clearInterval(time)
        }
    }, [])
    return time
}

const adjustZero = (digitStr) => {
    if (digitStr.toString().length < 2){
        digitStr = `0${digitStr}`;
    }
    return digitStr
}

const Digit = ({val}) => {
    const timeDigit = timeDigits[val]
  return (
    <>
        <div className="digit">
        {
            val == ":" 
            ?
            <div className="colon">
                <div className="top-dot"></div>
                <div className="bottom-dot"></div>
            </div>
            :
            <div className="">
                <div className={`digit-top ${timeDigit.top}`}></div>
                <div className={`digit-middle ${timeDigit.mid}`}></div>
                <div className={`digit-bottom ${timeDigit.bot}`}></div>
            </div>
        }
        </div>
     </>
  )
}

const Clock = () => {
    const time = useCurrentTime()
    
    const hr = adjustZero(time.getHours())
    const mn = adjustZero(time.getMinutes())
    const sc = adjustZero(time.getSeconds())

    
    const clock = (`${hr}:${mn}:${sc}`).split("")

    return (
        <>
            <div className="clock-page">
                <div className="clock-face">
                {
                    clock.map((val, idx) => 
                        <Digit key={idx} val={val} />
                    )
                }
                </div>
                <div className="table">

                </div>
            </div>
        </>
    )
}

export default Clock