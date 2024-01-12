// const example01:
//      defines a function, 'example01'
// (numArr: number[]) => string = (numArr:number[]) => {}
//      takes 'numArr', which is an array of numbers
//      returns a string
//      // assigns 
var numberList = [1, 2, 3, 2, 4];
var example01 = function (numArr) {
    var sum = 0;
    var product = 1;
    for (var i = 0; i < numArr.length; i++) {
        sum += numArr[i];
    }
    for (var i = 0; i < numArr.length; i++) {
        product *= numArr[i];
    }
    return "".concat(sum, ", ").concat(product);
};
console.log(example01(numberList));
