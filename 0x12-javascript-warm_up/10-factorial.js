#!/usr/bin/node
/*
 * This script outputs the factorial of command argument 1
 * description:
 * Make use of an anonymous function
 * that makes use of an arrow function
 */
const valToInt = parseInt(process.argv[2]);
let result = 1;
for (let i = 1; i <= valToInt; i++) {
  result *= i;
}
console.log(result);
