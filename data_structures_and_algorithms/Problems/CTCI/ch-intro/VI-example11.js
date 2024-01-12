// factorial
// 
var factorial = function (n) {
    if (n < 0) {
        return -1;
    }
    else if (n == 0) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
};
console.log(factorial(-1));
console.log(factorial(0));
console.log(factorial(1));
console.log(factorial(5));
console.log(factorial(20));
console.log(factorial(50));
