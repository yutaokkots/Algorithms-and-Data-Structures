/**
 * Implements basic calculator with string input, from LC0224
 * This file cannot be run in this local environment.
 */
import java.util.Stack;

public class _0224_basicCalculator {
    /**
     * Calculates the result of the given arithmetic expression.
     * @param s The arithmetic expression as a string.
     * @return The result of the arithmetic expression as an int.
     */

    public int calculate(String s){
        Stack<Integer> stack = new Stack<Integer>();
        int sign = 1;       // current number's +/- value
        int temp_calc = 0;  // temporary value
        int result = 0;

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(Character.isDigit(c)){
                temp_calc = 10 * temp_calc + (int)(c - '0');
            } else if (c == '+'){
                result += sign * temp_calc;
                temp_calc = 0;
                sign = 1;
            } else if (c == '-'){
                result += sign * temp_calc;
                temp_calc = 0;
                sign = -1;
            } else if (c == '('){
                stack.push(result);
                stack.push(sign);
                sign = 1;
                result = 0;
            } else if (c == ')'){
                result += sign * temp_calc;
                temp_calc = 0;
                result *= stack.pop();
                result += stack.pop();
            }
        }
        if (temp_calc != 0){
            result += sign * temp_calc;
        }
        return result; 
    }
}