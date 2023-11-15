#!/usr/bin/node
if (process.argv.length > 3) {
  const newArr = process.argv.map(Number).slice(2);
  newArr.sort();
  console.log(Number(newArr[1]));
} else {
  console.log(0);
}
