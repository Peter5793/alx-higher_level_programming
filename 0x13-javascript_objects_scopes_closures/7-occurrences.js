#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i = 0;
  for (; i < list.length; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
};
