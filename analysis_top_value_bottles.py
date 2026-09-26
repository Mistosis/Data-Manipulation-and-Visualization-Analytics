import pandas as pd
import os

base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
df = pd.read_csv(os.path.join(base_path, 'winemag_cleaned.csv'))

print("--- Step 10: Value for Money Deep Dive ---")

# Calculate Points per Dollar
df['value_score'] = df['points'] / df['price']

# Top 20 Value Wines
top_value = df.sort_values(by='value_score', ascending=False).head(20)

print("\nTop 20 Best Value Wines (Highest Points per Dollar):")
print(top_value[['title', 'points', 'price', 'value_score', 'country']].to_string(index=False))

top_value.to_csv(os.path.join(base_path, 'top_value_wines.csv'), index=False)
print(f"\nValue report saved to top_value_wines.csv")
