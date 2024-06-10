# Create a sample database to interact with it

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data/sqlite/salaries.db')
cursor = conn.cursor()

# Create the Salaries table
create_table_query = """
CREATE TABLE SALARIES (
    Id INTEGER PRIMARY KEY,
    EmployeeName TEXT,
    JobTitle TEXT,
    BasePay REAL,
    OvertimePay REAL,
    OtherPay REAL,
    Benefits TEXT,
    TotalPay REAL,
    TotalPayBenefits REAL,
    Year INTEGER,
    Notes TEXT,
    Agency TEXT,
    Status TEXT
);
"""
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()
