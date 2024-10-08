---
title: "Geographic Coordinates and Elevation Visualization"
date: "08.10.2024"
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

## Analysis of the Scatterplot

# General Distribution of Data:

The scatterplot illustrates the distribution of points in the geographical space. The X and Y axes represent geographical coordinates, while the colors indicate elevation values.
The area covered by colors from light blue to green suggests variations in elevation, indicating diverse terrain.
Height (Z):

The color gradient (from darker blue to bright green) indicates changes in elevation.
On the color scale (right side of the plot), Z values range from about 225 to 255. Observations include:
Light green areas indicate higher values (above 250).
Darker areas represent lower values (below 230).
High and Low Areas:

High Areas: The upper section of the plot shows a clear cluster of light colors, suggesting the presence of higher terrain.
Low Areas: The lower section of the plot displays darker shades, indicating regions of lower elevation.
Terrain Structure:

The clarity and variability of colors may suggest the presence of various terrain formations, such as hills, valleys, or plateaus.
There may also be small water bodies or other geographical features affecting local conditions.
Potential Anomalies:

Attention should be given to any outlier points that may indicate unusual geographical conditions. Investigating points with disproportionately high or low values can provide insights into underlying factors.
Clustering:

Noticeable clusters of points may suggest data groupings with similar characteristics, which could be of interest for urban or ecological analysis.
Conclusions
Elevation Variability: The area presents elevation variability, which may be significant for spatial planning, environmental protection, or geological studies.
Understanding Terrain: This analysis could be useful for further research, particularly in applications involving ecology, agriculture, or urbanization.
Z Values as Indicators: Z values may highlight areas requiring further analysis, such as water resource management or flood protection.
