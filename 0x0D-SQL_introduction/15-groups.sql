-- Scripts that lists the number of records with the same scores
SELECT
	score,
	COUNT(*) number
FROM 
	second_table
GROUP BY score DESC
HAVING COUNT (score) >= 1;
