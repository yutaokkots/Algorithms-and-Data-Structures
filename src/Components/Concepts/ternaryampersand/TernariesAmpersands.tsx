import React, { useState } from 'react'
import DisplayDAmpersand from './DisplayDAmpersand'
import StateDisplay from './StateDisplay';
import { displayInfo } from './displayInfo'
import { DisplayInfoItem } from './interfaces';
import './ternariesampersands.css'
import DisplayTernary from './DisplayTernary';
import DisplayOutOfMarkup from './DisplayOutOfMarkup';
import CodeDisplay from './CodeDisplay';
import { dampersandCode, ternaryCode, outsideMarkupCode} from './displayCode'

// reference: https://www.youtube.com/watch?app=desktop&v=mOwZhb9bZ5s

const initialUserInfoState = []

const codeSnippetArr = [dampersandCode, ternaryCode, outsideMarkupCode]

const TernariesAmpersands = () => {
    const [openArea, setOpenArea] = useState<boolean>(true)
    const [openInfo, setOpenInfo] = useState<boolean>(true)
    const [userInfo, setUserInfo] = useState<DisplayInfoItem[] | []>(initialUserInfoState);
  
    const setOpenAreaState = () => {
        setOpenArea(!openArea)
    }

    const setOpenInfoState = () => {
        setOpenInfo(!openInfo)
    }

    const setUserInfoState= () => {
        if (userInfo == initialUserInfoState) {
            setUserInfo(displayInfo)
        } else {
            setUserInfo(initialUserInfoState)
        }
    }

    return (
        <div className="ternaries-page">
            <h2>The case against Ternaries (?:) and double-ampersands (&&) in JSX code</h2>
            <div className="state-display-container">
                <StateDisplay state={openArea} setState={setOpenAreaState} stateName={"openArea"}/>
                <StateDisplay state={openInfo} setState={setOpenInfoState} stateName={"openInfo"}/>
                <StateDisplay state={userInfo} setState={setUserInfoState} stateName={"userInfo"}/>
            </div>

            <h3>Three Examples</h3>
            <div className="container-examples">
                <div className="example-d-ampersand">
                    <DisplayDAmpersand 
                        openArea={openArea} 
                        openInfo={openInfo} 
                        userInfo={userInfo}/>
                </div>
                <div className="example-d-ampersand">
                    <DisplayTernary
                        openArea={openArea} 
                        openInfo={openInfo} 
                        userInfo={userInfo}/>
                </div>
                <div className="example-d-ampersand">
                    <DisplayOutOfMarkup 
                        openArea={openArea} 
                        openInfo={openInfo} 
                        userInfo={userInfo}/>
                </div>
            </div>
            <h3>Code</h3>
            <div className="state-display-container">
                <CodeDisplay codeSnippet={codeSnippetArr}/>

            </div>
        </div>
    )
}

export default TernariesAmpersands