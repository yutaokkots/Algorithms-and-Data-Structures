import React from 'react'
import PropTypes from 'prop-types'

const MainBar = ({ categories, selectionCategory, selectionState }) => {
    return (
        <>
            {
                Object.keys(categories).length !== 0 && selectionCategory &&
                    categories[selectionCategory].map((element, idx) => 
                        <div 
                            key={idx} 
                            className={`project-display project-view ${idx == selectionState ? "project-view--selected" : ""}`}>
                                {element.component && <element.component />}
                        </div>
                    )
            }
        </>
    )
}

export default MainBar

MainBar.propTypes = {
    categories: PropTypes.object,
    selectionCategory: PropTypes.string,
    selectionState: PropTypes.number
  }
