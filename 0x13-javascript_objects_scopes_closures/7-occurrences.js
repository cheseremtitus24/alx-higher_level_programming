#!/usr/bin/node
/**
 * Defines an anonymous function that finds the
 * number of occurrences of a symbol, word or string
 */
module.exports.nbOccurences = function (list, searchElement) {
  let start = 0;
  for (const name of list) {
    if (typeof (name) === 'object') {
      for (const iname of name) {
        if (iname === searchElement) {
          start++;
        }
      }
    } else {
      if (name === searchElement) { start++; }
    }
  }
  return (start);
};
