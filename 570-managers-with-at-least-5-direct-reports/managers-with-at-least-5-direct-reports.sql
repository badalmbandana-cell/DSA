select name from employee where id IN (select managerId from employee group by managerId having count(id)>=5);
