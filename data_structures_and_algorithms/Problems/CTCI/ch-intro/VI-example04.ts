//Two different inputs

const printUnorderedPairs: (arrayA:number[], arrayB:number[]) => string = (
    arrayA: number[],
    arrayB: number[]
) => {
    for (let i:number = 0; i < arrayA.length; i++){
        for (let j:number = 0; j < arrayB.length; j++){
            if (arrayA[i] < arrayB[j]){
                let s:string = `${arrayA[i]},  ${arrayB[j]}`
                console.log(s)
                
            }
        }
    }
    return "ok"
}

let arrayA:number[] = [2, 4, 5, 7, 3]
let arrayB:number[] = [4, 5, 7, 3, 2]

printUnorderedPairs(arrayA, arrayB);