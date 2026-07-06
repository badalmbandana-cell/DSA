
select(select distinct salary from employee
where salary =
(select max(salary) from employee where salary <
(select max(salary) from employee))) as secondhighestsalary;
