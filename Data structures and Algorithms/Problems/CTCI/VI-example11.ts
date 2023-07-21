// factorial
// 

// time complexity: 
// O(N)
// because this is a recursion where:
//      , n-1, n-2, n-3, ... 1

const factorial: (n:number) => number = (
    n:number
) => {
    if (n < 0){
        return -1
    } else if (n == 0){
        return 1
    } else {
        return n * factorial(n - 1)
    }
}


console.log(factorial(-1))
console.log(factorial(0))
console.log(factorial(1))
console.log(factorial(5))
console.log(factorial(20))
console.log(factorial(50))