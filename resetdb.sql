-- Drop the existing database
DROP DATABASE IF EXISTS awsdb;

-- Create a new database
CREATE DATABASE awsdb;

-- Create a new user
CREATE USER awsuser WITH PASSWORD 'zAdRUnapr8*';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON DATABASE awsdb TO awsuser;