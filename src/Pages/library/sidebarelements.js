import Clock from "../../Components/MiniProjects/clock/Clock";
import MortgageCalculator from "../../Components/MiniProjects/mortgageCalculator/MortgageCalculator";
import FiveLetters from "../../Components/MiniProjects/fiveletters/FiveLetters";
import TrafficLight from "../../Components/MiniProjects/trafficlights/TrafficLight";
import AnalogClock from "../../Components/MiniProjects/analogclock/AnalogClock";

const sidebarelements = {
    "projects" : [
        {
            name: "Clock",
            display: false,
            url: "",
            component: Clock,
        },
        {
            name: "Analog Clock",
            display: false,
            url: "",
            component: AnalogClock,
        },
        {
            name: "Mortgage Calculator",
            display: false,
            url: "",
            component: MortgageCalculator
        },
        {
            name: "Traffic Light",
            display:false,
            url:"",
            component: TrafficLight
        },
        {
            name: "Five Letters",
            display:false,
            url:"",
            component:FiveLetters
        }
    ]
}

export default sidebarelements;