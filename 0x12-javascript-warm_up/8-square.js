#!/usr/bin/node
/*
 * This script print the string 'C is fun'
 * x times based on the first commandline argument
 * passed in.
 * Make use of an anonymous function
 * that makes use of an arrow function
 */
const valToInt = parseInt(process.argv[2]);
if (valToInt === 0) {
  process.exit(0);
}
(valToInt)
  ? (() => {
      for (let i = 0; i < valToInt; i++) {
        let row = '';
        for (let j = 0; j < valToInt; j++) {
          row += 'X';
        }
        console.log(row);
      }
    })()
  : console.log('Missing size');
