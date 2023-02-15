-- Uses Group By to group based on scores
SELECT score,COUNT(*) AS number  FROM second_table GROUP BY score ORDER BY number DESC;
