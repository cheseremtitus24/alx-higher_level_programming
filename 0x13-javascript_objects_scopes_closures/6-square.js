#!/usr/bin/node
const Square = require('./5-square.js');

module.exports = class PSquare extends Square {
  charPrint (symbol = 'X') {
    for (let i = 0; i < this.height; i++) {
      let out = '';
      for (let j = 0; j < this.width; j++) {
        out += symbol;
      }
      console.log(out);
    }
  }
};
