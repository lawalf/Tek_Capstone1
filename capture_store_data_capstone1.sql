DROP SCHEMA IF EXISTS da_bootcamp_capstone1_lawal; 
CREATE SCHEMA IF NOT EXISTS da_bootcamp_capstone1_lawal;
USE da_bootcamp_capstone1_lawal;

CREATE TABLE IF NOT EXISTS Animals (
Animal_ID INT,
Animal_Location VARCHAR(255),
Animal_Age INT
);