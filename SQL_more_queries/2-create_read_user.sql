-- Create the database 'hbtn_0d_2' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user 'user_0d_2' on localhost with the specified password if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges on all tables in 'hbtn_0d_2' to 'user_0d_2' on localhost
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
