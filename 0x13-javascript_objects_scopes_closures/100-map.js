#!/usr/bin/node

const originalList = require('./100-data').list;
console.log(originalList);

const mappedList = originalList.map((e, index) => e * index);
console.log(mappedList);
