-- Create table with default value
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256));
