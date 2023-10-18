-- Display number of records with the same score
SELECT score, COUNT(score) as number FROM second_table ORDER BY number DESC;
