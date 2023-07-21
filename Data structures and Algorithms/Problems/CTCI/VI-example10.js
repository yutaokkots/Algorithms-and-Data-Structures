// isPrime
var isPrime = function (num) {
    for (var x = 2; x * x <= num; x++) {
        if (num % x == 0) {
            return false;
        }
    }
    return true;
};
console.log(isPrime(5));
console.log(isPrime(7));
console.log(isPrime(8));
console.log(isPrime(379));
