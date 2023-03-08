-- shows tv title by their ratings
SELECT a.title, sum(b.rate) AS rating FROM tv_shows AS a 
INNER JOIN tv_show_ratings AS b 
ON a.id = b.show_id 
GROUP BY a.title 
ORDER BY rating DESC;

