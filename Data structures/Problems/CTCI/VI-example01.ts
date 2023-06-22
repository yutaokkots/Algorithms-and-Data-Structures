// const example01: (numArr: number[]) => string = (
//     numArr: number[]
// ) => {
//     // function code    
// }

// const example01:
//      defines a function, 'example01'
// (numArr: number[]) => string = (numArr:number[]) => {}
//      takes 'numArr', which is an array of numbers
//      returns a string
//      // assigns 

let numberList:number[] = [1, 2, 3, 2, 4]

const example01: (numArr: number[]) => string = (
    numArr: number[]
) => {
    let sum:number = 0;
    let product:number = 1
    for (let i:number = 0; i < numArr.length; i++){
        sum += numArr[i]
    }
    for (let i:number = 0; i < numArr.length; i++){
        product *= numArr[i]
    }
    return `${sum}, ${product}`
}

console.log(example01(numberList))