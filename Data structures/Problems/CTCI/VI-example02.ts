let numArr1:number[] = [1, 2, 3, 2, 1, 2, 5] 

const printPairs: (numArr: number[]) => string = (
    numArr: number[]
) => {
    for (let i:number = 0; i < numArr.length; i++){
        for (let j:number = 0; j < numArr.length; j++){
            console.log(`${numArr[i]}, ${numArr[j]}`)
        }
    } 
} 

printPairs(numArr1)

// BigO-> O(N^2)