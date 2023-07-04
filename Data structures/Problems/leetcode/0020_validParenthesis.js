var q01 = "()";
var q02 = "()[]{}";
var q03 = "({[]})";
var q04 = "[()]{}";
var q05 = "{[}]";
var q06 = "({[})";
var q07 = "(]";
var q08 = "[";
var q09 = "]";
var q10 = "";
var q11 = "((";
var q12 = "))";
var q13 = "([]))";
var q14 = "{(})";
var q15 = "([)]";
var q16 = "{([])}";
var q17 = "{{{{}}";
var q18 = "(((({{))";
var q19 = "{[()]";
var q20 = "(())[]{}";
var q_list = [q01, q02, q03, q04, q05, q06, q07, q08, q09, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20];
var isValid = function (s) {
    var stack = [];
    var dict = {
        "}": "{",
        ")": "(",
        "]": "["
    };
    for (var _i = 0, s_1 = s; _i < s_1.length; _i++) {
        var letter = s_1[_i];
        if (letter in dict) {
            if (stack.length > 0 && dict[letter] === stack[stack.length - 1]) {
                stack.pop();
            }
            else {
                return false;
            }
        }
        else {
            stack.push(letter);
        }
    }
    return stack.length > 0 ? false : true;
};
for (var _i = 0, q_list_1 = q_list; _i < q_list_1.length; _i++) {
    var question = q_list_1[_i];
    console.log(question);
    console.log(isValid(question));
}
// function isValid(s:string):boolean{
//     return true
// }
