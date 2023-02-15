-- Creates a table and inserts dummy data
-- Creates the table named second_table
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
-- Inserts values into the table as consecutive tuples
INSERT INTO second_table(id,name,score) VALUES (1,"John",10),(2,"Alex",3),(3,"Bob",14),(4,"George",8);
