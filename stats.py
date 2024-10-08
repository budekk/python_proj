import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the CSV file
file_path = r'C:\Users\Python\projekty\python_proj\data.csv'

# Load the data
df = pd.read_csv(file_path)

# Extract Z column
z = df['Z']

# Statystyki opisowe
mean_z = z.mean()
median_z = z.median()
min_z = z.min()
max_z = z.max()
std_z = z.std()
percentiles = z.quantile([0.25, 0.5, 0.75])

print("Mean:", mean_z)
print("Median:", median_z)
print("Min:", min_z)
print("Max:", max_z)
print("Standard Deviation:", std_z)
print("Percentiles (25%, 50%, 75%):", percentiles.values)

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(z, bins=30, kde=True)
plt.title('Distribution of Elevation (Z)')
plt.xlabel('Elevation (Z)')
plt.ylabel('Frequency')
plt.show()

# Zasięg
range_z = max_z - min_z
print("Range of Elevation (Z):", range_z)

# Korelacja
correlation_xy = df[['X', 'Y', 'Z']].corr()
print("Correlation Matrix:\n", correlation_xy)

# Wykrywanie outlierów (np. z użyciem IQR)
Q1 = z.quantile(0.25)
Q3 = z.quantile(0.75)
IQR = Q3 - Q1
outliers = df[(z < (Q1 - 1.5 * IQR)) | (z > (Q3 + 1.5 * IQR))]
print("Number of outliers detected:", len(outliers))
