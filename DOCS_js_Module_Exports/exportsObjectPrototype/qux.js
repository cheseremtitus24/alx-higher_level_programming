#!/usr/bin/node
// qux.js
var Qux = function() {};
Qux.prototype.log = function () {
  console.log("qux!");
};
exports.Qux = Qux;
