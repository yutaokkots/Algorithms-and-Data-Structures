// Review Questions from Chapter VI of the CTCI book


///////////////////////////
// VI.1
console.log("VI.1:")
// The following code computes the product of a and b. What is its runtime?
const product: (a:number, b:number) => number = (
    a:number,
    b:number
) => {
    let sum:number = 0;
    for (let i:number = 0; i < b; i++){
        sum += a;
    }
    return sum;
}

console.log("VI.1 product(2,3)", product(2,3))
console.log("VI.1 product(5,6)", product(5,6))
console.log("VI.1 product(10,11)", product(10,11))
console.log("VI.1 product(2,7)", product(2,7))
console.log("VI.1 product(5,6)", product(5,6))
// The time complexity is O(N) because the algorithm occurs n times, where n is the size of b


///////////////////////////
// VI.2
console.log("VI.2:")
// The following code computes a^b. What is the runtime?
const power: (a:number, b:number) => number = (
    a:number,
    b:number
) => {
    if (b < 0){
        return 0
    } else if (b == 0){
        return 1
    } else {
        return a * power(a, b-1)
    }
}
console.log("VI.2 power(6,5)", power(6,5))
console.log("VI.2 power(2,6)", power(2,6))
console.log("VI.2 power(6,2)", power(6,2))
console.log("VI.2 power(5,5)", power(5,5))
console.log("VI.2 power(1,0)", power(1,0))
console.log("VI.2 power(0,1)", power(0,1))

// the time complexity is O(N), because the algorithm occurs n times for the size of b

///////////////////////////
// VI.3
console.log("VI.3:")
// The following code computes a % b. What is its runtime?
const mod: (a:number, b:number) => number = (
    a:number,
    b:number
) => {
    if (b <= 0){
        return -1;
    } 
    let div:number = Math.floor(a / b);
    return a - div * b
}

console.log("VI.3 mod(12,5)", mod(12,5))
console.log("VI.3 mod(12,2)", mod(12,2))
console.log("VI.3 mod(8, 0)", mod(8, 0))
console.log("VI.3 mod(10,3)", mod(10,3))

// the time complexity is O(1), because the algorithm occurs once, independently of the values for a or b


///////////////////////////
// VI.4
console.log("VI.4:")
// The following code performs integer division. What is its runtime (assume a and b are both positive)?

const div: (a:number, b:number) => number | string = (
    a:number,
    b:number
) => {
    // additional code for edge case where b = 0
    if (b == 0){
        return "undefined"
    }

    let count:number = 0;
    let sum:number = b;
    while (sum <= a){
        sum += b;
        count += 1;
    }
    return count
}

console.log("VI.4 div(12,5)", div(12,5))
console.log("VI.4 div(12,2)", div(12,2))
console.log("VI.4 div(8, 0)", div(8, 0))
console.log("VI.4 div(10,3)", div(10,3))
console.log("VI.4 div(0, 8)", div(0, 8))

// The time complexity is O(N), because the number of times the while loop will run will depend on 
// how many times b will occur inside a. 
