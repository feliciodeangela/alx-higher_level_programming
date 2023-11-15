#!/usr/bin/node
if (process.argv.length > 3) {
  const newArr = process.argv.map(Number).slice(2);
  newArr.sort();
  console.log(newArr[newArr.length - 2]);
} else {
  console.log(process.argv.length);
}
