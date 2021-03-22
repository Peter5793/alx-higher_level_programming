#!/usr/bin/node
let i = 0;
const argv = process.argv;
const intNum = parseInt(argv[2]);

if (isNaN(intNum)) {
  console.log('Missing number of occurrences');
} else {
  for (; i < intNum; i++) {
    console.log('C is fun');
  }
}
