#!/usr/bin/node

function add (a, b) {
  return (Number.parseInt(a) + Number.parseInt(b));
}

// export the add function explicitily
module.exports.add = add;
