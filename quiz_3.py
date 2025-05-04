import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    Name TEXT,
    Age INTEGER,
    Grade TEXT,
    Score INTEGER
)
''')

students_data = [
    ("Alice", 20, "A", 95),
    ("Bob", 21, "B", 85),
    ("Charlie", 19, "A", 90),
    ("Daid", 22, "C", 70),
    ("Eva", 20, "B", 80)
]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students_data)
conn.commit()

# 1
cursor.execute("SELECT * FROM students WHERE Name LIKE 'B%'")
print(cursor.fetchall())

# 2
cursor.execute("SELECT * FROM students ORDER BY Score DESC")
print(cursor.fetchall())

# 3
cursor.execute("SELECT Grade, COUNT(*) FROM students GROUP BY Grade")
print(cursor.fetchall())

# 4
df = pd.read_sql_query("SELECT * FROM students", conn)
df['Score'].plot(title='Score Distribution')

# 5
plt.figure(figsize=(5, 5))
sns.boxplot(x=df['Age'])
plt.title('Age Boxplot')
plt.show()

# 6
cursor.execute("SELECT * FROM students WHERE Score = (SELECT MIN(Score) FROM students)")
print(cursor.fetchall())

