"""
Part 3

각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = """SELECT CustomerId, upper(city ||" "|| Country) as city_country
from customers;"""

QUERY_2 = """SELECT lower(SUBSTRING(FirstName,1,4)||SUBSTRING(LastName,1,2)) as new_name
from customers;"""

QUERY_3 = """SELECT EmployeeId 
from employees
where HireDate < "2013-01-01"
order by LastName;"""

QUERY_4 = """SELECT (c.FirstName||c.LastName||i.InvoiceId) as new_name
from customers as c
inner join invoices as i
on i.CustomerId = c.CustomerId
ORDER BY c.FirstName,c.LastName,i.InvoiceId;"""

QUERY_5 = """SELECT Name
FROM tracks
WHERE AlbumId IN (SELECT AlbumId 
    FROM albums
    WHERE Title = "Unplugged" OR Title = "Outbreak");"""
