#!/usr/bin/node
// Module exports a prototype Qux
var Qux = require('./qux').Qux;
var qux = new Qux();
qux.log();
