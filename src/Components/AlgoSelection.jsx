import React from 'react'
import algorithms from './algorithmtypes'
import { PropTypes } from 'prop-types'

const Selection = ({ value }) => {

    // use react component instead of <option><a href={value.url}>{value.name}</a>
    return(
      <>
        <option>{value.name}</option> 
      </>
    )
} 

export const AlgoSelection = () => {
  return (
    <div>
      <select >
      {
        algorithms.map((value, index) => 
          <Selection key={index} value={value} />
        )
      }
      </select>
    </div>
  )
}

Selection.propTypes = {
  value: PropTypes.object
}