import * as _ from '../cycclamp.js'
import{assert} from "https://deno.land/std@0.108.0/testing/asserts.ts";
Deno.test("clamp",()=>{
var number1 = -10
var lower1 = -5 
var upper1 = 5
var number2 = 10
var lower2 = -5 
var upper2 = 5
console.log("_.clamp(a,b,c)=", _.clamp(number1,lower1,upper1)) 
console.log("_.clamp(a,b,c)=", _.clamp(number2,lower2,upper2))
})