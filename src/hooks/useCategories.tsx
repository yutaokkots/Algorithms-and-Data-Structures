import React from 'react'
import {useEffect, useState} from "react"

import sidebarelements from '../Pages/library/sidebarelements'
import sidebarconcepts from '../Pages/library/sidebarconcepts'

interface CategoryType {
    [key:string]:any 
}

export const useCategories = () => {
    const [categories, setCategories] = useState<CategoryType>({})
    const getCategories = async () => {
        let elements = {...sidebarelements, ...sidebarconcepts}
        setCategories(elements)
    }
    useEffect(() => {
        getCategories();
    }, [])
    return { categories }
}
