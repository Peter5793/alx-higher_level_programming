-- a script that lists all shows, and all genres linked to that show

SELECT a.title, c.name FROM tv_shows AS a 
LEFT JOIN tv_show_genres AS b  
ON a.id = b.show_id 
LEFT JOIN tv_genres AS c 
ON c.id = b.genre_id 
ORDER BY a.title, c.name ASC;
