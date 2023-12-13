import React, {useEffect, useState} from 'react'
import  getRandomWord  from './fiveletters_functions.js'
import './fiveletters.css'

const FiveLetters = () => {
    const [word, setWord] = useState("")
    useEffect(() => {
        const getWord = async () => {
            try {
                const randomWord = await getRandomWord()
                setWord(randomWord)
            } catch (e) {
                console.error('Error:', e.message)
            }
        }
        getWord()
    }, [])
    return (
        <>
            <div className="five-letters-page">
                FiveLetters - {word}
            </div>
        </>
    )
}

export default FiveLetters