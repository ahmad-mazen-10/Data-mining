# Assignment 3:
# • For the following code :
# • Get number of rows
# • Get random 50% rows
# • Sort by 'col1' , DESC
# • Filter data to get obtain result (col2 >=7 )
# • Get the oldest 3 rows

import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'col1': np.random.randint(1, 100, 10),
    'col2': np.random.randint(1, 10, 10),
    'date': pd.date_range(start="2023-01-01", periods=10, freq='D')
}
df = pd.DataFrame(data)

num_rows = df.shape[0]
print(f"Number of rows: {num_rows}")

df_sample = df.sample(frac=0.5, random_state=42)
print("\nRandom 50% rows:")
print(df_sample)

df_sorted = df.sort_values(by='col1', ascending=False)
print("\nSorted by col1 (DESC):")
print(df_sorted)

df_filtered = df[df['col2'] >= 7]
print("\nFiltered (col2 >= 7):")
print(df_filtered)

df_oldest = df.nsmallest(3, 'date')
print("\nOldest 3 rows:")
print(df_oldest)
