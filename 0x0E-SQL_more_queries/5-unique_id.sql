-- script creates a database TABLE
-- unique_id that has 2 fields
-- id and name
-- the id field has a default value of 1
-- id filed is constrained as being UNIQUE
CREATE TABLE IF NOT EXISTS 'unique_id'(id INT DEFAULT=1 UNIQUE, name VARCHAR(256));
