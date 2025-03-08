-- Create a table named 'force_name' with columns 'id' (INT) and 'name' (VARCHAR)
-- The 'name' column is required (NOT NULL) to ensure that it cannot be empty
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
