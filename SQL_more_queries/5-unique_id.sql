-- Create a table named 'unique_id' with columns 'id' (INT) and 'name' (VARCHAR)
-- The 'id' column is required (NOT NULL) and has a default value of 1
-- The 'id' column must have unique values (UNIQUE constraint)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);
