-- Count the number of occurrences of each 'score' in 'second_table'
-- Group the results by 'score' and order them by the count in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
