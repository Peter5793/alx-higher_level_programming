#!/usr/bin/node
$(function () {
	$.ajax({
		type:'GET',
		URL: 'https://swapi.co/api/films/?format=json'
	}).done((data) => {
		const results = data.results;
		console.log(results);
		results.forEach(element => {
			$('#list_movies').append(`<li>${element.title}</li>`);
		});
	});
});
