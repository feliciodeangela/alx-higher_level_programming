#!/usr/bin/node
function fact(a) {
  if (a < 2) {
    return (1);
  } else {
    const ag = a * fact(a - 1);
    return (ag);
  }
}
console.log(fact(Number(process.argv[2])));
