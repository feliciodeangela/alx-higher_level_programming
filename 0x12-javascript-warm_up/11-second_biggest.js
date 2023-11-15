#!/usr/bin/node
if (process.argv.length > 3) {
  const newArr = process.argv.slice(2);
  newArr.sort();
  console.log(Number(newArr[newArr.length - 2]));
} else {
  console.log(process.argv.length);
}
