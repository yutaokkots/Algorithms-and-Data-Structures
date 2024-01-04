export const ternaryCode: string = `
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
                                    <div><pre>'openInfo' == true</pre></div>
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

export default DisplayTernary;
`;

export const dampersandCode: string = `
const DisplayDAmpersand:React.FC<DisplayProps> = ({ openArea, openInfo, userInfo }) => {
    return (
        <>
            <div><b>&&</b></div>
            <div>
                <div className='information-area'>
                    {openArea && 
                        <>  
                            <div><pre>'openArea' == true </pre></div>
                            {openInfo && 
                            <>
                            <div className="enclosed users-display">
                                <div><pre>'openInfo' == true</pre></div>
                                    { userInfo.map((user, idx) => 
                                        <UserItem key={idx} user={user} />
                                    )
                                }
                            </div>
                            </>
                            }
                        </>
                    }
                </div>
            </div>
        </>
    )
}

export default DisplayDAmpersand;
`;

export const outsideMarkupCode: string = `
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

export default DisplayOutOfMarkup;
`