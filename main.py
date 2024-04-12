# Pandas: Find the percentage of Missing values in each Column

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', None, None],
    'experience': [None, 5, None, None],
    'salary': [None, 180.2, 190.3, 205.4],
})

percent_missing = df.isnull().sum() * 100 / len(df)
print(percent_missing)

print('-' * 50)

df2 = pd.DataFrame({
    'col_name': df.columns,
    'percent_missing': percent_missing
})

print(df2)
