import React, {useState} from 'react'

interface CodeDisplayProps {
    codeSnippet: string[];
}

interface CodeSnippetDisplayProps {
    codeSnippet: string;
    selected: number;
    displayedVal: number;
}

const CodeSnippetDisplay:React.FC<CodeSnippetDisplayProps>  = ({ codeSnippet, selected, displayedVal }) => {
    return (
        <>
            <CodeSnippetSingle selected={ selected } displayedVal={ displayedVal } codeSnippet={ codeSnippet }/>
        </>
    )
}

interface CodeSnippetSelectionProps {
    setDisplay: (number) => void;
    selectionNo: number
}
const CodeSnippetSelection:React.FC<CodeSnippetSelectionProps> = ({ setDisplay, selectionNo }) => {
    
    const selectionArr = [...Array(selectionNo).keys()]

    return (
        <>
            {selectionArr.map((val, idx) => 
                <CodeSnippetbutton key={idx} val={val} setDisplay= {setDisplay}/>
            )}
        </>
    )
};

interface CodeSnippetButtonProps {
    setDisplay: (number) => void;
    val: number
}
const CodeSnippetbutton:React.FC<CodeSnippetButtonProps> = ({setDisplay, val}) => {
    const handleClick = () => {
        setDisplay(val)
    };
    return (
        <>
            <input 
                className="set-state-button" 
                type="button" 
                onClick={handleClick}
                value="See code"></input>
        </>
    )
}


interface CodeSnippetSingleProps {
    codeSnippet: string;
    selected: number;
    displayedVal: number;
}

const CodeSnippetSingle:React.FC<CodeSnippetSingleProps> = ({codeSnippet, selected, displayedVal}) => {

    if (selected != displayedVal) return null
    return (
        <>
            <div className="code-snippet-sm">
                <pre>{ codeSnippet }</pre>
            </div>
        </>
    )
}


const CodeDisplay:React.FC<CodeDisplayProps> = ({ codeSnippet }) => {
    const [displayedVal, setIsDisplayed] = useState<number>(0)

    const handleDisplay = (val) => {
        setIsDisplayed(val)
    };

    return (
        <>
            <div>
                <div>
                    <CodeSnippetSelection setDisplay={handleDisplay} selectionNo={codeSnippet.length}/>
                </div>
                <div>
                    {codeSnippet.map((code, idx) => 
                        <CodeSnippetDisplay key={ idx } selected={idx} displayedVal={displayedVal} codeSnippet={ code }/>)}
                </div>
            </div>
        </>
    )
}

export default CodeDisplay