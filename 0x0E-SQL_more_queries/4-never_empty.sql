-- script creates a database TABLE
-- id_not_null that has 2 fields
-- id and name
-- the id field has a default value of 1
CREATE TABLE IF NOT EXISTS 'id_not_null'(id INT DEFAULT=1, name VARCHAR(256));
