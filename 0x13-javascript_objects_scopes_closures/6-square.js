#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((parseInt(w) > 0) && (parseInt(h) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let out = '';
      for (let j = 0; j < this.width; j++) {
        out += 'X';
      }
      console.log(out);
    }
  }

  rotate () {
    // Swaps width and height
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Doubles the width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
