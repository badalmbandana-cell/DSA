select eu.unique_id as unique_id,e.name as name
from Employees e left join EmployeeUNI eu ON e.id=eu.id;
