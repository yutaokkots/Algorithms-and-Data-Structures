var numArr1 = [1, 2, 3, 2, 1, 2, 5];
var printPairs = function (numArr) {
    for (var i = 0; i < numArr.length; i++) {
        for (var j = 0; j < numArr.length; j++) {
            console.log("".concat(numArr[i], ", ").concat(numArr[j]));
        }
    }
};
printPairs(numArr1);
