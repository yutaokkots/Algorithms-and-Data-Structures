// reverse a string
var str_1:string = "Hello";
var str_2:string = "";
var str_3:string = "k";
var str_4:string = "hi there";

const reverseString: (s: string) => string = function(
    s: string
): string {
    let left:number = 0
    let right:number = s.length - 1
    let sArray:Array<string> = s.split("")
    while (right > left){
        let letter:string = sArray[right]
        sArray[right] = sArray[left]
        sArray[left] = letter
        left += 1
        right -= 1
    }
    let newS:string = sArray.join("")
    return newS;
}

console.log(reverseString(str_1));
console.log(reverseString(str_2));
console.log(reverseString(str_3));
console.log(reverseString(str_4));