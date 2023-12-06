/** Count by
 * 
 * Implement a function countBy(array, iteratee) that creates an object 
 * composed of keys generated from the results of running each element of array thru iteratee. 
 * The corresponding value of each key is the number of times the key was returned by iteratee. 
 * 
 * iteratees can either be:
 *      Functions: iteratee functions is invoked with one argument: (value).
 *      Strings: The property of an object. 
 *          E.g. 'length' can be used to return the number of elements of arrays.
 * 
 * @argument array (Array): The array to iterate over.
 * @argument iteratee (Function): The iteratee function to transform elements. 
 *          The function is invoked with one argument: (value).
 * @returns (Object): Returns the composed aggregate object.
 * @example countBy([6.1, 4.2, 6.3], Math.floor);
 *      // => { '4': 1, '6': 2 }
 * @example countBy(['one', 'two', 'three'], 'length');
 *      // => { '3': 2, '5': 1 }
 *      % npx ts-node iteratee.ts  
*/

type IterateeFn<T> = (value: T) => number | string;
        // <T> type variable, 'T'. -> can work with different types without specifying, until used. 
        // 'type IterateeFn<T>' defines a type alias named 'IterateeFn'
        // '(value: T) => number | string' is a function type. Takes a value (type T) and returns num/str.

function countBy<T>(
    array: Array<T>,
    iteratee: IterateeFn<T> | string
): {[key:string]: number} {
    const aggregate:Record<string, number> = {};
    const iterateFunction: IterateeFn<T> = 
        typeof iteratee === 'function' ? iteratee : (value:any) => value[iteratee];
    
    for (const item of array){
        const value = iterateFunction(item);
        aggregate[value] = (aggregate[value] || 0) + 1;
    }
    return aggregate;
}

const result1 = countBy([6.1, 4.2, 6.3], Math.floor)
const result2 = countBy(['one', 'two', 'three'], 'length')

console.log(result1)
console.log(result2)