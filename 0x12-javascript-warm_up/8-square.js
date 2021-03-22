#!/usr/bin/node
const argv = process.argv;
const intNum = parseInt(argv[2]);
let i = 0;

if (isNaN(intNum)) {
  console.log('Missing size');
} else {
  for (; i < intNum; i++) {
    console.log('X'.repeat(intNum));
  }
}
