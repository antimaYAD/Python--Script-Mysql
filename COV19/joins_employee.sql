use employee;
select * from employees;
-- Find the names of employees, their department names, and the projects they are working on.-- 
SELECT e.Name AS EmployeeName,
       d.DepartmentName,
       p.ProjectName
FROM Employees e
INNER JOIN Departments d
    ON e.DepartmentID = d.DepartmentID
INNER JOIN EmployeeProjects ep
    ON e.EmployeeID = ep.EmployeeID
INNER JOIN Projects p
    ON ep.ProjectID = p.ProjectID;
    
-- Retrieve all employees along with their department names and the names of the projects they are working on. Include employees who are not assigned to any projects.
SELECT e.Name AS EmployeeName,
       d.DepartmentName,
       p.ProjectName
FROM Employees e
LEFT JOIN Departments d
    ON e.DepartmentID = d.DepartmentID
LEFT JOIN EmployeeProjects ep
    ON e.EmployeeID = ep.EmployeeID
LEFT JOIN Projects p
    ON ep.ProjectID = p.ProjectID;

-- List all projects along with the names of employees working on them and their department names. Include projects that have no employees assigned.--
 select p.projectname as ProjectName , e.name as EmployeeName, d.departmentname as DepartmentName
 from projects as p
 right join employeeprojects as ep on ep.projectid = p.ProjectID
 right join employees as e on e.employeeid = ep.employeeid
 right join departments as d on d.departmentid = e.departmentid;
 
 -- Retrieve a list of all employees and all projects, showing which employees are working on which projects, and include employees or projects with no assignments-- 
 select e.name as employeename , p.projectname as Projectname
 FROM Employees e
LEFT JOIN Departments d
    ON e.DepartmentID = d.DepartmentID
LEFT JOIN EmployeeProjects ep
    ON e.EmployeeID = ep.EmployeeID
LEFT JOIN Projects p
    ON ep.ProjectID = p.ProjectID
union
 select e.name as employeename , p.projectname as Projectname
 FROM Employees e
LEFT JOIN Departments d
    ON e.DepartmentID = d.DepartmentID
LEFT JOIN EmployeeProjects ep
    ON e.EmployeeID = ep.EmployeeID
LEFT JOIN Projects p
    ON ep.ProjectID = p.ProjectID;

 
 
 