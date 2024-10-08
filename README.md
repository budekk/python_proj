---
title: "Geographic Coordinates and Elevation Visualization"
author: "Your Name"
date: "`r Sys.Date()`"
output: html_document
---

## Description

This script reads a CSV file containing geographic coordinates (X and Y) and elevation data (Z). It visualizes the data using a scatter plot, with the color of the points representing the elevation values. The plot also includes a color bar to indicate the elevation levels.


# Geographic Coordinates and Elevation Visualization

This project visualizes geographic coordinates (X, Y) and elevation (Z) data using Python.

## Overview

The plot below shows the geographic coordinates with the elevation data represented by color.

![Geographic Plot](./fig1.png)

## How to Generate the Plot

To recreate the plot, use the Python script provided below:

```python
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

plt.savefig('geographic_plot.png')
