#!/usr/bin/node
// baz.js
var Baz = function() {};

Baz.prototype.log = function () {
  console.log("baz!");
};

exports.Baz = new Baz();

