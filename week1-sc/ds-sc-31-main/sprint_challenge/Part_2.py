"""
Part 2.1

데이터베이스를 스키마대로 생성해야 합니다.
init_db 함수를 실행하면 3개의 테이블이 생성되어야 합니다.
"""


CREATE_USER_TABLE = """CREATE TABLE "User" (
    "id"    INTEGER,
    "username"  VARCHAR(32),
    "password"  VARCHAR(32),
    PRIMARY KEY("id" AUTOINCREMENT)
);
"""

CREATE_PRODUCT_TABLE = """CREATE TABLE "Product" (
    "id"    INTEGER,
    "product_name"  VARCHAR(32),
    "product_price"  INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);
"""

CREATE_USER_PRODUCT_TABLE = """CREATE TABLE "User_Product" (
    "id"    INTEGER, 
    "user_id"  INTEGER,
    "product_id"  INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (product_id) REFERENCES Product(id)
);"""

"""
Part 2.2

각 질문에 해당하는 결과를 조회할 수 있는 SQL 쿼리문을 작성합니다.
"""

# 1. 데이터베이스에서 가장 비싼 제품 (개별 가격당) 10개를 구해보세요.
# - 제품 이름만 쿼리 결과에 포함합니다.
SQL_QUERY_1 = """SELECT ProductName 
FROM Product AS p
ORDER BY UnitPrice DESC 
LIMIT 10;"""

# 2. 고용 당시 직원의 평균 연령을 구해보세요.
SQL_QUERY_2 = """SELECT AVG(HireDate - BirthDate) AS "Avg Age"
FROM Employee AS e"""

# 3. 1번 문제에 제품을 만든 회사들도 같이 구해보세요.
# - 제품 id, 제품 이름, 유닛 가격, 회사 이름만 쿼리 결과에 포함합니다.
SQL_QUERY_3 = """SELECT p.Id, p.ProductName, p.UnitPrice, s.CompanyName 
FROM Product AS p
INNER JOIN Supplier AS s
ON p.SupplierId = s.Id
ORDER BY UnitPrice DESC
LIMIT 10;"""

# 4. 가장 많은 제품이 있는 카테고리를 구해보세요.
SQL_QUERY_4 = """SELECT c.CategoryName
FROM Product AS p 
INNER JOIN Category AS c 
ON p.CategoryId = c.Id 
GROUP BY CategoryId
ORDER BY COUNT(CategoryId) DESC
LIMIT 1;"""

# 5. 각 도시별로 직원의 고용 당시 평균 연령을 구해보세요.
# - 도시 이름과 도시별 평균 연령을 쿼리 결과에 포함합니다.
SQL_QUERY_5 = """SELECT City , AVG(HireDate - BirthDate) AS "Avg Age"
FROM Employee AS e
GROUP BY City"""

# 6. 어느 직원이 가장 많은 영역(Territory)을 차지하고 있나요?
# - 직원 id, 직원 Lastname, 총 영역 수를 쿼리 결과에 포함합니다.
SQL_QUERY_6 = """SELECT e.Id AS "직원 id", e.LastName AS '직원 Lastname', COUNT(et.EmployeeId) as '총 영역 수'
FROM EmployeeTerritory AS et 
INNER JOIN Employee AS e
ON et.EmployeeId =e.Id
GROUP BY et.EmployeeId
ORDER BY COUNT(et.EmployeeId) DESC
LIMIT 1;"""
