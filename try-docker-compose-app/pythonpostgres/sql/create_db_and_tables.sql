-- create user with base role 
CREATE USER genhub WITH ROLE postgres;

-- Create database with owner
CREATE DATABASE genhub OWNER genhub;

-- Create analysis table
CREATE TABLE IF NOT EXISTS genhubrequest (
  userId text NOT NULL,
  request_time timestamp NOT NULL,
  requestid text NOT NULL,
  requested_samples int NOT NULL,
  available_samples int NOT NULL ,
  payable boolean,
  status text NOT NULL,
  PRIMARY KEY (requestid)
);