import React from 'react'
import solidList from './solidList'
import './solidPage.css'

interface SolidItemsProps {
    item: Item;
}

interface Item {
    name: string;
    description: string;
}

const SolidItems:React.FC<SolidItemsProps> = ({ item }) => {
    return (
        <>
            <h1>{item.name}</h1>
            <h3>"{item.description}"</h3>
        </>
    )
}

const Solid:React.FC = () => {
    return (
        <>   
            <div className="solid-page">
                {
                    solidList.map((item, idx) => 
                        <SolidItems key={idx} item={item}/>
                    )
                }
            </div>
        </>

    )
}

export default Solid