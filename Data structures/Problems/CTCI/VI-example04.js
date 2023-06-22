//Two different inputs
var printUnorderedPairs = function (arrayA, arrayB) {
    for (var i = 0; i < arrayA.length; i++) {
        for (var j = 0; j < arrayB.length; j++) {
            if (arrayA[i] < arrayB[j]) {
                var s = "".concat(arrayA[i], ",  ").concat(arrayB[j]);
                console.log(s);
            }
        }
    }
    return "ok";
};
var arrayA = [2, 4, 5, 7, 3];
var arrayB = [4, 5, 7, 3, 2];
printUnorderedPairs(arrayA, arrayB);
