#!/usr/bin/node

function add (a, b) {
  return (Number.parseInt(a) + Number.parseInt(b));
}

const [num1, num2] = process.argv.slice(2);

console.log(add(num1, num2));
