#!/usr/bin/node
/*
 * This script print the string 'C is fun'
 * x times based on the first commandline argument
 * passed in.
 * Make use of an anonymous function
 * that makes use of an arrow function
 */
const valToInt = parseInt(process.argv[2]);
(valToInt)
  ? (() => {
      for (let i = 0; i < valToInt; i++) {
        console.log('C is fun');
      }
    })()
  : console.log('Missing number of occurrences');
