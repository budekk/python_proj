import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\Python\projekty\python_proj\data.csv'  
df = pd.read_csv(file_path)

x = df['X']  
y = df['Y'] 
z = df['Z'] 

plt.figure(figsize=(10, 8))
plt.scatter(x, y, c=z, cmap='viridis', s=10)
plt.colorbar(label='Elevation (Z)')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Geographic Coordinates and Elevation')
plt.show()
