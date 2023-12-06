import React from 'react'


const SideBarElement = ({values, handleSelection, index}) => {

    const onClick = () => {
        handleSelection(index)
    }
    return(
      <>
        <div 
            className="sidebar-selection"
            onClick={onClick} 
            value={index}
            >
          <div>{values.project}</div>
        </div>
      </>
    )
}

const SideBar = ({sidebarelements, handleSelection}) => {
  return (
    <>
        <div className="">
            <div className="mini-title">
                Mini-projects
            </div>
            <div>
              {
                sidebarelements.map((values, idx) => 
                  <SideBarElement key={idx} index={idx} values={values} handleSelection={handleSelection} /> 
                )
              }
            </div>
            
        </div>
    </>
  )
}

export default SideBar