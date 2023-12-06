import { useState } from 'react'
import './App.css'
import { Routes, Route } from 'react-router-dom';
import Navbar from '../Components/Navbar'
import SlidingWindow from './CodingPages/SlidingWindow';
import TwoPointers from './CodingPages/TwoPointers';
import FastSlowPointers from './CodingPages/FastSlowPointers';
import MergeIntervals from './CodingPages/MergeIntervals';
import CycleSort from './CodingPages/CycleSort';
import InPlaceRevLinkedList from './CodingPages/InPlaceRevLinkedList';
import TreeBreadthFirstSearch from './CodingPages/TreeBreadthFirstSearch';
import TreeDepthFirstSearch from './CodingPages/TreeDepthFirstSearch';
import TwoHeaps from './CodingPages/TwoHeaps';
import Subsets from './CodingPages/Subsets';
import ModifiedBinarySearch from './CodingPages/ModifiedBinarySearch';
import TopKElements from './CodingPages/TopKElements';
import KWayMerge from './CodingPages/KWayMerge';
import TopoSort from './CodingPages/TopoSort';
import MainPage from './MainPage';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
        <header>
          <Navbar />
        </header>
        <main>
            <>
              
              <Routes>
                  <Route path="/" element={<MainPage />} />
                  <Route path="/:paramId/01-sliding-window"                    element={<SlidingWindow />} />
                  <Route path="/:paramId/02-two-pointers"                      element={<TwoPointers />} />
                  <Route path="/:paramId/03-fast-and-slow-pointers"            element={<FastSlowPointers />} />
                  <Route path="/:paramId/04-merge-intervals"                   element={<MergeIntervals />} />
                  <Route path="/:paramId/05-cycle-sort"                        element={<CycleSort />} />
                  <Route path="/:paramId/06-in-place-reversal-of-linked-lists" element={<InPlaceRevLinkedList />} />
                  <Route path="/:paramId/07-tree-breadth-first-search"         element={<TreeBreadthFirstSearch />} />
                  <Route path="/:paramId/08-tree-depth-first-search"           element={<TreeDepthFirstSearch />} />
                  <Route path="/:paramId/09-two-heaps"                         element={<TwoHeaps />} />
                  <Route path="/:paramId/10-subsets"                           element={<Subsets />} />
                  <Route path="/:paramId/11-modified-binary-search"            element={<ModifiedBinarySearch />} />
                  <Route path="/:paramId/12-top-K-elements"                    element={<TopKElements />} />
                  <Route path="/:paramId/13-k-way-merge"                       element={<KWayMerge />} />
                  <Route path="/:paramId/14-topological-sort"                  element={<TopoSort />} />
              </Routes>
            </>
      </main>
    </>
  )
}

export default App
