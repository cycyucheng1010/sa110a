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
