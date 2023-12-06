import React, {useState} from 'react'
import SideBar from '../Components/SideBar/SideBar'
import "./mainpage.css"

import sidebarelements from './lib/sidebarelements'
import MainBar from '../Components/MainBar/MainBar';


const MainPage = () => {
  const [selectionState, setSelectionState] = useState(0)

  const handleSelection = (index) => {
    setSelectionState(index)
  }
  
  return (
    <div className="main-screen">
        <div className="sidebar">
          <SideBar sidebarelements={sidebarelements} handleSelection={handleSelection}/>
        </div>
        <div className="mainbar">
          <MainBar sidebarelements= {sidebarelements} selectionState={selectionState} />
        </div>
    </div>
  )
}

export default MainPage