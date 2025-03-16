import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    Name TEXT,
    Department TEXT,
    Salary INTEGER
)
''')

employees_data = [
    ("Alice", "HR", 50000),
    ("Bob", "IT", 60000),
    ("Charlie", "Finance", 70000),
    ("David", "HR", 55000),
    ("Eva", "IT", 65000)
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?)", employees_data)
conn.commit()

# 1
cursor.execute("SELECT * FROM employees WHERE Department = 'HR'")
print(cursor.fetchall())

# 2
cursor.execute("SELECT * FROM employees WHERE Salary BETWEEN 60000 AND 70000")
print(cursor.fetchall())

# 3
cursor.execute("SELECT Department, SUM(Salary) FROM employees GROUP BY Department")
print(cursor.fetchall())

# 4
df = pd.read_sql_query("SELECT * FROM employees", conn)
df['Salary'].plot(title='Salary Distribution')
plt.show()

# 5
df['Salary'].plot(title='Salary Boxplot')
plt.show()

# 6
cursor.execute("""
    SELECT Department, AVG(Salary) as avg_salary
    FROM employees
    GROUP BY Department
    ORDER BY avg_salary DESC
    LIMIT 1
""")
print(cursor.fetchall())

