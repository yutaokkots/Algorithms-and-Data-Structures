//////////////////////////
console.log("Q) 1")

let animals = ["koala", "kangaroo", "tasmanian wolf"]
console.log(animals)
animals[2] = "eagle"
console.log(animals)

//////////////////////////
console.log("Q) 2")

const a = { x: 1}
const b = { x: 1}

console.log(a===b)  //returns false
console.log(a==b)   //returns false
console.log(a!=b)

//////////////////////////
console.log("Q) 3")

var thing;
let func = (str = 'no arg') => {
    console.log(str)
}

func(thing)
func(null)

//////////////////////////
console.log("Q) 4")

let animales = [{type:"lion"}, "tiger"]
let clones = animales.slice()

clones[0].type = "bear"
clones[1] = "sheep"

console.log(animales[0].type, clones[0].type);
console.log(animales[1], clones[1])

// bear bear
// tiger sheep

//////////////////////////
console.log("Q) 5")

let obj = {}
console.log(obj.a?.b)
//console.log(obj?.a.b)
//console.log(obj.?a.?b)
//console.log(obj[a][b])

// In JavaScript, the question mark (?) is part of the optional chaining feature 
// introduced in ECMAScript 2020 (ES2020). It is used to simplify accessing properties 
// of an object when the properties might not exist or be nullish (null or undefined).
//
// The optional chaining operator (?.) is used to access the b property of the a property 
// of the obj object. It allows you to avoid a runtime error if the a property doesn't exist 
// or is null or undefined. Instead of throwing an error, the expression obj.a?.b will 
// evaluate to undefined.




//////////////////////////
console.log("Q) 6")
// A generator function is a special type of function in JavaScript that can be paused and resumed during its execution. It allows you to control the flow of execution and generate a sequence of values over time, rather than returning a single value like a regular function.

// Here are some unique characteristics of generator functions:

// Use of the function* syntax: A generator function is defined using the function* syntax. For example:



function* fibonacci_1() {
    let a = 0;
    let b = 1;
  
    while (true) {
      yield a;
      [a, b] = [b, a + b];      // value swapping
    }
  }
  

function* fibonacci_2() {
    let a = 0;
    let b = 1;

    while (true) {
        yield a;
        //[a, b] = [b, a + b];
        a, b = b, a + b;        // This does not work
    }
}

const fibSequence1 = fibonacci_1();
const fibSequence2 = fibonacci_2();

// Generating and printing the first 8 Fibonacci numbers
console.log("Q6 part a")
for (let i = 0; i < 8; i++) {
    console.log(fibSequence1.next().value);
}
console.log("Q6 part b")
for (let i = 0; i < 8; i++) {
    console.log(fibSequence2.next().value);
}

//////////////////////////
console.log("Q) 7")
function* numbers(){
    let n = 0;
    while(true){
        yield n;
        n += 2
    }
}

const genNum = numbers()

for (let i = 0; i < 5; i++){
    console.log(genNum.next().value)

}

//////////////////////////
console.log("Q) 8")

const numeros = [1, 2, 3, 4, 5]

const [one, two, three, four, five] = numeros

console.log(numeros)
console.log(one)
console.log(two)
console.log(three)
console.log(four)
console.log(five)