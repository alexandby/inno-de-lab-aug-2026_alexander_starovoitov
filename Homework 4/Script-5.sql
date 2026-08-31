--1
/*create function CalculateAnnualBonus(employee_id INT, salary NUMERIC)
returns numeric as $$
begin
	return salary * 0.1;
end;
$$LANGUAGE plpgsql*/

--2
/*select *, CalculateAnnualBonus(employeeid, salary) as bonus
from employees*/

--3
/*create view IT_Department_View as
select employeeid, firstname, lastname, salary
from employees
where department = 'IT'*/

--4
select * from it_department_view


