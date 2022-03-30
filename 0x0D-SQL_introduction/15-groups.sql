-- Scripts that lists the number of records with the same scores
SELECT `score`, count(*) as number FROM SECOND_TABLE GROUP BY score ORDER BY score DESC;
