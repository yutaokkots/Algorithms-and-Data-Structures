import React, {useState} from 'react'
import "./mainpage.css"
import SideBar from '../Components/SideBar/SideBar'
import MainBar from '../Components/MainBar/MainBar';
import { useCategories } from '../hooks/useCategories'

const MainPage:React.FC = () => {
  const { categories } = useCategories()

  const [selectionCategory, setSelectionCategory] = useState<string>("projects");
  const [selectionState, setSelectionState] = useState<number>(0);

  const handleSelection = (index, category) => {
    setSelectionState(index)
    setSelectionCategory(category)
  }
  
  return (
      <div className="main-screen">
          <div className="sidebar">
              <SideBar 
                  categories={categories} 
                  handleSelection={handleSelection}/>
          </div>
          <div className="mainbar">
              <MainBar 
                  categories={categories}
                  selectionCategory={selectionCategory}
                  selectionState={selectionState}/>
          </div>
      </div>
  )
}

export default MainPage