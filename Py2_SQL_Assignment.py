import sqlite3
import csv
import os

DATABASE_NAME = 'retirement_data.db'
EMPLOYEE_FILE = 'Employee.txt'
PAY_FILE = 'Pay.txt'
SOCIAL_SECURITY_MIN_FILE = 'SocialSecurityMinimum.txt'

#Checks if database already exists.
if os.path.exists(DATABASE_NAME):
    os.remove(DATABASE_NAME)
    print(f"Existing database '{DATABASE_NAME}' removed.")

conn = None
try:
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    print(f"Database '{DATABASE_NAME}' created successfully.")

    cursor.execute('''
        CREATE TABLE Employee (
            EmployeeID INTEGER PRIMARY KEY,
            Name TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE Pay (
            EmployeeID INTEGER,
            Year INTEGER,
            Earnings REAL
        );
    ''')

    cursor.execute('''
        CREATE TABLE SocialSecurityMin (
            Year INTEGER PRIMARY KEY,
            Minimum REAL
        );
    ''')
    conn.commit()
    print("Tables created successfully.")

    #Imports all employee data.
    with open(EMPLOYEE_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader) #Skips header.
        employee_data = [tuple(row) for row in reader]

    cursor.executemany('INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?)', employee_data)
    print(f"Data imported from {EMPLOYEE_FILE} into Employee table.")

    with open(SOCIAL_SECURITY_MIN_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        ssm_data = [tuple(row) for row in reader]

    cursor.executemany('INSERT INTO SocialSecurityMin (Year, Minimum) VALUES (?, ?)', ssm_data)
    print(f"Data imported from {SOCIAL_SECURITY_MIN_FILE} into SocialSecurityMin table.")

    #Imports al pay data.
    with open(PAY_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        pay_data = [tuple(row) for row in reader]

    cursor.executemany('INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?)', pay_data)
    print(f"Data imported from {PAY_FILE} into Pay table.")

    conn.commit()
    print("All data committed successfully.")

except sqlite3.Error as e:
    print(f"Database error: {e}")
    if conn:
        conn.rollback()
except FileNotFoundError as e:
    print(f"Error: Input file not found - {e}")

finally:
    if conn:
        conn.close()
        print("Database connection closed for Part 1.")

#Below covers data reporting segment.

conn = None
try:
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    print(f"\nConnecting to database '{DATABASE_NAME}' for Part 2 reporting.")

    sql_query = """
    SELECT
        e.Name,
        p.Year,
        p.Earnings,
        s.Minimum
    FROM
        Employee AS e
    JOIN
        Pay AS p ON e.EmployeeID = p.EmployeeID
    JOIN
        SocialSecurityMin AS s ON p.Year = s.Year;
    """

    cursor.execute(sql_query)
    result_set = cursor.fetchall()
    print("Data fetched successfully.")

    print(f"{'Employee Name':<18} {'Year':<6} {'Earnings':<12} {'Minimum':<10} {'Include':<8}")
    print("-" * 60)

    for row in result_set:
        employee_name, year, earnings, minimum = row

        include_status = "Yes" if earnings >= minimum else "No"

        print(f"{employee_name:<18} {year:<6} {earnings:<12.2f} {minimum:<10.2f} {include_status:<8}")

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    if conn:
        conn.close()
        print("Database connection closed for Part 2.")