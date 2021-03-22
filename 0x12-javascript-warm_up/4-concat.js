#!/usr/bin/node
const argv = process.argv;

if (process.argv.length < 3) {
	console.log('No argument');
} else if (process.argv.length > 3) {
	console.log (argv[2] + ' is ' + argv[3]);
}
