import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
column = 'Age'
data = df[column].dropna()
mean = data.mean()
median = data.median()
mode = data.mode().iloc[0]
std_dev = data.std()

stats = [mean, median, mode, std_dev]
labels = ['Mean', 'Median', 'Mode', 'Standard Deviation']

plt.bar(labels, stats, color=['skyblue', 'orange', 'green', 'red'])
plt.title('Summary statistics for Age column in Titanic dataset')
plt.ylabel('Value')
plt.show()
