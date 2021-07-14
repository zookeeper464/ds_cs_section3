"""
Part 2

각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = """SELECT Title
From albums
where AlbumId = 31;"""

QUERY_2 = """SELECT  AlbumId
FROM albums AS al
INNER JOIN artists AS a
ON al.ArtistId = a.ArtistId
WHERE a.Name LIKE "%the%";"""

QUERY_3 = """SELECT InvoiceId
FROM invoices
WHERE BillingCity in ('Stuttgart','Oslo','Redmond')
ORDER BY InvoiceId;"""

QUERY_4 = """SELECT trackid
FROM tracks
WHERE Name LIKE 'The%';"""

QUERY_5 = """SELECT CustomerId
FROM customers
WHERE Email LIKE '%gmail.com';"""

QUERY_6 = """SELECT InvoiceId
FROM invoices
WHERE CustomerId in (29,30,63) and Total >= 1.00 and Total <=3.00;"""

QUERY_7 = """SELECT TrackId FROM tracks as t
left outer join genres as g
on t.GenreId = g.GenreId
where t.Milliseconds <= 400000 and t.Milliseconds >= 300000 and g.Name = "Soundtrack";"""

QUERY_8 = """SELECT COUNT(CustomerId) AS The_Num_of_customers_X_Country
FROM customers
group by Country;"""

QUERY_9 = """SELECT c.CustomerId
FROM customers as c
left outer join invoices as i
on c.CustomerId = i.CustomerId 
group by c.CustomerId
Order by SUM(i.Total) DESC 
limit 5;"""

QUERY_10 = """SELECT a.Name,COUNT(a.CustomerId) 
FROM (SELECT g.Name, i.CustomerId--DISTINCT i.CustomerId --DISTINCT g.name AS genre_name, COUNT(CustomerId) AS The_Number_of_customer_ID
FROM invoices AS i
INNER JOIN invoice_items AS ii 
ON i.InvoiceId = ii.InvoiceId
INNER JOIN tracks AS t
ON ii.TrackId = t.TrackId 
INNER JOIN genres AS g
ON t.GenreId = g.GenreId
GROUP BY g.Name, i.CustomerId) AS a
GROUP BY a.Name;"""
