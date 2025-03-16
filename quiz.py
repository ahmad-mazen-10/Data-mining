import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# create emploees table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS employees(
                   Name TEXT,
                   Department TEXT,
                   Salary Integer
               )
               """)

# insert sample data into the table
employees_data=[
    ('alice', 'IQ', 5000),
    ('bod', 'finance', 6000),
    ('Charlie', 'HR', 5500),
    ('nour', 'IT', 7000),
    ('eva', 'IQ', 65000),
]

# 1
df = pd.read_sql_query("SELECT* FROM employees_data", conn)

# 2
print('first 3 ')
print(df.head(3))

total_salary= df.groupby('department')['salary'].sum()
print(total_salary)

# 4
plt.figure(figsize=(8,5))
plt.hist(df['salary'])
plt.xlabel('salary')
plt.title('salary dis')
plt.show()

# 5
plt.figure(figsize=(6,4))
plt.boxplot(df["salary"])
plt.xlabel('salary')
plt.title('salary boxplot')
plt.show()
