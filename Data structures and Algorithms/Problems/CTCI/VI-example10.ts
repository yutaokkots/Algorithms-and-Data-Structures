// isPrime
// The for loop starts at 2 and runs until 
// (x * x) <= num
// or
// x = sqrt(num)

// so BigO is O(sqrt(N))

const isPrime: (num:number) => boolean = (
    num:number
) => {
    for (let x:number = 2; x * x <= num; x++){
        if (num % x == 0){
            return false
        }
    }
    return true
}

console.log(isPrime(5))
console.log(isPrime(7))
console.log(isPrime(8))
console.log(isPrime(379))