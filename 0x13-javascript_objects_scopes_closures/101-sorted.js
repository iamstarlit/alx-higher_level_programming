#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};

for (const key in dict) {
  const occurrence = dict[key];

  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [];
  }
  sortedDict[occurrence].push(key);
}
console.log(sortedDict);
