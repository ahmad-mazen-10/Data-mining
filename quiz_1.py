import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 21, 19, 22, 20],
    "Grade": ["A", "B", "A", "C", "B"],
    "Score": [95, 85, 90, 70, 80]
}

df = pd.DataFrame(data)
df.to_excel('students.xlsx', index=False, sheet_name='Sheet1')

# 1
df = pd.read_excel('students.xlsx', sheet_name='Sheet1')

# 2
print(df.head(3))

# 3
average_score = df['Score'].mean()
print("Average Score:", average_score)

# 4
plt.figure(figsize=(8, 5))
sns.histplot(df['Score'], bins=5, kde=True)
plt.title('Score Distribution')
plt.show()

# 5
plt.figure(figsize=(5, 5))
sns.boxplot(x=df['Age'])
plt.title('Age Boxplot')
plt.show()

# 6
grade_counts = df['Grade'].value_counts()
print(grade_counts)
