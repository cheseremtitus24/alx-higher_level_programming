#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((parseInt(w) > 0) && (parseInt(h) > 0)) {
      this.width = w;
      this.height = h;
    }
  }
};
