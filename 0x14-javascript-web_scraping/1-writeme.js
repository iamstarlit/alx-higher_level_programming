#!/usr/bin/node
// Writes content to a file.
'use strict';

const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filepath, content, (err) => {
  if (err) {
    console.error(err);
  }
});
