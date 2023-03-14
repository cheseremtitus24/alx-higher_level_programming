#!/usr/bin/node
/*
 * This script sums commandline
 * arguments 1 and 2 and prints out the results
 * Make use of an anonymous function
 * that makes use of an arrow function
 */
const valToInt = parseInt(process.argv[2]);
const val2ToInt = parseInt(process.argv[3]);
(valToInt && val2ToInt)
  ? (() => {
      console.log(valToInt + val2ToInt);
    })()
  : console.log(NaN);
