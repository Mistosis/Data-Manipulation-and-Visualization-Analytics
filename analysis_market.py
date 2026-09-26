import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
cleaned_file = os.path.join(base_path, 'winemag_cleaned.csv')
df = pd.read_csv(cleaned_file)

print("--- Market Analysis: Top Varieties ---")
top_varieties = df['variety'].value_counts().head(10)
print("Top 10 Varieties by Review Count:")
print(top_varieties)

# Visualization: Top Varieties
plt.figure(figsize=(12, 6))
sns.barplot(x=top_varieties.values, y=top_varieties.index, palette='viridis')
plt.title('Top 10 Most Popular Wine Varieties')
plt.xlabel('Number of Reviews')
plt.ylabel('Variety')
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'top_varieties.png'))
print(f"\nVarieties plot saved: top_varieties.png")

print("\n--- Market Analysis: Top Wineries ---")
top_wineries = df['winery'].value_counts().head(10)
print("Top 10 Wineries by Review Count:")
print(top_wineries)

# Visualization: Top Wineries
plt.figure(figsize=(12, 6))
sns.barplot(x=top_wineries.values, y=top_wineries.index, palette='magma')
plt.title('Top 10 Wineries by Volume of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Winery')
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'top_wineries.png'))
print(f"Wineries plot saved: top_wineries.png")

# Best quality by country
print("\n--- Geographic Analysis: Average Quality by Country (Top 15 Countries) ---")
top_countries = df['country'].value_counts().head(15).index
country_quality = df[df['country'].isin(top_countries)].groupby('country')['points'].mean().sort_values(ascending=False)
print(country_quality)

plt.figure(figsize=(12, 6))
sns.boxplot(data=df[df['country'].isin(top_countries)], x='country', y='points', palette='Set3')
plt.xticks(rotation=45)
plt.title('Quality Distribution by Top 15 Countries')
plt.xlabel('Country')
plt.ylabel('Points')
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'quality_by_country.png'))
print(f"Country quality plot saved: quality_by_country.png")
