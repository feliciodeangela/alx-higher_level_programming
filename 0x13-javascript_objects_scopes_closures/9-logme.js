#!/usr/bin/node
let it = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(`${it}: ${item}`);
    it++;
  }
};
