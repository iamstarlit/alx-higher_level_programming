#!/usr/bin/node

// Extract the arguments from index 2
const args = process.argv.slice(2);

// Check if no argument is passed
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
