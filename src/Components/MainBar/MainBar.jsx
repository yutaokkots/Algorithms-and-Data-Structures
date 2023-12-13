import React from 'react'

const MainBar = ( {sidebarelements, selectionState}) => {

    return (
        <>
            {
                sidebarelements.map((element,idx) => 
                    <div key={idx} className={`project-display project-view ${idx == selectionState ? "project-view--selected" : ""}`}>
                        {element.component && <element.component />}
                    </div>
                )
            }
        </>
    )
}

export default MainBar