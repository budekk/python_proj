import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Funkcja do wczytywania danych z pliku CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Funkcja do tworzenia wykresu współrzędnych geograficznych i wysokości
def plot_coordinates_and_elevation(df):
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

# Funkcja do obliczania i wyświetlania statystyk dla kolumny Z
def elevation_statistics(df):
    z = df['Z']
    
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
    
    # Wykres histogramu rozkładu Z
    plt.figure(figsize=(10, 6))
    sns.histplot(z, bins=30, kde=True)
    plt.title('Distribution of Elevation (Z)')
    plt.xlabel('Elevation (Z)')
    plt.ylabel('Frequency')
    plt.show()
    
    # Zakres (range) Z
    range_z = max_z - min_z
    print("Range of Elevation (Z):", range_z)
    
    # Macierz korelacji dla X, Y i Z
    correlation_xy = df[['X', 'Y', 'Z']].corr()
    print("Correlation Matrix:\n", correlation_xy)

# Główna funkcja, która łączy obie funkcjonalności
def main(file_path):
    # Wczytanie danych
    df = load_data(file_path)
    
    # Wykres współrzędnych i wysokości
    plot_coordinates_and_elevation(df)
    
    # Statystyki wysokości
    elevation_statistics(df)

# Ścieżka do pliku CSV (zastąp swoją ścieżką)
file_path = r'C:\Users\Python\projekty\python_proj\data.csv'  # Replace with your file path

# Uruchomienie głównej funkcji
main(file_path)
