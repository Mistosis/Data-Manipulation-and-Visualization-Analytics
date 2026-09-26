import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
df = pd.read_csv(os.path.join(base_path, 'winemag_cleaned.csv'))

print("--- Step 5: Price Tier Segmentation ---")

def segment_price(price):
    if price < 15: return 'Budget (<$15)'
    elif price < 35: return 'Premium ($15-$35)'
    elif price < 100: return 'Luxury ($35-$100)'
    else: return 'Collector (>$100)'

df['price_tier'] = df['price'].apply(segment_price)

tier_counts = df['price_tier'].value_counts()
tier_quality = df.groupby('price_tier')['points'].mean().sort_values()

print("\nMarket Share by Price Tier:")
print(tier_counts)

print("\nAverage Quality per Tier:")
print(tier_quality)

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=tier_quality.index, y=tier_quality.values, palette='coolwarm')
plt.title('Average Quality (Points) by Price Segmentation')
plt.ylim(80, 100)
plt.ylabel('Avg Points')
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'price_segments.png'))

plt.figure(figsize=(8, 8))
plt.pie(tier_counts, labels=tier_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Market Share Distribution')
plt.savefig(os.path.join(base_path, 'price_pie_chart.png'))

print(f"\nGraphs saved: price_segments.png, price_pie_chart.png")
