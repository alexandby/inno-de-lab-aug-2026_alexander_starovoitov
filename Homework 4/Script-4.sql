--1
/*UPDATE employees
SET salary = salary * 1.1
WHERE department = 'HR'*/

--2
/*update employees
set department = 'Senior IT'
where salary > 70000.00*/

--3
/*delete
from employees e
where not exists (
	select 1
	from employeeprojects ep
	where ep.employeeid = e.employeeid 
)*/

--4
/*begin transaction;

insert into projects (projectname, budget, startdate, enddate)
values ('Gothica Remake', 111000, '2023-05-12', '2024-12-05')
returning projectid;

insert into employeeprojects (employeeid, projectid, hoursworked)
values (2, 4, 346), (3, 4, 581);

commit;*/