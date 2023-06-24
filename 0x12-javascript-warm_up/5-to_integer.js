#!/usr/bin/node

const arg = process.argv.slice(2);
const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
