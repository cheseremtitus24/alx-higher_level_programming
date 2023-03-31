#!/usr/bin/node
/*
 * This script sums commandline
 * arguments 1 and 2 and prints out the results
 * Make use of an anonymous function
 * that makes use of an arrow function
 */
let secondMax = 0;
if (process.argv.length <= 3) {
  console.log(secondMax);
  process.exit(1);
}
const sortedArray = process.argv.slice(2).sort(function (a, b) {
  return parseInt(b) - parseInt(a); // sorted in descending order for inverse ( a - b)
});
// Convert int integer values to as to sort
secondMax = parseInt(sortedArray[1]);
console.log(secondMax);
