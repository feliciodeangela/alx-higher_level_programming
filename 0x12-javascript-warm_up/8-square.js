#!/usr/bin/node
let i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  while (i < Number(process.argv[2])) {
    console.log('X'.repeat(Number(process.argv[2])));
    i++;
  }
}
