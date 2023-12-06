import React from 'react'

const MainBar = ( {sidebarelements, selectionState}) => {
    console.log(selectionState);
    return (
        <>
            {
                sidebarelements.map((element,idx) => 
                    <div key={idx} className={`${idx == selectionState ? "project-view--selected" : "project-view"}`}>
                        {element.component && <element.component />}
                    </div>
                )
            }
        </>
    )
}

export default MainBar