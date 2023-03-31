#!/usr/bin/node
module.exports = class Rectangle {
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
};
