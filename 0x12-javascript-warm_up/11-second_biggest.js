#!/usr/bin/node
if (process.argv.length > 3) {
  let newArr = process.argv.slice(2);
  newArr.sort();
  console.log(newArr[1]);
} else {
  console.log(0);
}
