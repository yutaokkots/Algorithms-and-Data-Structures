import React, {useState} from 'react'
import "./mortgageCalculator.css"


const MortgageOutput = ({output}) => {
    return (
        <>
            <div className="mortgage-app">
                <h2>Expected Payment</h2>
                <div className="form-row output-row">
                    <div>
                        Monthly payment:
                    </div>
                    <div className="output-box">
                        <h1><span>${output.monthlymortgage != "NaN" ? output.monthlymortgage: 0}</span></h1>
                    </div>
                </div>
                <div className="form-row output-row">
                    <div>
                        Total Payment:
                    </div>
                    <div className="output-box">
                        <h3><span>${output.totalpayment != "NaN" ? output.totalpayment  : 0}</span></h3>
                    </div>
                </div>
                <div className="form-row output-row">
                    <div>
                        Total interest paid:
                    </div>
                    <div className="output-box">   
                        <h3><span>${output.totalinterest != "NaN" ? output.totalinterest : 0}</span></h3>
                    </div>
                </div>
            </div>
        </>
    )
}

const MortgageCalculator = () => {
    const [values, setValues] = useState({
        "loan": 0,
        "interest": 0,
        "term": 10,
    })
    const [output, setOutput] = useState({
        "monthlymortgage": 0,
        "totalpayment": 0,
        "totalinterest": 0
    })

    const calculator = () => {
        // M = P (i (1+i)**n) / ( (1+i)**n - 1)
        // P(iX)/(X- 1)

        const interestMonth = (values.interest / 12) / 100
        const totalTerm = (values.term * 12) 
        const interestTerm = Math.pow((1 + interestMonth), totalTerm)
        const monthly = values.loan * ( interestMonth * interestTerm) / ( interestTerm - 1 )
        const totalPayment = monthly *  totalTerm
        const interest = totalPayment - values.loan
        setOutput({
            "monthlymortgage": (monthly).toFixed(2),
            "totalpayment": (totalPayment).toFixed(2),
            "totalinterest": (interest).toFixed(2)
            })
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        calculator()
        // setValues({...values, [e.target.name]:e.target.value})
        console.log(values)
    }

    const handleChange = (e) => {
        e.preventDefault()
        setValues({...values, [e.target.name]:e.target.value})
    }

  return (
    <>
        <div className="mortgage-calculator">
            <div className="">
                <h2>Mortgage Calculator</h2>
                <form onSubmit={handleSubmit}>
                    <div className="form-row">
                        <label htmlFor="loan-amount">Loan Amount</label>
                        <input 
                            onChange={handleChange}
                            placeholder="e.g. 300000"
                            name="loan"
                            type="text" 
                            id="loan-amount"></input>
                    </div>
                    <div className="form-row">
                        <label htmlFor="interest-rate">Annual Interest Rate (%)</label>
                        <input 
                            onChange={handleChange}
                            placeholder="e.g. 6.5"
                            name="interest"
                            type="text"
                            pattern='^\d*\.?\d+$'
                            id="interest-rate"></input>
                    </div>
                    <div className="form-row">
                        <label htmlFor="loan-term">Loan Term (in years)</label>
                        <input 
                            onChange={handleChange}
                            placeholder="e.g.  30"
                            name="term"
                            type="number" 
                            id="loan-term"></input>
                    </div>
                    <div className="form-row-button">
                        <input type="submit" value="Submit"></input>
                    </div>
                </form>
            </div>
            
            <MortgageOutput output={output}/>
      
        </div>
    </>
  )
}

export default MortgageCalculator