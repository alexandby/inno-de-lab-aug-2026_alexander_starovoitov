--1
/*select p.projectname
from projects p
join employeeprojects ep on ep.projectid = p.projectid
where exists (
	select 1
	from employees e
	where ep.employeeid = e.employeeid and e.firstname = 'Bob' and e.lastname = 'Johnson' and ep.hoursworked > 150
)*/

--2
/*update projects p
set budget = budget * 1.1
where exists (
	select 1
	from employeeprojects ep
	join employees e on e.employeeid = ep.employeeid
	where ep.projectid = p.projectid and e.department = 'Senior IT'
)*/

--3
/*update projects
set enddate = startdate + INTERVAL '1 year'
where enddate is NULL*/

--4
/*begin transaction;

with inserted_employee as (
	insert into employees (firstname, lastname, department, salary, email)
	values ('Alexander', 'Gray', 'IT', 150000, 'gray.6907a@company.com')
	returning employeeid
)

insert into employeeprojects (employeeid, projectid, hoursworked)
select employeeid, 1, 80
from inserted_employee;

commit;*/