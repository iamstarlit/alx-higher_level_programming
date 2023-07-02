#!/usr/bin/node

const originalDict = require('./101-data').dict;
console.log(originalDict);

const mappedList = Object.keys(originalDict).map(function (key) {
  return originalDict[key] * parseInt(key, 10);
});
console.log(mappedList);
