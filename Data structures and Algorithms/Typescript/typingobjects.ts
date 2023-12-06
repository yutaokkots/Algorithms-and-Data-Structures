function isArray(value: unknown): boolean {
    return Array.isArray(value);
    //return value instanceof Array;
  }
function isFunction(value: unknown): boolean {
    return typeof value == 'function';
  }
function isObject(value: unknown): boolean {
    if (value == null) return false;
    const type = typeof value;
    return type === 'object' || type == 'function';
    //return typeof value == 'object';
  }
function isPlainObject(value: unknown): boolean {
    if (value == null) return false;
    const prototype = Object.getPrototypeOf(value);
    return prototype == null || prototype === Object.prototype;
  }

const testNull = null;
const testUndef = undefined;
const testObject = {"hello": 4, "goodnight": 3};        
const testFuncArr = () => "hello";
function testFunc(){
    return "hello"}
const testArray = [1, 2];

console.log(typeof testNull);       // object
console.log(testNull);              // null
console.log(typeof testUndef);      // undefined
console.log(testUndef);             // undefined
console.log(typeof testObject);     // object
console.log(testObject);            // {"hello": 4, "goodnight": 3}

console.log(typeof testFuncArr())   // string
console.log(typeof testFuncArr)     // function
console.log(typeof testFunc)        // function
console.log(testFuncArr())          // hello
console.log(testFuncArr)            // [Function: testFuncArr]
console.log(testFunc)               // [Function: testFunc]

console.log("\n")
//////////////////////////////////
// Testing Object.getPrototypeOf()
//////////////////////////////////

const nullObj = null;
// console.log(Object.getPrototypeOf(nullObj));     // TypeError

const undefObj = undefined;
// console.log(Object.getPrototypeOf(undefObj));    // TypeError

const testObj = {"hello": 4, "goodnight": 3}
console.log(Object.getPrototypeOf(testObj));        // [Object: null prototype] {}
//          const testObj = {"hello": 4, "goodnight": 3};  
//                  ├── created using object literal ('{}') syntax.
//                  └── [Object: null prototype] indicates that it has no
//                          prototype chain beyond 'Object.prototype'
//                          i.e. Plain Old Javascript Object (POJO)

const testArrFunc = () => "hello";
console.log(Object.getPrototypeOf(testFuncArr));    // {}
//          const testArrFunc = () => "hello";
//                  ├── Arrow functions, by default, have 
//                  │     an empty prototype (Object.prototype).
//                  └── Lightweight and lacks additional properties/methods.
function testFunction(){
    return "hello"}
console.log(Object.getPrototypeOf(testFunction));   // {}

console.log(Object.getPrototypeOf([]));             // Object(0) []
console.log(Object.getPrototypeOf(testArray));      // Object(0) []



