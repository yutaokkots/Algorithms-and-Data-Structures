const q01:string = "()"
const q02:string = "()[]{}"
const q03:string = "({[]})"
const q04:string = "[()]{}"
const q05:string = "{[}]"
const q06:string = "({[})"
const q07:string = "(]"
const q08:string = "["
const q09:string = "]"
const q10:string = ""
const q11:string = "(("
const q12:string = "))"
const q13:string = "([]))"
const q14:string = "{(})"
const q15:string = "([)]"
const q16:string = "{([])}"
const q17:string = "{{{{}}"
const q18:string = "(((({{))"
const q19:string = "{[()]"
const q20:string = "(())[]{}"

const q_list:string[]  = [q01,q02,q03,q04,q05,q06,q07,q08,q09,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]

const isValid: (s:string) => boolean = (
    s:string
) => {
    let stack:string[] = []
    let dict:object = {
        "}":"{",
        ")":"(",
        "]":"["
    }
    for (let letter of s){
        if (letter in dict){
            if (stack.length > 0 && dict[letter] === stack[stack.length - 1]){
                stack.pop()
            } else {
                return false
            }
        } else {
            stack.push(letter)
        }
    }
    return stack.length > 0 ? false : true
}


for (let question of q_list){
    console.log(question)
    console.log(isValid(question))
}

// function isValid(s:string):boolean{
//     return true

// }