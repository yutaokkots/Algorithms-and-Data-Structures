// the following function prints out the value at index of a list
// 
var numArr1 = [1, 2, 3, 5];
var numArr2 = [0, 1, 2, 3, 4, 5, 6, 7];
var printUnorderedPairs = function (numArr) {
    for (var i = 0; i < numArr.length; i++) {
        for (var j = i + 1; j < numArr.length; j++) {
            console.log("(".concat(numArr[i], ", ").concat(numArr[j], ")"));
        }
    }
    return true;
};
printUnorderedPairs(numArr1);
printUnorderedPairs(numArr2);
