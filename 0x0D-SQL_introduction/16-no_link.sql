-- Skips rows with the column name being null
SELECT  score,name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
