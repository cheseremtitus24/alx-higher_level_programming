#!/usr/bin/node
const valToInt = parseInt(process.argv[2]);

if (valToInt || valToInt === 0) {
  console.log('My number: ' + typeof valToInt)
} else {
  console.log('Not a number');
}
