use sales;
show tables;

CREATE TABLE STORE(
PERSON VARCHAR(20),
PRODUCTS VARCHAR(20),
QUATITY INT,
REVENU DOUBLE,
REGION VARCHAR(20)
);


SELECT @@secure_file_priv;

LOAD DATA  infile
"C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/store.csv"
INTO TABLE STORE
FIELDS TERMINATED BY ","
LINES TERMINATED BY "\n"
IGNORE 1 LINES;

-- SET GLOBAL local_infile = 1;

select * from store;


use world;
show tables;

SELECT * 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/NewData.csv'
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
FROM city;
