import pandas as pd
import os

def load_data(filename='rbi_data.csv'):
    """
    Load RBI data from CSV file.
    """
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        return df
    else:
        print(f"File {filepath} not found")
        return None

def calculate_statistics(data):
    """
    Calculate basic statistics from the data.
    """
    if data is None:
        print("No data to analyze")
        return
    
    print("Data Summary:")
    print(data.describe())
    print("\nData Info:")
    print(data.info())

def analyze_trends(data, column):
    """
    Analyze trends in a specific column.
    """
    if data is None:
        print("No data to analyze")
        return
    
    if column in data.columns:
        print(f"\nTrend Analysis for {column}:")
        print(f"Mean: {data[column].mean()}")
        print(f"Min: {data[column].min()}")
        print(f"Max: {data[column].max()}")
        print(f"Std Dev: {data[column].std()}")
    else:
        print(f"Column '{column}' not found in data")

if __name__ == "__main__":
    print("RBI Economic Indicators Analyzer")
    print("="*40)
    
    # Load and analyze data
    data = load_data()
    if data is not None:
        calculate_statistics(data)
    else:
        print("Please run scraper.py first to collect data")
