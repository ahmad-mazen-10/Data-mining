from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd



# Stock market data
data = {
    'Day': [1, 2, 3, 4, 5],
    'Opening_Price': [100, 102, 105, 108, 106],
    'Trading_Volume': [10000, 12000, 15000, 9000, 11000],
    'Closing_Price': [102, 105, 108, 106, 109]
}

df = pd.DataFrame(data)

# Prepare features (X) and target (y)
X = df[['Opening_Price', 'Trading_Volume']]
y = df['Closing_Price']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make prediction for new data
new_input = pd.DataFrame([[107, 13000]], columns=['Opening_Price', 'Trading_Volume'])
predicted = model.predict(new_input)

# Calculate R-squared score
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

print(f"Predicted Closing Price for new day: ${predicted[0]:.2f}")
print(f"Model R-squared score: {r2:.4f}")

# ============================================================
# =============================================================


transactions = [
    ['milk', 'bread'],
    ['bread', 'eggs'],
    ['milk', 'eggs'],
    ['milk', 'bread', 'eggs'],
    ['bread', 'cookies']
]

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
print("===== Frequent Itemsets with support >= 50% ===== :")
print(frequent_itemsets)
