const nums = [1, 1, 1, 2, 2, 3]
const numsObj = new Map()

// numsObj = {1:2}

for (let n of nums){
    // n = 1
    console.log(n, ":", numsObj.get(n))
    numsObj.set(n, (numsObj.get(n) || 0) + 1)
}

console.log(numsObj)

// undefined
// 1
// 2
// undefined
// 1
// undefined
// Map(3) { 1 => 3, 2 => 2, 3 => 1 }