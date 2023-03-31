#!/usr/bin/node
let counter = 0;
module.exports.logMe = function (str) {
  console.log(counter++ + ': ' + str);
};
