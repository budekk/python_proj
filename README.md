# Geographic Coordinates and Elevation Visualization

This project visualizes geographic coordinates (X, Y) and elevation (Z) data using Python.

## Overview

The plot below shows the geographic coordinates with the elevation data represented by color.

![Geographic Plot](./geographic_plot.png)

## How to Generate the Plot

To recreate the plot, use the Python script provided below:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Path to the CSV file
file_path = r'C:\Users\Python\projekty\python_proj\data.csv'

# Load the data
df = pd.read_csv(file_path)

# Extract X, Y, Z columns
x = df['X']
y = df['Y']
z = df['Z']

# Create the scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(x, y, c=z, cmap='viridis', s=10)
plt.colorbar(label='Elevation (Z)')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Geographic Coordinates and Elevation')

# Save the plot
plt.savefig('geographic_plot.png')
