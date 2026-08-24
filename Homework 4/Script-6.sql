--1
/*SELECT p.projectname
FROM projects p
join employees e on p.projectid = e.employeeid
where exists (
	select 1
	from employeeprojects e2
	where e2.employeeid = e.employeeid and e2.hoursworked > 150
)*/

--2
/*update projects
set budget = budget * 1.1
where exists (
	select 1
	from employees e
	join employeeprojects e2 on e2.employeeid = e.employeeid
	where e.department = 'Senior IT'
)*/

--3
/*update projects
set startdate = startdate + INTERVAL '1 year'
where enddate is NULL*/

--4
begin transaction;

insert into employees (firstname, lastname, department, salary, email)
values ('Alexander', 'Gray', 'IT', 150000, 'gray.6907a@company.com')
returning employeeid;

insert into employeeprojects (employeeid, projectid, hoursworked)
values (7, 1, 80);

commit;