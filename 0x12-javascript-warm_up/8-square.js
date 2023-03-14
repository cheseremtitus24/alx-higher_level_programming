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
        for (let j = 0; j < valToInt; j++) {
          process.stdout.write('X');
        }
        console.log('');
      }
    })()
  : console.log('Missing size');
