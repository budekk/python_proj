---
title: "Geographic Coordinates and Elevation Visualization"
author: "Your Name"
date: "`r Sys.Date()`"
output: html_document
---

## Description

This script reads a CSV file containing geographic coordinates (X and Y) and elevation data (Z). It visualizes the data using a scatter plot, with the color of the points representing the elevation values. The plot also includes a color bar to indicate the elevation levels.

### Python Code

```python
import pandas as pd
import matplotlib.pyplot as plt

# Define the file path to the data
file_path = r'C:\Users\Python\projekty\python_proj\data.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Extract X, Y, and Z columns from the DataFrame
x = df['X']
y = df['Y']
z = df['Z']

# Create a scatter plot of X and Y, with Z values represented by color
plt.figure(figsize=(10, 8))
plt.scatter(x, y, c=z, cmap='viridis', s=10)
plt.colorbar(label='Elevation (Z)')  # Add a color bar for Z (elevation)
plt.xlabel('X Coordinate')           # Label for the X-axis
plt.ylabel('Y Coordinate')           # Label for the Y-axis
plt.title('Geographic Coordinates and Elevation')  # Title of the plot
plt.show()  # Display the plot
