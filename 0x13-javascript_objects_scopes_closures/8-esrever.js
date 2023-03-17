#!/usr/bin/node
module.exports.esrever = function (str) {
  let i;
  let j;

  for (i = 0, j = str.length - 1; i < j; i++, j--) {
    temp = str[i];
    str[i] = str[j];
    str[j] = temp;
  }
  return (str);
};
