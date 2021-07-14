"""
Part 1

아래에 코드에 요구사항에 알맞은 SQL 쿼리문을 작성합니다.
"""

CUSTOMER_TABLE = """CREATE TABLE "Customer" (
    "customer_id"    INTEGER NOT NULL,
    "customer_name"  VARCHAR(32) NOT NULL,
    "customer_age"  INTEGER,
    PRIMARY KEY("customer_id" AUTOINCREMENT)
);
"""

PACKAGE_TABLE = """CREATE TABLE "Package" (
    "package_id"    INTEGER NOT NULL,
    "package_name"  VARCHAR(32) NOT NULL,
    "package_date"  DATE,
    PRIMARY KEY("package_id" AUTOINCREMENT)
);"""

CUSTOMER_PACKAGE_TABLE = """CREATE TABLE "Customer_Package" (
    "cp_id"    INTEGER NOT NULL,
    "customer_id"  INTEGER,
    "package_id"  INTEGER,
    PRIMARY KEY("cp_id" AUTOINCREMENT)
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
	FOREIGN KEY (package_id) REFERENCES Package(package_id)
);"""
