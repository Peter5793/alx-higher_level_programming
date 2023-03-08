-- titles that do not have comedy
SELECT 
  title 
FROM tv_shows 
  WHERE title NOT IN 
  (
      SELECT a.title FROM tv_shows AS a 
      LEFT JOIN tv_show_genres AS b 
      ON a.id = b.show_id 
      LEFT JOIN tv_genres AS c 
      ON b.genre_id = c.id WHERE c.name = 'Comedy' 
    )
      GROUP BY title ORDER BY title ASC;
