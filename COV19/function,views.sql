use employee;


-- SORTED PROCEDUER-- 
DELIMITER //
CREATE procedure GET_EMPLOYEE_BY_ID(IN EMP_ID INT)
   begin
       SELECT * FROM employees WHERE EmployeeID = EMP_ID;
   END //
   
DELIMITER ;

CALL GET_EMPLOYEE_BY_ID(4)


-- TRIGGER--

DELIMITER //

CREATE TRIGGER AfterEmployeeInsert
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO AuditLog (EmployeeID, Action, ActionDate)
    VALUES (NEW.EmployeeID, 'INSERT', NOW());
END //

DELIMITER ;


-- UDF (User Define Function)-- 

DELIMITER //

CREATE FUNCTION CalculateEmployeeAge(birthDate DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(YEAR, birthDate, CURDATE()) - 1; -- Example modification
END //

DELIMITER ;

-- Views simple-- 
create view emp as select name,employeeid from employees;

select * from emp;

insert into emp(name,employeeid) value('komal',456);

  