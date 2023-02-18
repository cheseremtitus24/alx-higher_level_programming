-- Script lists all the cities of California 
-- script utilizes subqueries
SELECT id,name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name="California");
