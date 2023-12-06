import React from 'react'
import { AlgoSelection } from './AlgoSelection'
import './Navbar.css'

export default function Navbar() {
  return (
    <>
        <nav className="menu">
            <div className="title">
                    Algo
            </div>
            <div className="selector">
                <AlgoSelection />
            </div>
        </nav>
    </>
  )
}
