import React from 'react'

import { DisplayInfoItem, DisplayProps } from './interfaces'

interface UserItemProp {
    user: DisplayInfoItem
}

interface ThirdLevelProps {
    openInfo: boolean;
    userInfo:DisplayInfoItem[];
}

const SecondLevelComp:React.FC<DisplayProps> = ({ openArea, openInfo, userInfo }) => {
    if (!openArea) return null

    return (
        <>
            <div>
                <div><pre>'openArea' == true </pre></div>
                <ThirdLevelComp openInfo={openInfo} userInfo={userInfo}/>
            </div>
        </>
    )
}

const ThirdLevelComp:React.FC<ThirdLevelProps> = ( {openInfo, userInfo} ) => {
    if (!openInfo) return null

    return(
        <>

            <div className="enclosed users-display">
                <div><pre>'openInfo' == true</pre></div>
                    { userInfo.map((user, idx) => 
                        <UserItem key={idx} user={user} />
                    )
                }
            </div>
        </>
    )
}

const UserItem:React.FC<UserItemProp> = ({ user }) => {
    return (
        <>  
            <div className="enclosed">
            <div className='user-box'>
                <div><b>name</b>: {user.name}</div>
                <div><b>username</b>: {user.username}</div>
                <div><b>email</b>: {user.email}</div>
            </div>
            </div>
        </>
    )
}

const DisplayOutOfMarkup:React.FC<DisplayProps> = ({ openArea, openInfo, userInfo }) => {
    return (
        <>
            <div><b>Outside of Markup</b></div>  
            <div className="enclosed">
                <SecondLevelComp openArea={openArea} openInfo={openInfo} userInfo={userInfo}/>
            </div>
        </>
    )
}

export default DisplayOutOfMarkup