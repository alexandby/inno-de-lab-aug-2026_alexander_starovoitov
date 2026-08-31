--1
/*create table departments (
	DepartmentID SERIAL PRIMARY KEY,
	DepartmentName VARCHAR(50) unique NOT NULL,
	Location VARCHAR(50)
);*/

--2
/*alter table employees add column email VARCHAR(100);*/

--3
/*update employees
set email = LOWER(FirstName || '.' || SUBSTRING(gen_random_uuid()::text FROM 1 FOR 5) || '@company.com')*/

--4
/*alter table employees add constraint UQ_Email unique (email)*/

--5
alter table departments rename column location to OfficeLocation