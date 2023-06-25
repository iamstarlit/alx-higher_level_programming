#!/usr/bin/node

const arg = process.argv[2];
const num = Number.parseInt(arg);

console.log(factorial(num));

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
