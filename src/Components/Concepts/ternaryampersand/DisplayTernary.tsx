import React  from 'react'
import { DisplayInfoItem, DisplayProps } from './interfaces'

interface UserItemProp {
    user: DisplayInfoItem
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

const DisplayTernary:React.FC<DisplayProps> = ({ openArea, openInfo, userInfo }) => {
    return (
        <>
            <div><b>?:</b></div>
            <div>
                <div className='information-area'>
                    {openArea ?
                        <>  
                            <div><pre>'openArea' == true </pre></div>
                            {openInfo ?
                                <>
                                <div className="enclosed users-display">
                                    <div><pre>'openInfo' == True</pre></div>
                                        { userInfo.map((user, idx) => 
                                            <UserItem key={idx} user={user} />
                                        )
                                    }
                                </div>
                                </>
                                :
                                null
                            }
                        </>
                        :
                        null
                    }
                </div>
            </div>
        </>  
    )
}

export default DisplayTernary