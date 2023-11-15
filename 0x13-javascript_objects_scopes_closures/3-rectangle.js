#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }
  print() {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }
};
