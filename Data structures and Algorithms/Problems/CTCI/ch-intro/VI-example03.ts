// the following function prints out the value at index of a list
// 

// Big(O) number -> deceptive. 
// O(N^2)

let numArr1:number[] = [1, 2, 3, 5] 
let numArr2:number[] = [0, 1, 2, 3, 4, 5, 6, 7] 

const printUnorderedPairs: (numArr:number[]) => boolean = (
    numArr:number[]
) => {
    for (let i:number = 0; i < numArr.length; i++){
        for (let j:number = i + 1; j < numArr.length; j++){
            console.log(`(${numArr[i]}, ${numArr[j]})`)
        }
    }
    return true
}

printUnorderedPairs(numArr2)        // where N=8
// (0, 1)
// (0, 2)
// (0, 3)
// (0, 4)
// (0, 5)
// (0, 6)
// (0, 7)
// (1, 2)
// (1, 3)
// (1, 4)
// (1, 5)
// (1, 6)
// (1, 7)
// (2, 3)
// (2, 4)
// (2, 5)
// (2, 6)
// (2, 7)
// (3, 4)
// (3, 5)
// (3, 6)
// (3, 7)
// (4, 5)
// (4, 6)
// (4, 7)
// (5, 6)
// (5, 7)
// (6, 7)

// (0, 1) (0, 2) (0, 3) (0, 4) (0, 5) (0, 6) (0, 7)
//        (1, 2) (1, 3) (1, 4) (1, 5) (1, 6) (1, 7)
//               (2, 3) (2, 4) (2, 5) (2, 6) (2, 7)
//                      (3, 4) (3, 5) (3, 6) (3, 7)  
//                             (4, 5) (4, 6) (4, 7)
//                                    (5, 6) (5, 7)
//                                           (6, 7)