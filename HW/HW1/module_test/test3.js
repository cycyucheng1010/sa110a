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

