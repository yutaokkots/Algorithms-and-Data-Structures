import React from 'react'
import SetStateButton from './SetStateButton'
import SetStateDisplay from './SetStateDisplay';

interface SetStateButtonProps {
    setState: () => void
    userInfo: any
}


const StateDisplay = ({ userInfo, setState }: SetStateButtonProps) => {
  return (
    <>
        <div className="state-display">
            <SetStateButton stateInfo={userInfo} setState={setState}/>
            <SetStateDisplay stateInfo={userInfo} />
        </div>
    </>
  )
}

export default StateDisplay