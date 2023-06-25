#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);

// Check if size is not a number
if (isNaN(size)) {
  console.log('Missing size');
  return;
}

for (let i = 0; i < size; i += 1) {
  // Define square inside the loop to reset.
  let square = '';
  for (let j = 0; j < size; j += 1) {
    // Check if size if positive Int
    if (size > 0) square += 'X';
  }
  console.log(square);
}
