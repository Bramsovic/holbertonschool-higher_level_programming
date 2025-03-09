-- Create a table named 'id_not_null' with columns 'id' (INT) and 'name' (VARCHAR)
-- The 'id' column is required (NOT NULL) and has a default value of 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
