import React from 'react'
import algorithms from './algorithmtypes'
import { PropTypes } from 'prop-types'

const Selection = ({ value }) => {
    return(
      <>
        <option><a href={value.url}>{value.name}</a></option> 
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

Selection.PropTypes = {
  value: PropTypes.object
}