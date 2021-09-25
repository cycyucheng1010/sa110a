/*
Checks if number is between start and up to, but not including, end. 
If end is not specified, it's set to start with start then set to 0.
If start is greater than end the params are swapped to support negative ranges.
_.inRange(3, 2, 4);
// => true
 
_.inRange(4, 8);
// => true
 
_.inRange(4, 2);
// => false
 
_.inRange(2, 2);
// => false
 
_.inRange(1.2, 2);
// => true
 
_.inRange(5.2, 4);
// => false
 
_.inRange(-3, -2, -6);
// => true
*/
import * as _ from "../cycinrange.js"
import{assert} from "https://deno.land/std@0.108.0/testing/asserts.ts"

Deno.test("inRange",()=>{
console.log("_.inRange(3,2,4) :",_.inRange(3,2,4))
console.log("_.inRange(4, 8) :",_.inRange(4, 8))
console.log("_.inRange(4, 2) :",_.inRange(4, 2))
console.log("_.inRange(2, 2) :",_.inRange(2, 2))
console.log("_.inRange(1.2, 2) :",_.inRange(1.2, 2))
console.log("_.inRange(5.2, 4) :",_.inRange(5.2, 4))
console.log("_.inRange(-3, -2, -6) :",_.inRange(-3, -2, -6))
})