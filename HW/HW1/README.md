# HW1
## 實作loadash內之函數，利用傳統作法、BDD、TDD的方式進行實作
### 傳統做法: clamp
* 先寫程式再寫測試
* 說明: Clamps number within the inclusive lower and upper bounds.
* main code: [cycclamp.js](https://github.com/cycyucheng1010/sa110a/blob/master/HW/HW1/cycclamp.js)
```
//Clamps number within the inclusive lower and upper bounds.
// Arguments: number (number): The number to clamp. [lower] (number): The lower bound. upper (number): The upper bound.
//Returns: (number): Returns the clamped number.
//_.clamp(-10, -5, 5);
// => -5
//_.clamp(10, -5, 5);
// => 5
export function clamp(number,lower,upper){
number =+number
lower =+lower
upper =+upper
lower = lower ===lower?lower:0
upper = upper === upper?upper:0
if(number===number){
    number=number<=upper?number:upper
    number=number>=lower?number:lower
}
return number
}
```
* function code: [test1.js](https://github.com/cycyucheng1010/sa110a/blob/master/HW/HW1/module_test/test1.js)
```
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
```
* result
```
PS C:\Users\rick2\sa110a\HW\HW1\module_test> deno test test1.js
running 1 tests
test clamp ... _.clamp(a,b,c)= -5
_.clamp(a,b,c)= 5
ok (3ms)

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out (3ms)
```
### BDD: inRange
* 先寫規格，再寫測試，最後寫程式
* 說明: Checks if number is between start and up to, but not including, end. 
* 規格: 
```
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
```
* 測試:[test2.js](https://github.com/cycyucheng1010/sa110a/blob/master/HW/HW1/module_test/test2.js)
```
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
```
* 程式:[cycinrange.js](https://github.com/cycyucheng1010/sa110a/blob/master/HW/HW1/cycinrange.js)
```
export function inRange(number, start, end){  
if (end ===undefined){
    end =  start
    start = 0
}
if(start>=end){
    var temp=end
    end=start
    start=temp
}  
if (number<end && number>start){
    return true
} 
else{
    return false
}
}
```
* result:
```
yucheng@ubuntu:~/sa110a/HW/HW1/module_test$ deno test test2.js
running 1 test from file:///home/yucheng/sa110a/HW/HW1/module_test/test2.js
test inRange ..._.inRange(3,2,4) : true
_.inRange(4, 8) : true
_.inRange(4, 2) : false
_.inRange(2, 2) : false
_.inRange(1.2, 2) : true
_.inRange(5.2, 4) : false
_.inRange(-3, -2, -6) : true
 ok (7ms)

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out (35ms)
```
### TDD: 
* 先寫測試再寫程式
* 說明: The opposite of _.before; this method creates a function that invokes func once it's called n or more times.
* 測試: [test3.js](https://github.com/cycyucheng1010/sa110a/blob/master/HW/HW1/module_test/test3.js)
```
import * as _ from "../cycafter.js";
import{assert} from "https://deno.land/std@0.108.0/testing/asserts.ts"

Deno.test("after",()=>{
var saves = ['profile', 'settings'];
 
var done = _.after(saves.length, function() {
  console.log('done saving!');
});
/*
_.forEach(saves, function(type) {
  asyncSave({ 'type': type, 'complete': done });
});
// => Logs 'done saving!' after the two async saves have completed.
*/
})
```
* 程式:[cycafter.js ](https://github.com/cycyucheng1010/sa110a/blob/master/HW/HW1/cycafter.js)
```
export function after(n, func) {
    if (typeof func !== 'function') {
      throw new TypeError('Expected a function')
    }
    n = n || 0
    return function(...args) {
      if (--n < 1) {
        return func.apply(this, args)
      }
    }
  }
```
* result
```
yucheng@ubuntu:~/sa110a/HW/HW1/module_test$ deno test test3.js
running 1 test from file:///home/yucheng/sa110a/HW/HW1/module_test/test3.js
test after ... ok (7ms)

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out (33ms)
```
