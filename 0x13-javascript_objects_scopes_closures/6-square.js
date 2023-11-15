#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    let chr;
    c ? chr = c : chr = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }
};
