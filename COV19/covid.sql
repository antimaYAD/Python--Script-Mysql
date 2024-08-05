use covid_db;
show tables;
select * from day_wise; 
select * from world_meter_wise;
select * from country_wise; 
SELECT COUNTRY AS HIGHEST_INFECTED_COUNTRY, CONFriM AS INFECTED_PEOPLE
FROM COUNTRY_WISE
ORDER BY confrim DESC
limit 1;

select country , (totalcases/population)*100 as Infected_percentage
from world_meter_wise
order by infected_percentage desc
limit 5;

SELECT country AS country_name,
       ((totaldeaths / population) * 100) AS Total_death_percentage
FROM world_meter_wise 
ORDER BY Total_death_percentage desc
LIMIT 10;



SELECT continent,
       (sum(totaldeaths)/ sum(population)) * 100  AS total_death_percentage
FROM world_meter_wise
GROUP BY continent
ORDER BY total_death_percentage DESC
LIMIT 10;

SELECT continent,
       (sum(totalcases)/ sum(population)) * 100  AS infected_percentage
FROM world_meter_wise
GROUP BY continent
ORDER BY infected_percentage DESC
LIMIT 10;

select (sum(totaldeaths)/ sum(population)) * 100  AS total_death_percentage
FROM world_meter_wise;

select date_day , (deaths/ no_country) as average_death_rate_by_day
from day_wise;
select country , continent 
from  world_meter_wise
order by totaldeaths desc
limit 1;

select country , (population / (select avg(totalcases)from world_meter_wise)) as Cases 
from world_meter_wise
order by cases desc
limit 10;




ALTER TABLE world_meter_wise 
CHANGE COLUMN `country/region` country VARCHAR(255);

use emplyoee;

-- Create Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    DepartmentID INT
);

-- Create Departments table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

-- Create Projects table
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(50),
    DepartmentID INT
);

-- Create EmployeeProjects table
CREATE TABLE EmployeeProjects (
    EmployeeID INT,
    ProjectID INT,
    PRIMARY KEY (EmployeeID, ProjectID)
);
-- Insert values into Employees table
INSERT INTO Employees (EmployeeID, Name, DepartmentID) VALUES
(1, 'Alice Smith', 101),
(2, 'Bob Johnson', 102),
(3, 'Carol White', 101),
(4, 'Dave Brown', 103),
(5, 'Eve Black', 102);

-- Insert values into Departments table
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(101, 'HR'),
(102, 'IT'),
(103, 'Finance');

-- Insert values into Projects table
INSERT INTO Projects (ProjectID, ProjectName, DepartmentID) VALUES
(201, 'Project Alpha', 101),
(202, 'Project Beta', 102),
(203, 'Project Gamma', 103);

-- Insert values into EmployeeProjects table
INSERT INTO EmployeeProjects (EmployeeID, ProjectID) VALUES
(1, 201),
(2, 202),
(3, 201),
(4, 203),
(5, 202);



