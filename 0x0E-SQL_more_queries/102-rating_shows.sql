-- shows tv title by their ratings
SELECT a.title, sum(c.rate) AS rating FROM tv_shows AS a 
  INNER JOIN tv_show_genres AS b
    ON a.id = b.show_id 
  INNER JOIN tv_show_ratings AS c
    ON b.show_id = c.show_id 
  GROUP BY a.title 
  ORDER BY rating DESC;
