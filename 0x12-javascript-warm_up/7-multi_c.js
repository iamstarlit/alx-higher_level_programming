#!/usr/bin/node

const c = 'C is fun';
const arg = process.argv.slice(2);
let num = parseInt(arg);

while (num) {
  console.log(c);
  num -= 1;
}
