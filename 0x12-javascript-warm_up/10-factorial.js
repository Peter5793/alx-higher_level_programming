#!/usr/bin/node
const argv = process.argv;
const num1 = parseInt(argv[2]);

function factorize (num1) {
  if (num1 === 0) {
    return 1;
  } else {
    return num1 * factorize(num1 - 1);
  }
}
if (isNaN(num1)) {
  console.log(1);
} else {
  console.log(factorize(num1));
}
