#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (let i = 0; i < list.length; i++) {
    list[i] === searchElement ? occ = occ + 1 : occ = occ + 0;
  }
  return (occ);
};
