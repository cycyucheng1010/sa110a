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