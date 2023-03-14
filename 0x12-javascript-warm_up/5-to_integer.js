#!/usr/bin/node
const valToInt = parseInt(process.argv[2]);
(valToInt)
  ? console.log('My number : ' + valToInt)
  : console.log('Not a number');
