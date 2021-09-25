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
### BDD: 先寫規格，再寫測試，最後寫程式
### TDD: 先寫測試再寫程式
