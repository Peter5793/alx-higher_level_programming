#!/usr/bin/node

const argv = proces.argv;
const request = require('request');
const url = `http://swapi.co/api/films/${argv[2]}`;

request(url, function(err, response body) {
	if (err) throw err;

	console.log(`${JSON.parse(body).title}`);
});
