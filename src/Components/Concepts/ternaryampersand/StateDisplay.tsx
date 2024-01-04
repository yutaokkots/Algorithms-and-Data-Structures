import React from 'react'
import SetStateButton from './SetStateButton'
import SetStateDisplay from './SetStateDisplay';

interface SetStateButtonProps {
    setState: () => void;
    state: any;
    stateName: string;
}

const StateDisplay = ({ state, setState, stateName }: SetStateButtonProps) => {
  return (
    <>
        <div className="state-display">
            <SetStateButton stateInfo={state} setState={setState}/>
            <SetStateDisplay stateInfo={state} stateName={stateName} />
        </div>
    </>
  )
}

export default StateDisplay