#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const fileContents1 = fs.readFileSync(sourceFile1, 'utf8').trim();
const fileContents2 = fs.readFileSync(sourceFile2, 'utf8').trim();
const concatenatedContents = fileContents1 + '\n' + fileContents2 + '\n';

fs.writeFileSync(destinationFile, concatenatedContents);
