import pandas as pd
import numpy as np
import os

# Load datasets
base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
file1 = os.path.join(base_path, 'winemag-data_first150k.csv')
file2 = os.path.join(base_path, 'winemag-data-130k-v2.csv')

print("--- Step 1: Loading Datasets ---")
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

print(f"Dataset 1 (150k) shape: {df1.shape}")
print(f"Dataset 2 (130k) shape: {df2.shape}")

# Merge datasets
# Note: First 150k has fewer columns. We'll keep what we can.
cols1 = df1.columns.tolist()
cols2 = df2.columns.tolist()
common_cols = list(set(cols1) & set(cols2))
print(f"Common columns found: {common_cols}")

# Columns only in v2 like 'taster_name' are valuable. 
# We'll use a outer join approach or just append and fill NAs.
df_combined = pd.concat([df1, df2], ignore_index=True, sort=False)
print(f"Combined dataset shape: {df_combined.shape}")

# Removing duplicates
print("--- Step 2: Removing Duplicates ---")
initial_len = len(df_combined)
# Use description and title for unique identification where title is available
df_combined = df_combined.drop_duplicates(subset=['description'])
final_len = len(df_combined)
print(f"Removed {initial_len - final_len} duplicate reviews.")

# Handling missing values
print("--- Step 3: Handling Missing Values ---")
print("Missing before:")
print(df_combined.isnull().sum())

# Drop rows where essential info is missing
df_combined = df_combined.dropna(subset=['price', 'points', 'country', 'variety'])
print(f"Final cleaned dataset shape: {df_combined.shape}")

# Save temp cleaned data
cleaned_file = os.path.join(base_path, 'winemag_cleaned.csv')
df_combined.to_csv(cleaned_file, index=False)
print(f"Cleaned data saved to {cleaned_file}")
