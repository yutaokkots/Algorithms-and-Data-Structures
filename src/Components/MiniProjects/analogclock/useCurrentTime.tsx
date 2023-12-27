import {useState, useEffect} from 'react'

const useCurrentTime = ():Date => {
    const [time, setTime] = useState(new Date())
    useEffect(() => {
        const time = window.setInterval(() => {
            setTime(new Date())
        }, 1000)
        return () => {
            window.clearInterval(time)
        }
    }, [])
  return time
}

export default useCurrentTime