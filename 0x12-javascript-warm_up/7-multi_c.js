#!/usr/bin/node

const arg = process.argv.slice(2);
let num = parseInt(arg);

if (isNaN(num)) {
  console.log('Missing Missing number of occurrences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num -= 1;
  }
}
