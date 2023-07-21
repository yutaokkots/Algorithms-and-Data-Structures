class Fibonacci {
    constructor(){
        this.List = [];
    }

    fibonacci(n, a = 0, b = 1, aList = []){
        if (n == 0){
            //return a
            this.List.push(a)
            return this.List
        }
        if (n == 1){
            //return b 
            this.List.push(b)
            return this.List
        }
        return this.fibonacci(n - 1, b, a + b, this.List)
    }
}

const fib = new Fibonacci()
console.log(fib.fibonacci(1))
console.log(fib.fibonacci(2))
console.log(fib.fibonacci(3))
console.log(fib.fibonacci(4))
console.log(fib.fibonacci(5))
console.log(fib.fibonacci(6))
console.log(fib.fibonacci(7))
let fib7 = fib.fibonacci(7)
console.log(`%c${fib7}`, "background-color:green;")
