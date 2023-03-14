#!/usr/bin/node
const valToInt = parseInt(process.argv[2]);

(valToInt || valToInt === 0)
  ? console.log('My number : ' + valToInt)
  : console.log('Not a number');
