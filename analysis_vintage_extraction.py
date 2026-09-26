import pandas as pd
import re
import os

base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
df = pd.read_csv(os.path.join(base_path, 'winemag_cleaned.csv'))

print("--- Step 6: Vintage Year Extraction ---")

def extract_year(title):
    if pd.isna(title): return None
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', title)
    if years:
        year = int(years[0])
        if 1900 < year < 2025: return year
    return None

df['year'] = df['title'].apply(extract_year)

print(f"\nExtracted years for {df['year'].notna().sum()} out of {len(df)} records.")

vintage_quality = df.groupby('year')['points'].mean().tail(20) # Last 20 vintage years
print("\nAverage Quality by Vintage (Recent 20 Years):")
print(vintage_quality)

# Saving updated data with years
df.to_csv(os.path.join(base_path, 'winemag_with_years.csv'), index=False)
print("\nUpdated dataset saved as winemag_with_years.csv")
