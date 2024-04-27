/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let stack = [];
    let answer = 0;
    let tempCalc = 0;
    let sign = 1;
    let i = 0;
    for (let currVal of s){
        if (!isNaN(currVal) && currVal != " "){
            tempCalc = (tempCalc * 10) + parseInt(currVal);
        } else if (currVal == "+" || currVal == "-"){
            answer += sign * tempCalc;
            tempCalc = 0;
            sign = currVal == "+" ? 1 : -1; 
        } else if (currVal == "("){
            stack.push(answer);
            stack.push(sign);
            sign = 1;
            answer = 0;
        } else if (currVal == ")"){
            answer += sign * tempCalc;
            answer *= stack.pop();
            answer += stack.pop();
            tempCalc = 0;
        }
        console.log(`[${stack}]; temp: ${tempCalc}, answ: ${answer}`);
        console.log(s)
        console.log(`${" ".repeat(i)}^`)
        console.log(" ")
        i++
    }

    return answer + (tempCalc * sign);
};

let s = "(1+(4+5+2)-3)+(6+8)"
console.log(calculate(s))

/* 
[0,1]; temp: 0, answ: 0
(1+(4+5+2)-3)+(6+8)
^
 
[0,1]; temp: 1, answ: 0
(1+(4+5+2)-3)+(6+8)
 ^
 
[0,1]; temp: 0, answ: 1
(1+(4+5+2)-3)+(6+8)
  ^
 
[0,1,1,1]; temp: 0, answ: 0
(1+(4+5+2)-3)+(6+8)
   ^
 
[0,1,1,1]; temp: 4, answ: 0
(1+(4+5+2)-3)+(6+8)
    ^
 
[0,1,1,1]; temp: 0, answ: 4
(1+(4+5+2)-3)+(6+8)
     ^
 
[0,1,1,1]; temp: 5, answ: 4
(1+(4+5+2)-3)+(6+8)
      ^
 
[0,1,1,1]; temp: 0, answ: 9
(1+(4+5+2)-3)+(6+8)
       ^
 
[0,1,1,1]; temp: 2, answ: 9
(1+(4+5+2)-3)+(6+8)
        ^
 
[0,1]; temp: 0, answ: 12
(1+(4+5+2)-3)+(6+8)
         ^
 
[0,1]; temp: 0, answ: 12
(1+(4+5+2)-3)+(6+8)
          ^
 
[0,1]; temp: 3, answ: 12
(1+(4+5+2)-3)+(6+8)
           ^
 
[]; temp: 0, answ: 9
(1+(4+5+2)-3)+(6+8)
            ^
 
[]; temp: 0, answ: 9
(1+(4+5+2)-3)+(6+8)
             ^
 
[9,1]; temp: 0, answ: 0
(1+(4+5+2)-3)+(6+8)
              ^
 
[9,1]; temp: 6, answ: 0
(1+(4+5+2)-3)+(6+8)
               ^
 
[9,1]; temp: 0, answ: 6
(1+(4+5+2)-3)+(6+8)
                ^
 
[9,1]; temp: 8, answ: 6
(1+(4+5+2)-3)+(6+8)
                 ^
 
[]; temp: 0, answ: 23
(1+(4+5+2)-3)+(6+8)
                  ^
*/