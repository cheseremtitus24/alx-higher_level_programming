#!/usr/bin/node
/*
 * This script sums commandline
 * arguments 1 and 2 and prints out the results
 */
const valToInt = parseInt(process.argv[2]);
const val2ToInt = parseInt(process.argv[3]);

if (!isNaN(valToInt) && !isNaN(val2ToInt)) {
  console.log(valToInt + val2ToInt);
} else {
  console.log(NaN);
}
