#!/usr/bin/node
// hello.js # Exporting anonymous Named function
module.exports.hello = function () {
  console.log('hello world');
}

/*
 * module.exports.hello = function () {
 * is similar to :
 * exports.hello = function () {
 * because
 * exports is an alias for module.exports
 *
 */
