import pandas as pd
from scipy import stats
df = pd.read_csv('data.csv')
column = 'Age'
data = df[column].dropna()
mean = data.mean()
median = data.median()
mode = data.mode().iloc[0]
std_dev = data.std()
print(f"Summary statistics for {column}:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")