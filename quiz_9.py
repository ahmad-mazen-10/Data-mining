import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Given transactions
transactions = [
    ['L', 'M', 'K'],
    ['M', 'K'],
    ['L', 'M', 'H'],
    ['M', 'K', 'H'],
    ['L', 'C'],
    ['L', 'M', 'K', 'C']
]

# Convert to one-hot encoded DataFrame
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Set thresholds
min_support = 0.5
min_confidence = 0.7

# Apriori
frequent_itemsets_apriori = apriori(df, min_support=min_support, use_colnames=True)
rules_apriori = association_rules(frequent_itemsets_apriori, metric="confidence", min_threshold=min_confidence)

# FP-Growth
frequent_itemsets_fp = fpgrowth(df, min_support=min_support, use_colnames=True)
rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=min_confidence)

print("Association Rules from Apriori:")
print(rules_apriori[['antecedents', 'consequents', 'support', 'confidence']])

print("\nAssociation Rules from FP-Growth:")
print(rules_fp[['antecedents', 'consequents', 'support', 'confidence']])