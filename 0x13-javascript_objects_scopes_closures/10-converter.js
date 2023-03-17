#!/usr/bin/node
/* Function Ulizes a Closure that is derived from the example below
function makeAdder(x) {
  return function (y) {
    return x + y;
  };
}

const add5 = makeAdder(5);
const add10 = makeAdder(10);

console.log(add5(2)); // 7
console.log(add10(2)); // 12
*/

/* Conversion Example
function dec2bin(dec){
    return (dec >>> 0).toString(2);
}

dec2bin(1);    // 1
dec2bin(-1);   // 11111111111111111111111111111111
dec2bin(256);  // 100000000
dec2bin(-256); // 11111111111111111111111100000000
*/
module.exports.converter = function (base) {
  return function (y) {
    return (y >>> 0).toString(base);
  };
};
