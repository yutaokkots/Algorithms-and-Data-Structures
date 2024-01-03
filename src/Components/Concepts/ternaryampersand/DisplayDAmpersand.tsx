import React, { useState } from 'react'
import StateDisplay from './StateDisplay';
import { displayInfo } from './displayInfo'
import { DisplayInfoItem } from './interfaces';


// const initialState:DisplayInfoItem[] = [{
//     "username":"",
//     "name":"",
//     "email":"",
// }]

const initialState = []

const DisplayDAmpersand:React.FC = () => {
    const [userInfo, setUserInfo] = useState<DisplayInfoItem[]>(initialState);
    const [] = useState("")
    const setState = () => {
        if (userInfo == initialState) {
            setUserInfo(displayInfo)
        } else {
            setUserInfo(initialState)
        }
    }

    return (
        <>
            <div>&&</div>
            <StateDisplay userInfo={userInfo} setState={setState}/>
            {userInfo && <></>}
        </>
    )
}

export default DisplayDAmpersand