-- Create the database 'hbtn_0d_usa' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select 'hbtn_0d_usa' as the active database
USE hbtn_0d_usa;

-- Create a table named 'states' with columns 'id' (INT) and 'name' (VARCHAR)
-- The 'id' column is required (NOT NULL), auto-incremented, and set as the primary key
-- The 'name' column is required (NOT NULL)
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
