import Clock from "../../Components/MiniProjects/clock/Clock";
import MortgageCalculator from "../../Components/MiniProjects/mortgageCalculator/MortgageCalculator";
import FiveLetters from "../../Components/MiniProjects/fiveletters/FiveLetters";

const sidebarelements = [
    {
        project: "Clock",
        display: false,
        url: "",
        component: Clock,
    },
    {
        project: "Mortgage Calculator",
        display: false,
        url: "",
        component: MortgageCalculator
    },
    {
        project: "Five Letters",
        display:false,
        url:"",
        component:FiveLetters
    }
]

export default sidebarelements;