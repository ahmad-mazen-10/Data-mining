import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder

# -------------- Given transactions  ----------------
transactions = [
    ['Milk', 'Bread', 'Eggs'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Eggs'],
    ['Bread', 'Butter', 'Eggs']
]

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Set thresholds
min_support = 0.5  # 50%
min_confidence = 0.7  # 70%

# Apriori Algorithm
print("=== Apriori Algorithm ===")
frequent_itemsets_apriori = apriori(df, min_support=min_support, use_colnames=True)
rules_apriori = association_rules(frequent_itemsets_apriori, metric="confidence", min_threshold=min_confidence)

print("\nFrequent Itemsets:")
print(frequent_itemsets_apriori)
print("\nAssociation Rules:")
print(rules_apriori[['antecedents', 'consequents', 'support', 'confidence']])

# FP-Growth Algorithm
print("\n=== FP-Growth Algorithm ===")
frequent_itemsets_fp = fpgrowth(df, min_support=min_support, use_colnames=True)
rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=min_confidence)

print("\nFrequent Itemsets:")
print(frequent_itemsets_fp)
print("\nAssociation Rules:")
print(rules_fp[['antecedents', 'consequents', 'support', 'confidence']])



# Calculate item frequencies
item_counts = df.sum().sort_values(ascending=False)
