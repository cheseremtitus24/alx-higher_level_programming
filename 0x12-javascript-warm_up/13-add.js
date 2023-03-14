#!/usr/bin/node
/*
 * This script sums commandline
 * parameter values 1 and 2 and returns the results
 */
const add = function (valToInt, val2ToInt) {
  if (valToInt && val2ToInt) {
    return (valToInt + val2ToInt);
  }
};

// Export as a Named Module-Function
module.exports.add = add;
