--1
/*create user hr_user with password 'secure_pass123'*/

--2
/*grant select on employees to hr_user*/

--3
--Test #1 - PASSED!
/*select *
from employees e */

--Test #2 - DENIED!
/*INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Abaduba', 'Baobab', 'HR', 60000.00)*/

--4
/*grant insert, update on employees to hr_user*/
--Test #3 - PASSED!
/*INSERT INTO Employees (employeeid, FirstName, LastName, Department, Salary, email) VALUES
(5,'Abaduba', 'Baobab', 'HR', 60000.00, 'abaduba.b0512@company.com')*/
/*update employees e
set lastname = 'Abudaba'
where e.employeeid = 5*/