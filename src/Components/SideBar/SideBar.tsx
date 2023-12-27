import React from 'react'
import categorySelect from '../../Pages/library/categorySelect'

const SideBarCategory = ({catName, categories, handleSelection}) => {
  return (
    <>
        {categories[catName] &&
          <>
            <div className="mini-title">
              {catName}
            </div>
            <div>
              { categories[catName] &&
              categories[catName].map((values, idx) => 
                <SideBarElement key={idx} index={idx} values={values} catName={catName} handleSelection={handleSelection} /> 
              )}
            </div>
          </>
        }
    </>
    )
}

const SideBarElement = ({values, handleSelection, catName, index}) => {
    const onClick = () => {
        handleSelection(index, catName)
    }
    return(
      <>
        <div 
            className="sidebar-selection"
            onClick={onClick} 
            >
          <div>{values.name}</div>
        </div>
      </>
    )
}

const SideBar = ({handleSelection, categories}) => {
  return (
    <>
        <div className="">
          {
            categorySelect.map((cat, idx) => 
                <SideBarCategory key={idx} catName={cat} categories={categories} handleSelection={handleSelection}/>
            )
          }
        </div>
    </>
  )
}

export default SideBar