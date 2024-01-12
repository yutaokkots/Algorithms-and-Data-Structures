// reverse a string
var str_1 = "Hello";
var str_2 = "";
var str_3 = "k";
var str_4 = "hi there";
var reverseString = function (s) {
    var left = 0;
    var right = s.length - 1;
    var sArray = s.split("");
    while (right > left) {
        var letter = sArray[right];
        sArray[right] = sArray[left];
        sArray[left] = letter;
        left += 1;
        right -= 1;
    }
    var newS = sArray.join("");
    return newS;
};
console.log(reverseString(str_1));
console.log(reverseString(str_2));
console.log(reverseString(str_3));
console.log(reverseString(str_4));
