-- script for all genres of the tv show dexter
SELECT a.name FROM tv_genres AS a
LEFT JOIN tv_show_genres AS b
ON a.id = b.genre_id
LEFT JOIN tv_shows AS c
ON b.show_id = c.id
WHERE c.title = 'Dexter'
GROUP BY a.name
ORDER BY name ASC
