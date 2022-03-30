-- Scripts that lists the number of records with the same scores
SELECT score, COUNT(*) AS number FROM SECOND_TABLE GROUP BY score ORDER BY number DESC;
