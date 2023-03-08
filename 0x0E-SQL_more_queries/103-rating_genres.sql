-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT a.name, sum(b.rate) AS rating FROM tv_genres AS a 
  INNER JOIN tv_show_genres AS c
      ON a.id = c.genre_id 
  INNER JOIN tv_show_ratings AS b 
      ON c.show_id = b.show_id 
GROUP BY a.name
ORDER BY rating DESC;
