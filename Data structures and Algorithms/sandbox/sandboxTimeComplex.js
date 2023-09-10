// let arr = [2, 3, 4, 5, 6]

// // O(N^2)
// for (let i = 0; i < arr.length; i++) {
//     console.log(`i is equal to ${i}`)
//     for (let j = 0; j < arr.length; j++){
//         console.log(`>>> j is ${arr[j]}`)
//     }
// }


const arr = [1, 3, 4, 2, 2]
const arr2 = [4,3,1,2,8,9,6,5,7,5]

const findDuplicate = (arr) => {
    arr.sort()
    let count = 0;
    for (let num of arr){
        if (count == num){
            return num
        }
        count = num 
    }
  
}

console.log(findDuplicate(arr2))