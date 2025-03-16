import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Product": ["A", "B", "C", "D", "E", "F", "G"],
    "Region": ["North", "South", "North", "East", "West", "South", "North"],
    "Sales": [200, 150, 300, 250, 400, 350, 100]
}

df = pd.DataFrame(data)
df.to_excel('sales.xlsx', index=False, sheet_name='Sheet1')

# 1
df = pd.read_excel('sales.xlsx', sheet_name='Sheet1')

# 2
print(df.info())

# 3
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# 4
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'],kde=True)
plt.title('Sales Distribution')
plt.show()

# 5
plt.figure(figsize=(5, 5))
sns.boxplot(x=df['Sales'])
plt.title('Sales Boxplot')
plt.show()

# 6
max_sales_product = df.loc[df['Sales'].idxmax()]
print("Product with Highest Sales:\n", max_sales_product)
