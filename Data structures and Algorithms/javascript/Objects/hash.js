const str1 = "anagram"
const str2 = "mammalian"

////////////////////////////////
//////// string counter method 1
let countS = new Map()

for (let letter of str1){
    if (letter in countS){
        countS[letter] += 1;
    } else {
        countS[letter] = 1;
    }
}
console.log(countS)


////////////////////////////////
//////// string counter method 2
const counter = (str) => {
    let count = {};
    str.split("").forEach((letter) => count[letter] = (count[letter] || 0) + 1)
    return count
}

const countT = counter(str2);
console.log(countT);

countT.forEach((v,k) => {
    console.log(k);
})

