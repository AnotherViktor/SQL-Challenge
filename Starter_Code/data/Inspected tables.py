import pandas as pd
import os

# Path to the folder containing CSV files
folder_path = r'C:\Users\vikto\OneDrive\Рабочий стол\SQLchallenge\Starter_Code\data'

# List all files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Inspect each file
for file in files:
    print(f"Inspecting file: {file}")
    file_path = os.path.join(folder_path, file)
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Show the first few rows and column names
    print(df.head())
    print(df.columns)
    print(df.info())
    print("\n")
