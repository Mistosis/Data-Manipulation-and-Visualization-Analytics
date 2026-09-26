import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
df = pd.read_csv(os.path.join(base_path, 'winemag_cleaned.csv'))

print("--- Step 7: Regional/Variety Heatmap ---")

top_countries = df['country'].value_counts().head(8).index
top_varieties = df['variety'].value_counts().head(8).index

# Matrix of Country vs Variety (Average Points)
subset = df[df['country'].isin(top_countries) & df['variety'].isin(top_varieties)]
pivot = subset.pivot_table(index='country', columns='variety', values='points', aggfunc='mean')

plt.figure(figsize=(12, 8))
sns.heatmap(pivot, annot=True, cmap='YlGnBu', fmt=".1f")
plt.title('Average Quality Heatmap: Top 8 Countries vs Varieties')
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'heatmap_geo_variety.png'))

print(f"\nHeatmap saved to heatmap_geo_variety.png")
